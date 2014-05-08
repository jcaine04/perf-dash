from flask import render_template, url_for, current_app, make_response
from . import main

@main.route('/')
def index():
    return render_template('index.html')