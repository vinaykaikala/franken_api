import pytest
from gene_query.test_app import main

# returns our flask app instance
@pytest.fixture
def app():
    app = main()
    return app
