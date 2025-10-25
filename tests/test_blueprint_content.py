"""This is a test script to test flask application content and functionality."""

import pytest
# Local application imports
from application.app import create_app


@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    # Use create_app() to instantiate the application
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as app_client:
        yield app_client


def test_bp_usage():
    """Test if there is a blueprint registered (part of resolving errors/full testing)"""
    app = create_app()
    assert 'homepage' in app.blueprints, "Homepage Blueprint was not registered!"


def test_main_page_content(client):
    """
    flask unit testing for content in default page:
    Check for 200 status and 'Blueprint' keyword.
    """
    # Access the Blueprint's default route ('/')
    response = client.get('/')

    # Check for successful connection (HTTP 200)
    assert response.status_code == 200

    # Check for the required keyword 'Blueprint' in the response content
    assert b"Blueprint" in response.data


def test_about_page_content(client):
    """
    flask unit testing for content in about page:
    Check for 200 status and 'Blueprint' keyword.
    """
    # Access the Blueprint's '/about' route
    response = client.get('/about')

    # Check for successful connection (HTTP 200)
    assert response.status_code == 200

    # Check for the required keyword 'Blueprint' in the response content
    assert b"Blueprint" in response.data
