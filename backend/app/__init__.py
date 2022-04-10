from flask import Flask, Blueprint
from flask_restplus import Api

from app.controller.info_controller import api as info
from app.controller.api_controller import api as admin
from app.controller.page_controller import api as admin_page


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config/app.cfg')

    blueprint = Blueprint('bt_10', __name__)
    api = Api(blueprint, title='Gioi thieu thuc pham',
              version='1.0',
              description='trang web gioi thieu thuc pham cua nhom 10')
    app.register_blueprint(blueprint, url_prefix='/food-blog')
    api.add_namespace(info, '/info')
    api.add_namespace(admin, '/api')
    api.add_namespace(admin_page, '/page')

    return app
