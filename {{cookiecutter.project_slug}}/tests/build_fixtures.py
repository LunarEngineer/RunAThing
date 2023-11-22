"""Build pytest fixtures.

Pytest fixtures are helper functions which can be reused multiple
times. That means you can run 'big expensive test a' and many
'small test b' independently.

Normally pytest fixtures aren't accessible outside of the module
scope in which they're accessed.

Examine this file structure:

```
tests/
    things/
        test_thing.py
    other_things/
        test_other_thing.py
```

The testing structure here would run each test file independently.
That results in fixtures declared in test_thing not being able to
access the fixtures in test_other_thing.

That is 'fixed' with the below code.
"""

def build_fixtures():
    raise NotImplementedError