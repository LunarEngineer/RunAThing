# RunAThing

What happens when you have a bunch of projects and need to maintain them all?

This project abstracts a setup and forms the core of a CI-CD / workflow execution system.

It does this by building a minimal and reusable project which other repos will fork and auto-update to.

That implies that it has hooks which can be used as actions, and so this builds frames for the hooks that will allow you to test various things fairly quickly and easily.

This assumes that you have access to a central data layer where information is stored.

Arbitrary actions.

If it's arbitrary actions then each *set* of actions will fork from this.

A logical and narrowing dependency chain can be explicitly established. Neato.

Here at the root we assume very, very, little. We assume that this is a git project. We assume that you will have some source code in src, tests you wish to run in tests, and any environmental definition you want will be declared in an env; there's also potential other things associated with each one of these projects. (Metadata, e.g.)

We assume there is a data layer definition here which defines the scope of information accessible in local scope, parent scope, and potentially global scope.

This thing potentially depends on other things, upstream, and is potentially depended on by other things downstream. This is *implicitly declared* by referencing the data layer and reusing the data layer as the storage mechanism.
