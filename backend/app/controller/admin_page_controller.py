from flask_restplus import Resource, Namespace, abort
from flask import request, render_template, make_response
from app.service.products_service import *
from app.view.product import ProductForm

api = Namespace('page', description='admin manage products api')


@api.route('/index')
@api.route('')
class Index(Resource):
    @api.doc('get one or more products')
    def get(self):
        headers = {'Content-Type': 'text/html'}
        ok, result = get_all_product()
        if not ok:
            abort(500, result)
        products = result.to_dict(orient='records')
        return make_response(render_template('index.html', products=products), 200, headers)


@api.route('/detail')
class Detail(Resource):
    @api.doc('get one or more products')
    def get(self):
        headers = {'Content-Type': 'text/html'}
        params = request.args
        if 'id' not in params:
            abort(400, "product id is not valid.!!!")
        ok, result = get_one_product(params.get('id'))
        product = []
        if not ok:
            abort(500, result)
        products = result.to_dict(orient='records')
        if len(products) != 1:
            abort(500, "product is not existed or not valid!!!")
        else:
            product = products[0]
        return make_response(render_template('detail.html', product=product), 200, headers)


@api.route('/new')
class AddNew(Resource):
    @api.doc('get one or more products')
    def get(self):
        form, rp = generate_product_from()
        return rp

    @api.doc('get one or more products')
    def post(self):
        form, rp = generate_product_from()
        data = form.data
        return rp


def generate_product_from():
    headers = {'Content-Type': 'text/html'}
    form = ProductForm(meta={'csrf': False})
    return form, make_response(render_template('new.html', form=form), 200, headers)
