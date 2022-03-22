DROP DATABASE IF EXISTS practice;
CREATE DATABASE practice;

DROP TABLE IF EXISTS products_price_history;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS clients_and_products;
DROP TABLE IF EXISTS addresses;


CREATE TABLE addresses (
    idA        INTEGER PRIMARY KEY NOT NULL,
    city       VARCHAR(200)        NOT NULL
);


CREATE TABLE clients (
    idC        INTEGER PRIMARY KEY NOT NULL,
    first_name VARCHAR(200)        NOT NULL,
    telephone  VARCHAR(200)        NOT NULL,
    mail       VARCHAR(200)        NOT NULL,
    address_id INTEGER
);

CREATE TABLE products (
    idP           INTEGER PRIMARY KEY NOT NULL,
    price         SMALLINT            NOT NULL,
    name          VARCHAR(200),
    client_id     INTEGER
);

CREATE TABLE products_price_history (
    idPPH          INTEGER PRIMARY KEY NOT NULL,
    start_time     VARCHAR(200)                ,
    end_time       VARCHAR(200)                ,
    observations   VARCHAR(200)                ,
    product_price  SMALLINT                    ,
    product_id     SMALLINT NOT NULL
);

CREATE TABLE clients_and_products (
    id             INTEGER PRIMARY KEY NOT NULL,
    client_name    VARCHAR(200)        ,
    client_phone   VARCHAR(200)        ,
    client_email   VARCHAR(200)        ,
    product_price  SMALLINT            ,
    address_id     integer             ,
    product_name   VARCHAR(200)
);

ALTER TABLE ONLY clients
    ADD CONSTRAINT fk_address_address_id FOREIGN KEY (address_id) REFERENCES addresses(idA);

ALTER TABLE ONLY products
    ADD CONSTRAINT fk_products_client_id FOREIGN KEY (client_id) REFERENCES clients(idC);

ALTER TABLE ONLY products_price_history
    ADD CONSTRAINT fk_products_product_id FOREIGN KEY (product_id) REFERENCES products(idP);

INSERT INTO addresses (idA, city) VALUES (1, 'Bucharest[Jessica]');

INSERT INTO clients (idC, first_name, telephone, mail, address_id) VALUES (1, 'Jessica', '2345', 'jessica@2345.com', 1);
INSERT INTO clients (idC, first_name, telephone, mail) VALUES (2, 'Mathew', '1234', 'mathiew@1234.com');
INSERT INTO clients (idC, first_name, telephone, mail) VALUES (3, 'Andrew', '3456', 'andrew@4567.com');

INSERT INTO products (idP, name, price, client_id) VALUES (1, 'phone[Jessica]', 10, 1);
INSERT INTO products (idP, name, price, client_id) VALUES (2, 'car[Jessica]', 20, 1);
INSERT INTO products (idP, name, price, client_id) VALUES (3, 'table[Mathew]', 100, 2);
INSERT INTO products (idP, name, price, client_id) VALUES (4, 'chair[Mathew]', 200, 2);
INSERT INTO products (idP, name, price, client_id) VALUES (5, 'fork[Mathew]', 300, 2);
INSERT INTO products (idP, name, price) VALUES (6, 'bazooka', 2000);
INSERT INTO products (idP, name, price) VALUES (7, 'katana', 3000);

INSERT INTO products_price_history (idPPH, start_time, end_time, product_price, product_id, observations) VALUES (1, '01.01.2000', '01.02.2000', 10, 1, 'phone[Jessica]');
INSERT INTO products_price_history (idPPH, start_time, end_time, product_price, product_id, observations) VALUES (2, '01.03.2000', '01.04.2000', 20, 1, 'phone[Jessica]');
INSERT INTO products_price_history (idPPH, start_time, end_time, product_price, product_id, observations) VALUES (3, '01.04.2000', '01.05.2000', 30, 1, 'phone[Jessica]');

INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price, address_id) VALUES (1, 'Jessica', '2345', 'jessica@2345.com', 'phone', 10, 1);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price, address_id) VALUES (2, 'Jessica', '2345', 'jessica@2345.com', 'car', 20, 1);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price, address_id) VALUES (3, 'Mathew', '1234', 'mathiew@1234.com', 'table', 100, null);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price, address_id) VALUES (4, 'Mathew', '1234', 'mathiew@1234.com', 'chair', 200, null);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price, address_id) VALUES (5, 'Mathew', '1234', 'mathiew@1234.com', 'fork', 300, null);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price, address_id) VALUES (6, 'Andrew', '2345', 'jessica@2345.com', null, null, null);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price, address_id) VALUES (7, null, null, null, 'bazooka', 2000, null);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price, address_id) VALUES (8, null, null, null, 'katana', 3000, null);
