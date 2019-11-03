from flask import Flask
from app.api.v1.views.Office import version_one as office_v1_blueprint
from app.api.v1.views.Party import version_one as party_v1_blueprint
from app.api.v1.views.v1_views_utils import version_one as v1_views_utils_blueprint


def create_app():
    """This is the application factory"""
    app = Flask(__name__)
    app.register_blueprint(office_v1_blueprint)
    app.register_blueprint(party_v1_blueprint)
    app.register_blueprint(v1_views_utils_blueprint)
    return app