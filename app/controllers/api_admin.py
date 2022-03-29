from flask import Blueprint, session, jsonify


from services import docker, exercises
from data.configuration import CONFIGURATION
from services.set_timeout import SET_TIMEOUT


api_admin = Blueprint('api_admin', __name__)


@api_admin.route("/re", methods=["GET", "POST"])
def display_admin_login():
    if request.method == "GET":
        return render_template("admin-login.html")
    else:
        if request.form['pass'] == CONFIGURATION['ADMIN_DASHBOARD_PASS']:
            session["is-admin-logged"] = 1
            return redirect(url_for("admin.display_admin_dashboard"))
        return redirect(url_for("admin.display_admin_login"))


@api_admin.route("/dashboard", methods=["GET"])
def display_admin_dashboard():
    if "is-admin-logged" in session.keys():
        return render_template("admin-dashboard.html")
    else:
        return redirect(url_for("admin.display_admin_login"))


@api_admin.route("/logout")
def logout_admin():
    docker.stop_language_containers()
    session.pop('is-admin-logged', None)
    exercises.delete_all_exercise_files()
    return redirect(url_for("admin.display_admin_login"))


@api_admin.route("/active-projects")
def get_active_projects():
    if "is-admin-logged" in session.keys():
        try:
            docker.initialize()
            SET_TIMEOUT.clear()
            SET_TIMEOUT.run(docker.stop_language_containers, int(CONFIGURATION["DOCKER_KILL_TIMEOUT_SECONDS"]))
        except:
            print("THERE WAS A PROBLEM CONNECTING TO DOCKER")
        projects = exercises.get_active_exercises()
        return jsonify(projects)
    return "not logged"
