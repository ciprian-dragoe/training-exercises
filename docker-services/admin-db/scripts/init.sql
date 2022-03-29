CREATE TABLE IF NOT EXISTS users (
    id              SERIAL primary key,
    created_date    date                NOT NULL default now(),
    name            VARCHAR(100)        NOT NULL
);

CREATE TABLE IF NOT EXISTS starter_projects (
    id              SERIAL primary key,
    is_visible      bool                         default True,
    created_date    date                NOT NULL default now(),
    name            VARCHAR(100)        NOT NULL
);

CREATE TABLE IF NOT EXISTS starter_files (
    id                  SERIAL primary key,
    name                VARCHAR(100)        NOT NULL,
    content             VARCHAR(1000)       NOT NULL,
    created_date        date                NOT NULL default now(),
    starter_project_id  INTEGER             NOT NULL,
    CONSTRAINT fk_starter_projects
        FOREIGN KEY(starter_project_id)
            REFERENCES starter_projects(id)
);

CREATE TABLE IF NOT EXISTS projects (
    id                 SERIAL primary key,
    name               VARCHAR(100)        NOT NULL,
    created_date       date                NOT NULL default now(),
    starter_project_id integer,
    CONSTRAINT fk_starter_project_id
        FOREIGN KEY(starter_project_id)
            REFERENCES starter_projects(id),
    user_id            INTEGER,
    CONSTRAINT fk_users
        FOREIGN KEY(user_id)
            REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS files(
    id              SERIAL primary key,
    name            VARCHAR(100)        NOT NULL,
    content         VARCHAR(1000)       NOT NULL,
    created_date    date                NOT NULL default now(),
    project_id     INTEGER,
    CONSTRAINT fk_exercises
        FOREIGN KEY(project_id)
            REFERENCES projects(id)
);

------------------------ STORED PROCEDURES ------------------------
CREATE OR REPLACE FUNCTION get_or_create_user(user_name VARCHAR(100))
RETURNS users
LANGUAGE plpgsql
AS $function$
DECLARE
    result users%ROWTYPE;
BEGIN
    SELECT * into result FROM users where name = user_name;
    if result is not null then
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
    if result is not null then
        return result;
    else
        select name into project_name from starter_projects where id = starterProjectId;
        insert into projects(name, user_id, starter_project_id) values(project_name, userId, starterProjectId) returning * into result;
        insert into files(id, name, content, project_id) select id, name, content, result.id from starter_files where starter_project_id = starterProjectId;
        return result;
    end if;
END
$function$;

-- pagina starter projects
--   session storage daca e vre-un utilizator nume atunci prepopulez field
--     atunci cand incep proiect pun nume + id in session storage
--   get starter projects
-- pagina active project
--   create or get user by name
--   create or get project by user id and starter project id
--   create or get files by user id & project
--   execute code & update existing file content
-- pagina admin
--   get users with active projects
--   set visible starter projects
--     get all starter projects
--     update by project id
--   rehidrate
--     get all file names from disk
--     get all starter projects
--     delete starter projects that do not have those names and return the starter project id
--     delete starter files by range project ids
--     delete projects by range starter_project_ids and return theire ids
--     delete files by range project ids
--     create new starter projects based on missing names
--     create new starter files based on file names
--     get all users
--     get all user projects
