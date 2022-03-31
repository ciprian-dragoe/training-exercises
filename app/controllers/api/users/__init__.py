from flask import Blueprint


from controllers.api.users.files import api_files


api_users = Blueprint('api/user/', __name__)
api_users.register_blueprint(api_files, url_prefix='<int:user_id>/files')
