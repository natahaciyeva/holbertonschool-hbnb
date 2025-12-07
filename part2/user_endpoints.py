from flask_restx import Namespace, Resource, fields
from services.user_service import UserService

api = Namespace("users", description="User management endpoints")
service = UserService()

user_model = api.model("User", {
    "id": fields.String(readonly=True),
    "email": fields.String(required=True),
    "first_name": fields.String,
    "last_name": fields.String,
})

create_user_model = api.model("CreateUser", {
    "email": fields.String(required=True),
    "password": fields.String(required=True),
    "first_name": fields.String,
    "last_name": fields.String
})

update_user_model = api.model("UpdateUser", {
    "email": fields.String,
    "password": fields.String,
    "first_name": fields.String,
    "last_name": fields.String
})

@api.route("/")
class UserList(Resource):

    @api.marshal_list_with(user_model)
    def get(self):
        """List all users"""
        users = service.list_users()
        # Exclude passwords
        return [u.to_dict() for u in users]

    @api.expect(create_user_model)
    @api.marshal_with(user_model, code=201)
    def post(self):
        """Create a new user"""
        data = api.payload
        user = service.create_user(data)
        return user.to_dict(), 201


@api.route("/<string:user_id>")
class UserResource(Resource):

    @api.marshal_with(user_model)
    def get(self, user_id):
        """Get a single user by ID"""
        user = service.get_user(user_id)
        if not user:
            api.abort(404, "User not found")
        return user.to_dict()

    @api.expect(update_user_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Update an existing user"""
        data = api.payload
        user = service.update_user(user_id, data)
        if not user:
            api.abort(404, "User not found")

        return user.to_dict()

