from data.database import admin_connection, execute_select


@admin_connection
def get_files(connection, project_id):
    return execute_select(connection, f"""select * from files where project_id = {project_id}""")


@admin_connection
def update_file(connection, file_id, content):
    return execute_select(connection,
                          f"""update files set content=%(content)s where id = {file_id}""",
                          {"content": content})
