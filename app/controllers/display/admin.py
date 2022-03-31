from data.configuration import CONFIGURATION


from flask import Blueprint, request, redirect, session, render_template, url_for, jsonify


display_admin = Blueprint('admin', __name__)


@display_admin.route("/login", methods=["GET", "POST"])
def render_admin_login():
    if request.method == "GET":
        return render_template("admin-login.html")
    else:
        if request.form['pass'] == CONFIGURATION['ADMIN_DASHBOARD_PASS']:
            session["is-admin-logged"] = 1
            return redirect(url_for("admin.display_admin_dashboard"))
        return redirect(url_for("admin.display_admin_login"))


@display_admin.route("/dashboard", methods=["GET"])
def render_admin_dashboard():
    if "is-admin-logged" in session.keys():
        return render_template("admin-dashboard.html")
    else:
        return redirect(url_for("admin.display_admin_login"))


@display_admin.route("/logout")
def logout_admin():
    session.pop('is-admin-logged', None)
    return redirect(url_for("admin.display_admin_login"))
