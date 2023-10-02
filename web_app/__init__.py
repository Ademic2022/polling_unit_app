from flask import Flask
from datetime import timedelta
from models import storage

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'polling_unit_app'

    from web_app.routes import views
    app.register_blueprint(views, url_prefix='/')

    return app

def configure_db(app):
    with app.app_context():
        storage.reload()
    return app
