from flask import Blueprint


from controllers.display.users.projects import display_projects


display_users = Blueprint('/users', __name__)
display_users.register_blueprint(display_projects, url_prefix='<int:user_id>/projects')
