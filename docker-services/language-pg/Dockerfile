# syntax=docker/dockerfile:1
FROM postgres
COPY ./docker-services/language-pg/scripts/init.sql /docker-entrypoint-initdb.d/init.sql
