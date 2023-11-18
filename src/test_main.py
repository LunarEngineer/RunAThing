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
        'test_config': {
            'fuck': 'yeah'
        },
        'file_structure_expectations': {
            
        }
    },
    # {},
]
@pytest.mark.parametrize(('test_case'), test_cases)
def test_deployment(test_case):
    """Walks through and documents what the project builds."""
    import tempfile
    with tempfile.TemporaryDirectory() as t:
        # Take the defaults
        _test_config = _base_config.copy()
        # Inherit the per test specific config.
        _test_config.update(test_case['test_config'])
        # And inherit the config specifying where to store stuff.
        _test_config.update({
            "cookiecutters_dir": f"{t}/cookiecutters",
            "replay_dir": f"{t}/replays"
        })
        print("Cloning the local into a temp bare workspace.")
        # Write the test case input out to a yaml config.
        with open(f'{t}/test_config.yml', 'w') as f:
            yaml.safe_dump(_test_config, f)
        # Set the environment variable for the cookiecutter config to use that.
        os.environ["COOKIECUTTER_CONFIG"] = f'{t}/test_config.yml'
        subprocess.run(f"git clone --bare file:///workspaces/RunAThing {t}/repo.git", shell=True)
        # It *must* be specified with a full file schema.
        make_project(f'file://{t}/repo.git', f'{t}/test', no_input=True)
        # This is what my file structure should look like.
        # with open(f'{t}/test/run-a-thing/pyproject.toml', 'r') as f:
        #     _ = f.readlines()
        raise Exception(os.listdir(f'{t}/test/run-a-thing'), "_")