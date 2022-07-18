from data.configuration import CONFIGURATION


from flask import Blueprint, request, redirect, session, render_template, url_for, jsonify


display_admin = Blueprint('admin', __name__)


@display_admin.route("/login", methods=["GET", "POST"])
def render_admin_login():
    if request.method == "GET":
        upgrade_to_https = request.host_url[-8:-1] == 'loca.lt' or request.host_url[-9:-1] == 'ngrok.io'
        return render_template("admin-login.html", upgrade_to_https=upgrade_to_https)
    else:
        if request.form['pass'] == CONFIGURATION['ADMIN_DASHBOARD_PASS']:
            session["is-admin-logged"] = 1
            return redirect('/admin/dashboard')
        return redirect('/admin/login')


@display_admin.route("/dashboard", methods=["GET"])
def render_admin_dashboard():
    if "is-admin-logged" in session.keys():
        upgrade_to_https = request.host_url[-8:-1] == 'loca.lt' or request.host_url[-9:-1] == 'ngrok.io'
        return render_template("admin-dashboard.html", upgrade_to_https=upgrade_to_https)
    else:
        return redirect('/admin/login')


@display_admin.route("/logout")
def logout_admin():
    session.pop('is-admin-logged', None)
    return redirect('/admin/login')
