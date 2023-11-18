"""Deploy the project."""
import click
from cookiecutter.main import cookiecutter


def make_project(repo_folder, output_folder, no_input):
    cookiecutter(
        template=repo_folder,
        checkout=None,
        no_input=no_input,  # If test name isn't empty, run this without input.
        extra_context=None,
        replay=None,
        overwrite_if_exists=False,
        output_dir=output_folder,
        config_file=None,
        default_config=False,
        password=None,
        directory=None,
        skip_if_file_exists=False,
        accept_hooks=True,
        keep_project_on_failure=False
    )

@click.command()
@click.option('--repo-folder', prompt='Cookiecutter folder', help='The source code.')
@click.option('--output-folder', prompt='Output folder', help='Compiled project.')
@click.option('--test', prompt='Declare a test', help='Run a test.')
def main(repo_folder, output_folder, test):
    click.echo(f'Deploying project from: {repo_folder}')
    click.echo(f'Deploying project to: {output_folder}')
    click.echo(f'Test Execution: {test}')
    make_project(repo_folder=repo_folder, output_folder=output_folder, no_input=len(test))

if __name__=="__main__":
    main()