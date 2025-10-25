from flask import Blueprint, render_template

# Declare Blueprint object: name='homepage', template_folder='templates'
homepage_bp = Blueprint(
    'homepage',
    __name__,
    template_folder='templates'
)

@homepage_bp.route('/')
def home():
    """Renders the default route page with homepage.html template."""
    return render_template('homepage.html')

@homepage_bp.route('/about')
def about():
    """Renders the about route page with about.html template."""
    return render_template('about.html')