from data import database


def get_all():
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
        SELECT f.name, f.content, p.name as project_name, p.entry_point_starter_file_id
        FROM starter_files f
        inner join starter_projects p on f.starter_project_id = p.id
    """)


def create(file):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
            insert into starter_files(name, content, starter_project_id)
            values(%(file_name)s, %(file_content)s, {file['starter_project_id']}) 
            returning *
        """, {
        'file_name': file['name'],
        'file_content': file['content'],
    })[0]


def delete(file_id):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
            update starter_projects set entry_point_starter_file_id = NULL where entry_point_starter_file_id = {file_id};
            delete from starter_files where id = {file_id};
        """)


def update_content(file_id, new_content):
    connection = database.get_db_connection(database.DbConnection.admin)
    return database.execute(connection, f"""
                update starter_files
                set content = %(new_content)s
                where id = {file_id}
                returning *;
            """, { 'new_content': new_content})[0]
