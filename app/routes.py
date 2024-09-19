from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/exam')
def exam():
    return render_template('exam.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/informative')
def informative():
    return render_template('informative.html')