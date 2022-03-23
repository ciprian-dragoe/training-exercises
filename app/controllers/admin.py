from flask import Blueprint, request, redirect, session, render_template, url_for, jsonify


from services import docker, exercises
from data.configuration import CONFIGURATION
from services.set_timeout import SET_TIMEOUT


admin_route = Blueprint('admin', __name__)


@admin_route.route("/login", methods=["GET", "POST"])
def display_admin_login():
    if request.method == "GET":
        return render_template("admin-login.html")
    else:
        if request.form['pass'] == CONFIGURATION['ADMIN_DASHBOARD_PASS']:
            session["is-admin-logged"] = 1
            return redirect(url_for("admin.display_admin_dashboard"))
        return redirect(url_for("admin.display_admin_login"))


@admin_route.route("/dashboard", methods=["GET"])
def display_admin_dashboard():
    if "is-admin-logged" in session.keys():
        return render_template("admin-dashboard.html")
    else:
        return redirect(url_for("admin.display_admin_login"))


@admin_route.route("/logout")
def logout_admin():
    docker.kill_existing_containers()
    session.pop('is-admin-logged', None)
    exercises.delete_all_exercise_files()
    return redirect(url_for("admin.display_admin_login"))


@admin_route.route("/active-projects")
def get_active_projects():
    if "is-admin-logged" in session.keys():
        docker.initialize()
        SET_TIMEOUT.clear()
        SET_TIMEOUT.run(docker.kill_existing_containers, int(CONFIGURATION["DOCKER-KILL-TIMEOUT-SECONDS"]))
        projects = exercises.get_active_exercises()
        return jsonify(projects)
    return "not logged"
