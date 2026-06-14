# Initialize the Flask application factory
from flask import Flask

def create_app():
    """Application factory pattern - professional way to create Flask apps"""
    app = Flask(__name__)
    
    # Register blueprints (modular routing)
    from app.routes import main
    app.register_blueprint(main)
    
    return app