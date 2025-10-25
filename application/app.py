# application/app.py

from flask import Flask, render_template

# Import your Blueprint object from the new location
from .bp.homepage.homepage import homepage_bp

"""Flask Application factory for Blueprint assignment."""


def create_app():
    app = Flask(__name__)

    # --- Blueprint Registration ---
    # Register your homepage Blueprint to the Flask app
    app.register_blueprint(homepage_bp, url_prefix='/')

    # --- Legacy Routes (Defined INSIDE the factory function) ---

    @app.route('/legacy_hello')
    def hello_world():
        """Displays the default greeting."""
        return 'Hello CPS3500!'

    @app.route('/legacy_new_page')
    def new_page():
        """Displays the new page content."""
        return 'This is a New Page!'

    @app.route('/user/<name>')
    def user_greeting(name):
        """Renders the user info template with the greeting logic."""
        # NOTE: Assumes 'user_info.html' is in the main application's template folder
        return render_template('user_info.html', username=name)

    # The factory function MUST return the app instance
    return app


if __name__ == '__main__':
    # This block executes ONLY when the script is run directly (for local testing)
    app = create_app()
    app.run(debug=True)

# NOTE: Ensure you have a blank line after this line!
