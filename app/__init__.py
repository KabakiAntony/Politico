from flask import Flask
from app.api.v1.views.Office import version_one as office_v1_blueprint


def create_app():
    """This is the application factory"""
    app = Flask(__name__)
    app.register_blueprint(office_v1_blueprint)
    return app