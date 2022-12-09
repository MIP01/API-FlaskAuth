from flask import Blueprint
from controllers.UserController import list, insert, show, update, delete
user_bp = Blueprint('user_bp', __name__)
user_bp.route('/', methods=['GET'])(list)
user_bp.route('/', methods=['POST'])(insert)
user_bp.route('/<int:user_id>', methods=['GET'])(show)
user_bp.route('/<int:user_id>', methods=['PUT'])(update)
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete)