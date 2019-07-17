from flask_restplus import Api

api = Api(
    version='1.0', title='Users API',
    description='A simple Users API',
)

UserNamespace = api.namespace('users', description='User actions')
