from flask import Blueprint


from controllers.api.users.projects import api_projects


api_users = Blueprint('api/user/', __name__)
api_users.register_blueprint(api_projects, url_prefix='<int:user_id>/projects')
