{{ cookiecutter.template_components.header }}

from setuptools import setup


setup(
    name="sample_project",
    install_requires={{ cookiecutter.project_dependencies.python.deps }}
)
