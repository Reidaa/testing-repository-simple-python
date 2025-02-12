import json

from flask import Blueprint, jsonify
from flask_jwt_extended import current_user, jwt_required

from src.env import env
from src.Repository import repository
from src.utils.misc import capitalize_name

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/id")
@jwt_required()
def get_user_id():
    data = repository.read()

    try:
        return f"Your id is : {data['users'].index(current_user['username'])}", 200
    except ValueError:
        return jsonify(
            {
                "name": "Bad Request",
                "msg": "This username is already used.",
                "solution": "Try again.",
                "status_code": 400,
            }
        )


@user_bp.route("/hello")
@jwt_required()
def get_hello():
    return f"Hello {capitalize_name(current_user['username'])}"
