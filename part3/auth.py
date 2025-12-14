from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User

@api_v1.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Email and password required"}), 400

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=user.id,
        additional_claims={
            "is_admin": user.is_admin
        }
    )

    return jsonify({
        "access_token": access_token
    }), 200

