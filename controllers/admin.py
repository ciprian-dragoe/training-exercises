from flask import Blueprint, request, redirect, session, render_template, url_for
import bcrypt
import os
admin_route = Blueprint('admin', __name__)
salt = bcrypt.gensalt()
hard_codded_hashed_password = bcrypt.hashpw(os.environ.get("ADMIN_PASS").encode(), salt)


@admin_route.route("/login", methods=["GET", "POST"])
def display_admin_login():
    if request.method == "GET":
        return render_template("admin-login.html")
    else:
        if verify_password(request.form['pass'], hard_codded_hashed_password):
            session["user-logged"] = 1
            return redirect(url_for("admin.display_admin_dashboard"))
        return redirect(url_for("admin.display_admin_login"))


@admin_route.route("/dashboard", methods=["GET"])
def display_admin_dashboard():
    if "user-logged" in session.keys():
        return render_template("admin-dashboard.html")
    else:
        return redirect(url_for("admin.display_admin_login"))


def verify_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)
