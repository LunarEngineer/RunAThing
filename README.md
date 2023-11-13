# RunAThing - Python

This provides a consistent and reusable base for inheriting default dependencies such that subsequent projects can be automatically updated per changes in the root.

This will set you up with tox as a local test runner and the ability to execute local actions.

This mirrors a production environment, and as such it sets expectations for security, quality, and implementation.

This was heavily inspired by https://github.com/cicirello/python-github-action-template/

## Development Notes

This is intended to assist enabling arbitrary actions in a central framework.

If it's arbitrary actions then each *set* of actions will fork from this.

A logical and narrowing dependency chain can be explicitly established.

Here at the root we assume very, very, little. We assume that this is a git project. We assume that you will have some source code in src, tests you wish to run in tests, and any environmental definition you want will be declared in an env; there's also potential other things associated with each one of these projects. (Metadata, e.g.)

We assume there is a data layer definition here which defines the scope of information accessible in local scope, parent scope, and potentially global scope.

This thing potentially depends on other things, upstream, and is potentially depended on by other things downstream. This is *implicitly declared* by referencing the data layer and reusing the data layer as the storage mechanism.

Requirements which are found to apply to a higher level will migrate upstream.

## Github Actions

The workflow defined in this project...