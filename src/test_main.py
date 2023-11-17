import os
import subprocess
from main import make_project

def test_deployment():
    import tempfile
    with tempfile.TemporaryDirectory() as t:
        print("Cloning the local into a temp bare workspace.")
        os.environ["COOKIECUTTER_CONFIG"] = "src/test_config.yml"
        subprocess.run(f"git clone --bare file:///workspaces/RunAThing {t}/repo.git", shell=True)
        make_project(f'{t}/repo.git', f'{t}/test', no_input=True)
        raise Exception("HEY!")