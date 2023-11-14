"""Parse a configuration file.

This picks up a config.ini in order to automatically generate
the required files needed for packaging.

Those files are intended to be ephemeral, as the environment they
build may be dynamic. It allows for package versions to be
explicitly declared at the root level and be inherited / overridden
deeper in the chain.

The configuration files written out are biased, but intended to
provide a project the capability to bootstrap to a functional
state and remain in touch with a secure remote.

TODO: GITHOOK
"""
import re
import subprocess
import yaml
from typing import Any, List, Mapping, Tuple
from io import TextIOWrapper

__TEMPLATE_HEADER__ = """###AutoGeneratedDocument
# This file is automatically generated.
# Rerunning the packaging script will not respect your changes.
# If you wish to implement change do that within your config.yaml.
"""

def _break_across_lines(items: List[str], white_space: int = 0) -> str:
    """Produce appropriate output for ini given input."""
    output_str = ''
    for item in items:
        output_str += f"\n{' '* white_space}{item}"
    return output_str
    

def build_setup_py(config_mapping: Mapping[str, Any]) -> str:
    """Return setup.py str"""
    # Note all this is done explicitly for clarity sake.
    _name: str = config_mapping["project_name"]
    _project_deps: str = config_mapping["project_dependencies"]["python"]["deps"]

    return f"""{__TEMPLATE_HEADER__}
from setuptools import setup, find_packages


setup(
    name="{_name}",
    install_requires={_project_deps}
)
    """


def build_pyproject_toml(config_mapping: Mapping[str, Any]) -> str:
    """Return pyproject.toml str"""
    # Note all this is done explicitly for clarity sake.
    _reqs: Mapping[str, Any] = config_mapping['project_dependencies']
    _build_reqs: List[str] = _reqs['python']['build_deps']
    return f"""{__TEMPLATE_HEADER__}
[build-system]
requires = {_build_reqs}
build-backend = "setuptools.build_meta"
"""


def build_setup_cfg(config_mapping: Mapping[str, Any]) -> str:
    """Return setup.cfg str"""
    # Note all this is done explicitly for clarity sake.
    _project_author: str = config_mapping["project_author"]
    _project_author_email: str = config_mapping["project_author_email"]
    _project_name: str = config_mapping["project_name"]
    _project_description: str = config_mapping["project_description"]
    _python_project_dependencies: Mapping[str, Any] = config_mapping["project_dependencies"]["python"]
    _python_min_version: str = _python_project_dependencies["min_version"]
    _python_package_deps: str = _break_across_lines(_python_project_dependencies["deps"], 4)
    _python_test_deps: str = _break_across_lines(_python_project_dependencies["test_deps"], 4)
    try:
        _remote_url = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url']).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        raise Exception("Unable to build setup.py: Is this a git project?")

    return f"""{__TEMPLATE_HEADER__}

[metadata]
name = "{_project_name}"
version = file: VERSION
author = "{_project_author}"
author_email = "{_project_author_email}"
description = "{_project_description}"
long_description = file: README.md
long_description_content_type = text/markdown
url = {_remote_url}
license = "LICENSE"

[options]
packages = find:
python_requires = >={_python_min_version}

[options.extras_require]
dev = {_python_test_deps}
"""


def _parse_pyversion(version_string: str) -> Tuple[str, str]:
    """Parse major and minor python version.
    
    This uses regular expression parsing to turn
    `'3.10'` into `(3, 10)`. That allows for version
    comparison."""
    try:
        major, minor = re.search(r'(\d+\.\d+)', version_string).group(1).split('.')
        if (not major) or (not minor):
            raise NotImplementedError("Please pass a python version string like 3.10")
        if not major == '3':
            raise NotImplementedError(f"Only Python 3 for now, not {major} from {version_string}")
        # There's potentially more validation...
        major = int(float(major))
        minor = int(float(minor))
        return major, minor
    except BaseException as e:
        raise TypeError(f"Unable to determine python version from {version_string}")


def build_tox_ini(config_mapping: Mapping[str, Any]) -> str:    
    """Return setup.cfg str"""
    # Note all this is done explicitly for clarity sake.
    _python_project_dependencies: Mapping[str, Any] = config_mapping["project_dependencies"]["python"]
    # Versions
    _python_min_version: Tuple[int, int] = _parse_pyversion(_python_project_dependencies["min_version"])
    _python_max_version: Tuple[int, int] = _parse_pyversion(_python_project_dependencies["max_version"])
    _py_ver_string = ','.join([f'3{str(_)}' for _ in range(_python_min_version[1], _python_max_version[1])])

    return f"""{__TEMPLATE_HEADER__}
[tox]
requires =
    tox>=4
env_list = lint, type, py{{{_py_ver_string}}}

[testenv]
description = Setup for the testing suite.

commands =
    pytest {{posargs:tests}}
[testenv:lint]
description = run linters
skip_install = true
deps =
    black==22.12
commands = black {{posargs:.}}

[testenv:type]
description = run type checks
deps =
    mypy>=0.991
commands =
    mypy {{posargs:src tests}}
"""



def build_config(config_file: TextIOWrapper):
    """Build reusable configuration.

    This writes out the setup.py, pyproject.toml, setup.cfg, and tox.ini
    required for a Python project.
    """
    # First try to load the config_file
    config_mapping = yaml.safe_load(config_file)
    _setup_py_str = build_setup_py(config_mapping)
    with open('setup.py', 'w') as setup_pyfile:
        setup_pyfile.write(_setup_py_str)
    _pyproject_toml_str = build_pyproject_toml(config_mapping)
    with open('pyproject.toml', 'w') as setup_pyproject_tomlfile:
        setup_pyproject_tomlfile.write(_pyproject_toml_str)
    _setup_cfg_str = build_setup_cfg(config_mapping)
    with open('setup.cfg', 'w') as setup_configfile:
        setup_configfile.write(_setup_cfg_str)
    _tox_ini_str = build_tox_ini(config_mapping)
    with open('tox.ini', 'w') as tox_inifile:
        tox_inifile.write(_tox_ini_str)


if __name__ == '__main__':
    with open('config.yaml', 'r') as config_file:
        build_config(config_file)
