from ..server import api, UserNamespace
from ..models import user as UserService
from flask_restplus import fields, Resource, marshal


UserUpdateModel = api.model('User', {
    'firstName': fields.String(required=False),
    'lastName': fields.String(required=False),
    'age': fields.Integer(required=False)
})

UserCreateModel = api.model('User', {
    'firstName': fields.String(required=True),
    'lastName': fields.String(required=False),
    'age': fields.Integer(required=False)
})

UserModel = api.model('User', {
    'id': fields.Integer(readonly=True, required=True),
    'firstName': fields.String(required=True),
    'lastName': fields.String(required=False),
    'age': fields.Integer(required=False),
    'likes': fields.Integer(required=False)
})

UserLikeModel = api.model('UserLike', {
    'value': fields.Integer(required=True)
})

@UserNamespace.route('/')
class UserList(Resource):
    @UserNamespace.doc('users list')
    @UserNamespace.marshal_with(UserModel)
    def get(self):
        return UserService.find()

    @UserNamespace.doc('create a new user')
    @UserNamespace.expect(UserCreateModel)
    @UserNamespace.marshal_with(UserModel)
    def post(self):
        data = marshal(api.payload, UserCreateModel)
        return UserService.create(data=data)


@UserNamespace.route('/<int:pk>/')
@UserNamespace.response(404, 'User not found')
@UserNamespace.param('pk', 'The user identifier')
class UserDetails(Resource):
    @UserNamespace.doc('user details by pk')
    @UserNamespace.marshal_with(UserModel)
    def get(self, pk: int):
        user = UserService.findById(pk=pk)

        if user is not None:
            return user

        UserNamespace.abort(404, 'User with PK \'{}\' not found '.format(pk))

    @UserNamespace.doc('update user by pk')
    @UserNamespace.expect(UserUpdateModel)
    @UserNamespace.marshal_with(UserModel)
    def patch(self, pk: int):
        user = UserService.update(pk=pk, data=api.payload)

        if user is not None:
            return user

        UserNamespace.abort(404, 'User with PK \'{}\' not found '.format(pk))

    @UserNamespace.doc('delete user by pk')
    def delete(self, pk: int):
        user = UserService.delete(pk=pk)

        if user is not None:
            return user

        UserNamespace.abort(404, 'User with PK \'{}\' not found '.format(pk))


@UserNamespace.route('/<int:pk>/like/')
class UserLike(Resource):
    @UserNamespace.doc('like for user')
    @UserNamespace.expect(UserLikeModel)
    @UserNamespace.marshal_with(UserModel)
    def post(self, pk: int):

        user = UserService.like(pk=pk, value=api.payload['value'])

        if user is not None:
            return user

        UserNamespace.abort(404, 'User with PK \'{}\' not found '.format(pk))
