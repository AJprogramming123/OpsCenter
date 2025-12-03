import boto3
import mimetypes
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
def docker():
    html = get_s3_text_file('frontend/templates/card.html')
    return render_template_string(html)

@moving_bp.route('/playbooks')
def playbooks():
    html = get_s3_text_file('frontend/templates/ansible.html')
    return render_template_string(html)

@moving_bp.route('/docker')
def isos():
    html = get_s3_text_file('frontend/templates/docker.html')
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


#---------------------------------------#
#NEW UPDATES - Around Thanksgiving time
@moving_bp.route('/images/<filename>')
def serve_png(filename):
    s3_key = f'frontend/images/{filename}'
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=s3_key)
    return Response(obj['Body'].read(), mimetype='image/png')


#--------------------------------------#
#Routes to AWS Guides just generated before deadline

@moving_bp.route('/aws')
def aws():
    html = get_s3_text_file('frontend/templates/aws.html')
    return render_template_string(html)

@moving_bp.route('/aws/multicdn')
def multi_cdn():
    html = get_s3_text_file('frontend/templates/aws/multicdn.html')
    return render_template_string(html)

@moving_bp.route('/aws/s3backend')
def s3_backend():
    html = get_s3_text_file('frontend/templates/aws/s3backend.html')
    return render_template_string(html)

@moving_bp.route('/aws/security')
def security():
    html = get_s3_text_file('frontend/templates/aws/security.html')
    return render_template_string(html)
