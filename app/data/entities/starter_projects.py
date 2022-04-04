from data import database


def get_all_project_names():
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, """SELECT name, id FROM starter_projects""")


def get_all_projects_with_files():
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, """
        SELECT p.id as project_id, p.name as project_name, f.id as file_id, f.name as file_name, f.content as file_content
        FROM starter_projects p
        inner join starter_files f on f.starter_project_id = p.id""")


def create(project):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
        INSERT INTO starter_projects(name)
        VALUES (%(project_name)s) returning *;
    """, {"project_name": project['name']})[0]


def update_starter_file(project_id, file_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
            update starter_projects
            set entry_point_file_id = {file_id}) 
            where id = {project_id}
            returning *;
        """)


def delete_by_name(name):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
                delete from starter_projects
                where name = %(name)s
            """, {'name': name})
