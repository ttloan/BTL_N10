import json

from flask_restplus import Resource, Namespace, abort
from flask import Response, request
from app.service.products_service import *

api = Namespace('page', description='admin manage products api')


@api.route('/index')
@api.route('')
class Index(Resource):
    @api.doc('get one or more products')
    def get(self):
        return 'Hello index!'


@api.route('/detail')
class Detail(Resource):
    @api.doc('get one or more products')
    def get(self):
        pass


@api.route('/new')
class AddNew(Resource):
    @api.doc('get one or more products')
    def get(self):
        pass
