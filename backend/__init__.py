import os
from flask import Flask
from .moving import moving_bp

def create_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend'))
    template_folder = os.path.join(base_dir, 'templates')
    static_folder = os.path.join(base_dir, 'static')

    app = Flask(
        __name__,
        template_folder=template_folder,
        static_folder=static_folder
    )

    # Set path to /downloads at the project root
    app.config['DOWNLOADS_FOLDER'] = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../downloads')
    )

    app.register_blueprint(moving_bp)

    return app
