CREATE TABLE IF NOT EXISTS users (
    id              SERIAL primary key,
    created_date    date                NOT NULL default now(),
    name            VARCHAR(100)        NOT NULL
);

CREATE TABLE IF NOT EXISTS starter_projects (
    id                          SERIAL primary key,
    is_visible                  bool                         default True,
    created_date                date                NOT NULL default now(),
    name                        VARCHAR(100)        NOT NULL,
    entry_point_starter_file_id INTEGER
);

CREATE TABLE IF NOT EXISTS starter_files (
    id                  SERIAL primary key,
    name                VARCHAR(100)        NOT NULL,
    content             VARCHAR(3000),
    created_date        date                NOT NULL default now(),
    starter_project_id  INTEGER             NOT NULL,
    CONSTRAINT fk_starter_projects
        FOREIGN KEY(starter_project_id)
            REFERENCES starter_projects(id)
);

ALTER TABLE starter_projects
ADD CONSTRAINT fk_entry_point_starter_files
FOREIGN KEY (entry_point_starter_file_id)
REFERENCES starter_files (id);

CREATE TABLE IF NOT EXISTS projects (
    id                 SERIAL primary key,
    name               VARCHAR(100)        NOT NULL,
    created_date       date                NOT NULL default now(),
    starter_project_id integer,
    CONSTRAINT fk_starter_project
        FOREIGN KEY(starter_project_id)
            REFERENCES starter_projects(id),
    user_id            INTEGER,
    CONSTRAINT fk_users
        FOREIGN KEY(user_id)
            REFERENCES users(id),
    entry_point_file_id INTEGER
);

CREATE TABLE IF NOT EXISTS files(
    id              SERIAL primary key,
    name            VARCHAR(100)        NOT NULL,
    content         VARCHAR(3000)       NOT NULL,
    created_date    date                NOT NULL default now(),
    project_id     INTEGER,
    CONSTRAINT fk_projects
        FOREIGN KEY(project_id)
            REFERENCES projects(id)
);

ALTER TABLE projects
ADD CONSTRAINT fk_entry_point_file
FOREIGN KEY (entry_point_file_id)
REFERENCES files (id);


------------------------ STORED PROCEDURES ------------------------
CREATE OR REPLACE FUNCTION get_or_create_user(user_name VARCHAR(100))
RETURNS users
LANGUAGE plpgsql
AS $function$
DECLARE
    result users%ROWTYPE;
BEGIN
    SELECT * into result FROM users where name = user_name;
    if found then
        return result;
    else
        insert into users(name) values(user_name) returning * into result;
        return result;
    end if;
END
$function$;

CREATE OR REPLACE FUNCTION get_or_create_project(userId int, starterProjectId int)
RETURNS projects
LANGUAGE plpgsql
AS $function$
DECLARE
    result projects%ROWTYPE;
    project_name varchar(100);
BEGIN
    SELECT * into result FROM projects where user_id = userId and starter_project_id = starterProjectId;
    if found then
        return result;
    else
        select name into project_name from starter_projects where id = starterProjectId;
        insert into projects(name, user_id, starter_project_id) values(project_name, userId, starterProjectId) returning * into result;
        insert into files(name, content, project_id) select name, content, result.id from starter_files where starter_project_id = starterProjectId;
        update projects set entry_point_file_id = (select id from files where project_id = result.id and name like '%main.%') where id = result.id;
        return result;
    end if;
END
$function$;
