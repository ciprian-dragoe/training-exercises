from services.languages import language_execution_factory
from data.entities import files


def process(language, code, user_id=None, file_id=None):
    runner = language_execution_factory.manufacture(language)
    result = runner(code)
    if user_id and file_id and files.is_user_owning_file(user_id, file_id):
        files.update(file_id, code)
    return result
