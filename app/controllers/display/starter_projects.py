from flask import Blueprint, render_template, request


display_starter_projects = Blueprint('starter-projects', __name__)


@display_starter_projects.route("/")
def render_exercises():
    # todo: find a more elegant solution to differentiate when a request is done via https
    upgrade_to_https = request.host_url[-8:-1] == 'loca.lt'
    return render_template("starter-projects.html", upgrade_to_https=upgrade_to_https)

