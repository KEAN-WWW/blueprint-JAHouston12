"""This is a test script to test flask application using the Application Factory pattern."""

from application.app import create_app

def test_bp_usage():
    """Test if the 'homepage' blueprint is successfully registered."""
    # 1. Create the application instance using the factory function
    app = create_app()

    # 2. Assert that the blueprint named 'homepage' is in the app's blueprints collection
    assert 'homepage' in app.blueprints, "Homepage Blueprint was not registered!"
