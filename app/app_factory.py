# Import the Flask class from the flask module
from flask import Flask


# Function to create and configure the Flask application
def create_app():
    # Create an instance of the Flask class
    app = Flask(__name__)

    # Return the Flask application instance
    return app
