import boto3
from flask import Blueprint, Response

moving_bp = Blueprint('pages', __name__)

# Create S3 client (no credentials needed — IAM handles it)
s3 = boto3.client('s3')
BUCKET_NAME = 'capstone-ajaimes'

# --- Serve HTML templates directly from S3 ---
@moving_bp.route('/')
def index():
    obj = s3.get_object(Bucket=BUCKET_NAME, Key='frontend/templates/index.html')
    html = obj['Body'].read().decode('utf-8')
    return Response(html, mimetype='text/html')

@moving_bp.route('/isos')
def home():
    obj = s3.get_object(Bucket=BUCKET_NAME, Key='frontend/templates/card.html')
    html = obj['Body'].read().decode('utf-8')
    return Response(html, mimetype='text/html')

@moving_bp.route('/playbooks')
def about():
    obj = s3.get_object(Bucket=BUCKET_NAME, Key='frontend/templates/ansible.html')
    html = obj['Body'].read().decode('utf-8')
    return Response(html, mimetype='text/html')

@moving_bp.route('/docker-scripts')
def docker_scripts():
    obj = s3.get_object(Bucket=BUCKET_NAME, Key='frontend/templates/docker.html')
    html = obj['Body'].read().decode('utf-8')
    return Response(html, mimetype='text/html')




# --- Serve download files (Ansible, YAML, etc) ---
@moving_bp.route('/downloads/<filename>')
def download_file(filename):
    file_key = f'downloads/{filename}'
    file_obj = s3.get_object(Bucket=BUCKET_NAME, Key=file_key)
    return Response(
        file_obj['Body'].read(),
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )
