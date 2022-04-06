from controllers.api.users.projects import api_projects
from data.entities import users


from flask import Blueprint, jsonify, request


api_users = Blueprint('api/users/', __name__)
api_users.register_blueprint(api_projects, url_prefix='<int:user_id>/projects')


@api_users.route("/", methods=["Post"])
def create_user_project():
    user = users.get_or_create(request.json['name'])
    return jsonify({"user": user})
