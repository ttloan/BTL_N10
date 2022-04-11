from flask_restplus import Resource, Namespace
api = Namespace('', description='info api')


@api.route('')
class HealthCheck(Resource):
    @api.doc('health check')
    def get(self):
        return 'Hello World!'

