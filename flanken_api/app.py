import logging.config
import click
from flask import Flask, Blueprint

from flanken_api import settings
from flanken_api.api.flanken.endpoints.flanken_api import ns as flanken_namespace
from flanken_api.api.flanken.endpoints.referral_db_api import ns2 as referral_namespace
from flanken_api.api.restplus import api
from flanken_api.database import db

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['PROBIO'] = settings.MOUNT_POINT_PROBIO
    flask_app.config['PSFF'] = settings.MOUNT_POINT_PSFF

def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(flanken_namespace)
    api.add_namespace(referral_namespace)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)


app = Flask(__name__)

@click.command()
@click.option('-p', '--port', type=int, default=5000)
def main(port):
    initialize_app(app)
    logging.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format('localhost'))
    app.run(debug=settings.FLASK_DEBUG, port=port, host='0.0.0.0')
