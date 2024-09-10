import os
import tempfile
from behave import fixture, use_fixture

from app import create_app  

@fixture
def flaskr_client(context, *args, **kwargs):
    app = create_app()
    app.testing = True
    context.app = app.test_client()
    yield context.app

def before_feature(context, feature):
    # -- HINT: Recreate a new app client before each feature is executed.
    use_fixture(flaskr_client, context)