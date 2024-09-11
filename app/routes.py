# Import the render_template function from the flask module
from flask import render_template

# Import the app instance from the current package
from . import app

# Define the route for the home page
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Define the route for the about page
@app.route('/about')
def about():
    # Render the about.html template
    return render_template('about.html')

# Define the route for the exam page
@app.route('/exam')
def exam():
    # Render the exam.html template
    return render_template('exam.html')
