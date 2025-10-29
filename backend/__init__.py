import boto3
from flask import Flask
from .moving import moving_bp

def create_app():
    app = Flask(__name__)

    # Configure S3 client
    app.config['S3_BUCKET'] = 'mycapstonebucket'
    app.config['S3_FRONTEND_PATH'] = 'frontend'
    app.config['S3_DOWNLOADS_PATH'] = 'downloads'
    app.s3 = boto3.client('s3')

    app.register_blueprint(moving_bp)

    return app
