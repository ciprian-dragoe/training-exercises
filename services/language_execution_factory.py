from services import exercises, database


def manufacture(language_type):
    if language_type in FACTORY:
        return FACTORY[language_type]


def execute_sql(code, user, exercise_number):
    exercises.write_file(f"{user}-{exercise_number}-code.sql", code)
    query_result = database.execute_select(code)
    return query_result


def execute_js(code, user, exercise_number):
    exercises.write_file(f"{user}-{exercise_number}-code.js", code)
    return "True"


FACTORY = {
    "sql": execute_sql,
    "js": execute_js,
}
