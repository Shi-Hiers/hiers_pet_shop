# This file creates the Flask app and imports the routes.
from flask import Flask, g
from .app_factory import create_app

# Create the Flask application instance
app = create_app()

# Set the secret key for session management and other security-related features
app.secret_key = 'your-secret'

from . import routes



