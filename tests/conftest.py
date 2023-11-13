## Define testing here.
import tempfile
import pytest
import build_fixtures


build_fixtures.build_fixtures()
# Declaration of this as a fixture allows it to be reused in other tests.
# This allows for the integration tests to be built dynamically.
@pytest.fixture(name='data_layer', scope='package')
def makeThingStore():
    """This makes a temporary thing store."""
    class ThingStore():
        def __init__(self):
            return self
        def put(self, thing_name, thing_value):
            setattr(self, thing_name, thing_value)
        def get(self, thing_name):
            return getattr(self, thing_name)
    
    # Make a local empty testing directory for temporary artifacts.
    with tempfile.TemporaryDirectory() as t:
        yield ThingStore()
