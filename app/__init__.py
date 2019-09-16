from flask import Flask

def create_app():
    """This is the application factory"""
    app = Flask(__name__)
    return app