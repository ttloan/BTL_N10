import json

from flask_restplus import Resource, Namespace, abort
from flask import Response, request
from app.service.products_service import *
from app.service.categories_service import *

api = Namespace('api', description='admin manage products api')


@api.route('/product')
class Product(Resource):
    @api.doc('get one or more products')
    def get(self):
        params = request.args
        if 'id' in params:
            ok, result = get_one_product(params.get('id'))
        elif 'type' in params:
            ok, result = get_product_by_type(params.get('type'))
        else:
            ok, result = get_all_product()
        if not ok:
            abort(500, result)
        return Response(result.to_json(orient='records'), mimetype='application/json')

    @api.doc('delete one product')
    def delete(self):
        params = request.json
        ok = False
        error = None
        if 'id' in params:
            ok, error = del_product_by_id(params.get('id'))
        else:
            abort(400, message="invalid id")
        if not ok:
            abort(500, message=error)
        return Response(json.dumps({'message': 'deleted success!!!'}), mimetype='application/json')

    @api.doc('add one new product')
    def post(self):
        params = request.json
        product = validate_product(params)
        ok, result = add_product(product)
        if not ok:
            abort(500, message=result)
        return Response(json.dumps({'message': 'insert success!!!'}), mimetype='application/json')


@api.route('/category')
class Category(Resource):
    @api.doc('get one or more category')
    def get(self):
        ok, result = get_all_category()
        if not ok:
            abort(500, result)
        return Response(result.to_json(orient='records'), mimetype='application/json')


def validate_product(params):
    result = convert_product_to_model(params)
    if len(result) != len(product_manager.PRODUCT_FIELDS):
        abort(400, message="invalid params")
    return result
