import boto3
from flask import Blueprint, Response, render_template_string

moving_bp = Blueprint('pages', __name__)
s3 = boto3.client('s3')
BUCKET_NAME = 'capstone-ajaimes'

# --- Helper function ---
def get_s3_text_file(key):
    """Fetch a text file (HTML or CSS) from S3 and decode it."""
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=key)
    return obj['Body'].read().decode('utf-8')

# --- HTML routes ---
@moving_bp.route('/')
def index():
    html = get_s3_text_file('frontend/templates/index.html')
    return render_template_string(html)

@moving_bp.route('/isos')
def isos():
    html = get_s3_text_file('frontend/templates/card.html')
    return render_template_string(html)

@moving_bp.route('/playbooks')
def playbooks():
    html = get_s3_text_file('frontend/templates/ansible.html')
    return render_template_string(html)

#--- Serve CSS directly from S3 ---
@moving_bp.route('/static/<filename>')
def serve_css(filename):
    """Serve CSS files from S3 (e.g. home.css)."""
    css_key = f'frontend/static/{filename}'
    css_content = get_s3_text_file(css_key)
    return Response(css_content, mimetype='text/css')

# --- File downloads ---
@moving_bp.route('/downloads/<filename>')
def download_file(filename):
    file_key = f'downloads/{filename}'
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=file_key)
    return Response(
        obj['Body'].read(),
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )
