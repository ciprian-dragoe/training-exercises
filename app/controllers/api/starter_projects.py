from services import starter_projects


from flask import Blueprint, jsonify


api_starter_projects = Blueprint('api/starter-projects/', __name__)


@api_starter_projects.route("/")
def get_starter_projects():
    results = starter_projects.get_all_by_visibility()
    return jsonify({"starter_projects": results})
