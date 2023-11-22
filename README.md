# RunAThing

So What: You want to run a project. You want that to be easy. You want to work with potentially everyone else. You want to just inherit a stable set of tools reusable for what you want to do. You want to *just be able to do what you want to do*.

You also want this to maybe go to production some day...

## What's the So What?

Dependencies are a pain in the ass. They break. Security flaws are found. Ugh, huge pain in the ass. Someone has to pay attention to all this stuff. So, best to automate it *as much as possible*.

This makes a project with cookiecutter that you can *stamp* out into your organization. That will form a single root project with the packaging flavor of your choice. This allows you to use that as a single git remote which you may track with many, many, subordinate projects that can all be updated *automatically* when the root updates. Oh yes, yes, that's pretty.

This provides a consistent and reusable base for inheriting default dependencies such that subsequent projects can be automatically updated per changes in the root. This project is monitored for security. (And as soon as I can enable it security updates will be automated.)

This will set you up with [tox](https://tox.wiki/en/latest/user_guide.html) as a local test runner and the ability to execute local actions; it will also define your data scope such that you can programatically access your data layers.

This mirrors a production environment, and as such it sets expectations for security, quality, and implementation.

This was heavily inspired by https://github.com/cicirello/python-github-action-template/ and https://github.com/audreyfeldroy/cookiecutter-pypackage.

## Contributing

If you'd like to contribute to this please keep in mind the vision of a future that's equitable for all. Those are the guidelines that drive development here. Reduce cost, ease access, simplify, enhance.

Feel free to open a PR!
