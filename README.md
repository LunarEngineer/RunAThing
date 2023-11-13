# RunAThing - Python

This provides a consistent and reusable base for inheriting default dependencies such that subsequent projects can be automatically updated per changes in the root.

This will set you up with tox as a local test runner and the ability to execute local actions.

This mirrors a production environment, and as such it sets expectations for security, quality, and implementation.

This was heavily inspired by https://github.com/cicirello/python-github-action-template/

## Project Structure

This assumes that you're using setuptools to build the Python package and that your environment is appropriately configured to do that.

If you're using the devcontainer, that should be true.

The major configuration files for this project are:

1. [`setup.cfg`](setup.cfg): Primary configuration - This file declares all package dependencies *and* testing dependencies. Note the defaults and their versions. These are updated such that you may simply pull updates from this file and they can be reasonably assumed they are the most secure and appropriate.
2. [`pyproject.toml`](pyproject.toml): Secondary configuration - This file is used but shouldn't ever really need be updated.
3. [`setup.py`](setup.py): Ditto.
4. [`tox.ini`](tox.ini): This is used to run the testing actions on the source code. There are a number of environments and they deserve their own documentation.

The major sections of things that are convenient to understand for this project are:

1. [`.devcontainer`](.devcontainer/): This houses a standard container template for a development environment that supports package installation, testing, and execution. This also has a place to set some of the environment variables in that environment, which is useful. These influence the testing environment.
2. [`.github`](.github/): This houses the CI implemented in github and defines how this package implements the above workflow. Note the additional dependencies introduced here in the actions.
3. [`docs`](docs/): This houses the documentation. This is auto-built by CI.
4. [`src`](src/): Go build something here. Reuse the template.
5. [`tests`](src/): This defines how your thing is tested. Go ensure this makes sense for you.

## Packaging

This uses setuptools and distlib to create releasable code that's reusable across both Windows and Linux.

## Testing

This uses tox to run:
1. Linting and formatting - Tox will run ruff; check [`tox.ini`](tox.ini) for the ruff section.
2. Static typing - Tox will run mypy; check [`tox.ini`](tox.ini) for the mypy section.
3. Dependency testing - Tox can run safety; check [`tox.ini`](tox.ini) for the safety section. **This is not available for enterprise use unless you [use an appropriate key](https://pypi.org/project/safety/).**
3. Security testing - Tox will run bandit; check [`tox.ini`](tox.ini) for the bandit section. If you're looking for additional security you can look into tools like Snyk, GitGuardian, and pyup.io.
4. Unit testing - Tox will run pytest; check [`tox.ini`](tox.ini) for the testing section and check the [`conftest.py`](tests/conftest.py) for test setup.
5. Integration testing - Tox, during the pytest run, will run an integration test. Check the [`conftest.py`](tests/conftest.py) fixtures section for more information.
6. Documentation Generation - Tox will assume that you have Python code with numpy style docstrings and will use Sphinx to auto-generate that documentation. Please see the [`conf.py`](docs/conf.py)
7. GitHub Integration Test- Tox will use Act to test workflows locally as if GitHub was the execution engine.

## Versioning

This uses semantic release to determine versioning.

## Releasing

This will release by creating a tag and pushing to PyPi pending successful execution of the Github workflows defined in [`.github`](.github)

## License

Please see the [license](LICENSE).

## Publishing

This uses setuptools to publish; you're required to [create a Pypi account](https://pypi.org/) in order to do that.

## Distribution

This creates binaries and makes them accessible with tags; it does this by using sdist and committing them to the git project with short-hand commit tag notation.

## Security

This uses standard tooling to validate code security and safety.
For more information see the testing section above.

## Contributing

If you'd like to contribute to this please keep in mind the vision of a future that's equitable for all. Those are the guidelines that drive development here. Reduce cost, ease access, simplify, enhance.

Feel free to open a PR!
