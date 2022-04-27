from data import database


def get_all_by_visibility(visibility):
    return database.execute(database.DbConnection.admin, f"""SELECT * FROM starter_projects where is_visible={visibility} order by name""")


def get_all_projects_with_files():
    return database.execute(database.DbConnection.admin, """
        SELECT p.id as project_id, p.name as project_name, f.id as file_id, f.name as file_name, f.content as file_content
        FROM starter_projects p
        inner join starter_files f on f.starter_project_id = p.id""")


def create(project):
    return database.execute(database.DbConnection.admin, f"""
        INSERT INTO starter_projects(name)
        VALUES (%(project_name)s) returning *;
    """, {"project_name": project['name']})[0]


def update_starter_file(project_id, file_id):
    return database.execute(database.DbConnection.admin, f"""
            update starter_projects
            set entry_point_starter_file_id = {file_id} 
            where id = {project_id}
            returning *;
        """)


def delete_by_name(name):
    return database.execute(database.DbConnection.admin, f"""
                update starter_projects set entry_point_starter_file_id = Null
                    where name = %(name)s;
                delete from starter_files 
                    where starter_project_id = (select id from starter_projects where name = %(name)s);
                delete from starter_projects
                    where name = %(name)s;
            """, {'name': name})
