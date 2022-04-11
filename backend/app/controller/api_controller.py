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
            ok, result = get_product_by_type(params.get('type'), params.get('size'))
        elif 'latest' in params:
            ok, result = get_latest_product(params.get('size'))
        elif 'deal' in params:
            ok, result = get_deal_product(params.get('size'))
        elif 'count' in params:
            ok, result = count()
            data = json.dumps({'count': result})
            data = "%s(%s)" % (params['callback'], data) if 'callback' in params else data
            return Response(data, mimetype='application/json')
        else:
            size = params.get('size') if 'size' in params else None
            page = params.get('page') if 'page' in params else None
            ok, result = get_all_product(size, page)
        if not ok:
            abort(500, result)
        data = result.to_json(orient='records')
        data = "%s(%s)" % (params['callback'], data) if 'callback' in params else data
        return Response(data, mimetype='application/json')

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
