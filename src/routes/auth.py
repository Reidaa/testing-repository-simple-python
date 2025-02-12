from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from src.Repository import repository

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.post("/authenticate")
def authenticate():
    try:
        username = request.form["username"]
    except KeyError:
        return jsonify(
            {
                "name": "Bad Request",
                "msg": "Need username to be authenticated.",
                "solution": "Try again.",
                "status_code": 400,
            }
        )

    data = repository.read()

    try:
        id = data["users"].index(username)
    except ValueError:
        id = len(data["users"])

    identity = {
        "id": id,
        "username": username,
    }

    access_token = create_access_token(
        identity=identity,
        fresh=True,
        additional_claims={},
    )

    response = {
        "success": True,
        "return": {
            "access": access_token,
        },
        "code": 200,
    }

    resp = jsonify(response)

    repository.insert(username)

    return resp
