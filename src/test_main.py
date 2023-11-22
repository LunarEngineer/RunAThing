"""Test recipes.

This tests particular recipes to validate that the Thing framework
can pick them up and reuse them.

This shows how to push something through the framework and shows,
in general, what's expected of a reusable Thing.

Each test case is defined by the recipe file in the thing templates.

That recipe file includes both metadata and the default cookiecutter
input template providing the default values used in test.
"""
import os
import pytest
import subprocess
import yaml
from main import make_project

_base_config = {
    "default_context": {
        "full_name": "Testing Function",
        "email": "nomail@example.com",
    }
}


test_cases = [
    {
        'test_description': {
            'name': 'setup.cfg packaging',
            'description': "".join([
                "This uses a simple recipe to create"
            ])
        }
        'test_config': {
            'heck': 'yeah'
        },
        'file_structure_expectations': {
            
        }
    },
    # {},
]
@pytest.mark.parametrize(('test_case'), test_cases)
def test_deployment(test_case):
    """Walks through and documents what the project builds, and how."""
    import tempfile
    with tempfile.TemporaryDirectory() as t:
        # Set up Cookiecutter
        _cookiecutter_setup(test_case, t)
        # Reuse the local, simple, functionality, to make the project in test.
        # This is it, this is all you need. Everything else is twiddling config.
        make_project(f'file://{t}/repo.git', f'{t}/test', no_input=True)
        # Investigate the structure of the built project in an interactive
        #   and documenty way. Yes, that's an adjective.
        _package_files_validation()
        _test_files_validation()
        # Now, we're going to go ahead and run the testing framework.
        _run_tests()
        # And finally we're going to go ahead and publish to pypi (not really)
        _thing_publication_validation()
        raise Exception(os.listdir(f'{t}/test/run-a-thing'), "_")


def _cookiecutter_setup(test_case: dict[str, dict[str, str]], test_folder: str):
    """Set up Cookiecutter for the test.
    
    This will ensure that Cookiecutter is set up to use without breaking.
    It will set the local configuration up to ensure that the cookiecutter
    directory is in a temporary location.
    It will then clone that into the test folder.
    """
    # Take the defaults
    _test_config = _base_config.copy()
    # Inherit the per test specific config.
    _test_config.update(test_case['test_config'])
    # And inherit the config specifying where to store stuff.
    _test_config.update({
        "cookiecutters_dir": f"{test_folder}/cookiecutters",
        "replay_dir": f"{test_folder}/replays"
    })
    # Write the test case input out to a yaml config.
    with open(f'{test_folder}/test_config.yml', 'w') as f:
        yaml.safe_dump(_test_config, f)
    # Set the environment variable for the cookiecutter config to use that.
    os.environ["COOKIECUTTER_CONFIG"] = f'{test_folder}/test_config.yml'
    subprocess.run(f"git clone --bare file:///workspaces/RunAThing {test_folder}/repo.git", shell=True)


def _package_files_validation():
    """Unpack and validate structure and test install.
    
    This reads in the files used for packaging. It validates their
    contents and ensures that the package *should* be installable.
    It does not attempt to install at this time.
    """
    with open(f'{t}/test/run-a-thing/pyproject.toml', 'r') as f:
        pyproject_toml = f.read()
    with open(f'{t}/test/run-a-thing/setup.cfg', 'r') as f:
        setup_cfg = f.read()
    with open(f'{t}/test/run-a-thing/setup.py', 'r') as f:
        setup_py = f.read()
    raise NotImplementedError("READ DOCSTRING FOR REQUIREMENTS")


def _test_files_validation():
    """Unpack and validate the testing framework."""
    with open(f'{t}/test/run-a-thing/tox.ini', 'r') as f:
        tox_ini = f.read()
    raise NotImplementedError("READ DOCSTRING FOR REQUIREMENTS")


def _run_tests():
    raise NotImplementedError("READ DOCSTRING FOR REQUIREMENTS")


def _thing_publication_validation():
    raise NotImplementedError("READ DOCSTRING FOR REQUIREMENTS")