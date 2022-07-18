import services.projects
from services import users
from services import projects
from services import docker
from services import files
from services import sync_disk_projects_db_projects


from flask import Blueprint, session, jsonify


api_admin = Blueprint('api/admin', __name__)


@api_admin.route("/users")
def get_users_with_projects():
    if "is-admin-logged" in session.keys():
        result = users.get_users_with_projects()
        return jsonify(result)
    response = jsonify({'message': 'Not authorized'})
    return response, 404


@api_admin.route("/projects/<int:project_id>/files", methods=["Get"])
def get_files(project_id):
    if "is-admin-logged" in session.keys():
        result = files.get_files(project_id)
        return jsonify(result)
    else:
        response = jsonify({'message': 'Not authorized'})
        return response, 404


@api_admin.route("/projects", methods=["DELETE"])
def delete_projects():
    if "is-admin-logged" in session.keys():
        result = projects.delete_all()
        return jsonify(result)
    else:
        response = jsonify({'message': 'SUCCESS'})
        return response, 404


@api_admin.route("/sync-starter-projects")
def reload_starter_projects():
    if "is-admin-logged" in session.keys():
        sync_disk_projects_db_projects.start()
        return jsonify({'message': 'SUCCESS'})
    else:
        response = jsonify({'message': 'Not authorized'})
        return response, 404


@api_admin.route("/keep-language-environments-active")
def set_containers_state():
    if "is-admin-logged" in session.keys():
        try:
            docker.start()
            return jsonify({"message": "SUCCESS"})
        except:
            return jsonify({"message": "There was a problem starting the container, check logs"})
    else:
        response = jsonify({'message': 'Not authorized'})
        return response, 404




# todo - add extra wrapper for every admin call to verify credentials
