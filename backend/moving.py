from flask import Blueprint, render_template

moving_bp = Blueprint('pages', __name__)

@moving_bp.route('/')
def start():
    return render_template('index.html')

@moving_bp.route('/home')
def home():
    return render_template('home.html') 

@moving_bp.route('/about')
def about():
    return render_template('stuff/about.html')

