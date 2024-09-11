# Import the app instance from the app package
from app import app

# Check if the script is executed directly (and not imported)
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)