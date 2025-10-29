from flask import Blueprint, Response, send_file, render_template_string
from io import BytesIO
import boto3

moving_bp = Blueprint('pages', __name__)
s3 = boto3.client('s3')
BUCKET_NAME = 'capstone-ajaimes'

# HTML routes
@moving_bp.route('/')
def index():
    obj = s3.get_object(Bucket=BUCKET_NAME, Key='frontend/templates/index.html')
    html = obj['Body'].read().decode('utf-8')
    return render_template_string(html)  # will process any Jinja

@moving_bp.route('/isos')
def home():
    obj = s3.get_object(Bucket=BUCKET_NAME, Key='frontend/templates/card.html')
    html = obj['Body'].read().decode('utf-8')
    return render_template_string(html)

# Static assets
@moving_bp.route('/static/<path:filename>')
def static_files(filename):
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=f'frontend/static/{filename}')
    return send_file(BytesIO(obj['Body'].read()), attachment_filename=filename)
