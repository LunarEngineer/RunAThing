{{ cookiecutter.template_components.header }}

from setuptools import setup


setup(
    install_requires={{ cookiecutter.project_dependencies.python.deps }}
)
