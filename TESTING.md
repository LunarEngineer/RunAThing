# Testing Plan

The test suite will use cookiecutter and try to create a python package, verifying some information.

If you ask the testing suite nicely, it will keep the output.

Now, is this project appropriate for the testing suite?

What happens when you cookiecut over a previously cut cookie?

## What is tested, and how.

1. Run-A-Thing can deploy and install: This is intended to allow you to bootstrap a thing from scratch. A single line of code will take the pacakge to an initial deployment, assuming you know in general what you want. This validates installation and import.
2. Dependencies: The Run-A-Thing code and dependencies, which are intended to be minimal, are free of security and safety issues.
3. Regression / Integration Testing: This automatically creates tests that validate whether the outputs of your workflows have changed as a result of changes in code or dependencies.
4. Performance Testing: Every thing you build should be auditable for the effort required to run them. The Run-A-Thing framework handles all of that and it is validated here.
