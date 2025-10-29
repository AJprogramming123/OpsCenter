from flask import Blueprint, Response, send_file, render_template_string
from io import BytesIO
import boto3

moving_bp = Blueprint('pages', __name__)
s3 = boto3.client('s3')
BUCKET_NAME = 'capstone-ajaimes'

# --- Serve HTML templates directly from S3 ---
def render_s3_template(key):
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=key)
    html = obj['Body'].read().decode('utf-8')
    return render_template_string(html)

@moving_bp.route('/')
def index():
    return render_s3_template('frontend/templates/index.html')

@moving_bp.route('/isos')
def home():
    return render_s3_template('frontend/templates/card.html')

@moving_bp.route('/playbooks')
def about():
    return render_s3_template('frontend/templates/ansible.html')

# --- Serve static files (CSS, JS, images) from S3 ---
@moving_bp.route('/static/<path:filename>')
def static_files(filename):
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=f'frontend/static/{filename}')
    return send_file(BytesIO(obj['Body'].read()), download_name=filename)

# --- Serve downloadable files from S3 ---
@moving_bp.route('/downloads/<filename>')
def download_file(filename):
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=f'downloads/{filename}')
    return send_file(BytesIO(obj['Body'].read()), download_name=filename, as_attachment=True)
