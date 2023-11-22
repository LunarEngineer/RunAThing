
## Development Notes

File Checklist:

* Setup.cfg
* pyproject.toml
* setup.py
* tox.ini

https://github.com/cookiecutter/cookiecutter/blob/main/.github/workflows/tests.yml

## TODO:
Note that DevContainer Features is an appropriate place to expose the thing store as a built in data layer.
Simply define them as a feature and then they're rebuildable.

Timthoughts: the pattern of cookiecutter has value in implementation, but why? fork stays current, cookiecutter needs link. cookiecutter does point back, though. I say this module should be included as a submodule for an ancillary project. Integration at that point can refine, enhance, and simplify.

```sh
python src/utils/build_config.py
pip install -e .[dev]
```

This makes a default setup.

Development Plan:

The Thing Store inherits this.

Input Expectation:

* Python version.
* Tox version.
* Package versions.

Given these, this will generate all required documentation, including a container specification and packaging, for a custom Python environment.

Check out the config.yaml. It's boss.

This is intended to assist enabling arbitrary actions in a central framework.

If it's arbitrary actions then each *set* of actions will fork from this.

A logical and narrowing dependency chain can be explicitly established.

Here at the root we assume very, very, little. We assume that this is a git project. We assume that you will have some source code in src, tests you wish to run in tests, and any environmental definition you want will be declared in an env; there's also potential other things associated with each one of these projects. (Metadata, e.g.)

We assume there is a data layer definition here which defines the scope of information accessible in local scope, parent scope, and potentially global scope.

This thing potentially depends on other things, upstream, and is potentially depended on by other things downstream. This is *implicitly declared* by referencing the data layer and reusing the data layer as the storage mechanism.

Requirements which are found to apply to a higher level will migrate upstream.

This uses setuptools.

This 'freezes' the main branch.

https://github.com/marketplace

* https://github.com/marketplace/actions/semantic-version
* https://github.com/marketplace/actions/pypi-publish
# That implies this makes a distribution

This is an example of packaging in github ci.

https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/


These are runners for tox:
* https://github.com/marketplace/actions/tox-env
* https://github.com/ymyzk/tox-gh-actions
* https://github.com/marketplace/actions/python-tox-on-fedora (This appears at a shallow glance the most stable / maintained)



## Local Development

This uses *tox* to run workflows locally, or remotely.

That allows for a standard setup routine which can be inherited across projects that defines default dependencies for all projects which reuse this.

tox, actions, github, gitlab, commonality? JOB INDEPENDENT.

What does this do? It takes a formatted, versioned, dataset, and uses it to build and run either local or remote jobs.

This uses the local data layer to request the workflow and run it remotely in the test suite.

This can build github actions.

This can build gitlab actions.

This can be used in a Python environment.

This requires the thing store.


PATTERN: SOURCE CODE IS JOB INDEPENDENT.

EVERY RUN

There's a github actions local extension.

## Github Actions

The workflow defined in this project...

* Build: This builds the project.