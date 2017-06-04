# -*- coding: utf-8 -*-
"""User resources."""

from flask_jwt import jwt_required
from flask_restful import Resource, fields, marshal, marshal_with, reqparse

from {{cookiecutter.app_name}}.models.users import User

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')
parser.add_argument('email')


resource_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
}


class UserView(Resource):
    """UserView API."""

    @jwt_required()
    def get(self, user_id):
        """Get a user."""
        user = User.get_by_id(user_id)
        if user:
            return marshal(user, resource_fields), 201
        return 'User not found', 404

    @jwt_required()
    def put(self, user_id, **kwargs):
        """Update a user."""
        user = User.get_by_id(user_id)
        if user:
            args = parser.parse_args()
            for arg, val in args.items():
                if val:
                    # if a value is provided for an attr, then update its value
                    setattr(user, arg, val.encode())

            user.save()
            return marshal(user, resource_fields), 201

        return 'User not found', 404


class UserViewList(Resource):
    """UserViewList API."""

    @jwt_required()
    @marshal_with(resource_fields)
    def get(self):
        """List users."""
        return User.query.all(), 200

    def post(self):
        """Register user."""
        args = parser.parse_args()

        user = User.query.filter_by(username=args['username']).first()
        if user:
            return 'User already exists', 409

        user = User.query.filter_by(email=args['email']).first()
        if user:
            return 'Email already registered', 409

        return marshal(User.create(username=args['username'],
                                   email=args['email'],
                                   password=args['password']), resource_fields), 201
