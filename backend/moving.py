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
    return render_template('about.html')

# Example additional routes for your buttons
@moving_bp.route('/isos')
def isos():
    return render_template('card.html')

@moving_bp.route('/playbooks')
def playbooks():
    return render_template('ansible.html')

@moving_bp.route('/docker-scripts')
def docker_scripts():
    return render_template('docker.html')
