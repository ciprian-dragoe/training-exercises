DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS clients_and_products;

CREATE TABLE clients (
    id         INTEGER PRIMARY KEY NOT NULL,
    name       VARCHAR(200)        NOT NULL,
    telephone  VARCHAR(200)        NOT NULL,
    mail       VARCHAR(200)        NOT NULL
);

CREATE TABLE products (
    id            INTEGER PRIMARY KEY NOT NULL,
    price         SMALLINT            NOT NULL,
    name          VARCHAR(200),
    client_id     INTEGER
);

ALTER TABLE ONLY products
    ADD CONSTRAINT fk_products_client_id FOREIGN KEY (client_id) REFERENCES clients(id);

CREATE TABLE clients_and_products (
    id             INTEGER PRIMARY KEY NOT NULL,
    client_name    VARCHAR(200)        ,
    client_phone   VARCHAR(200)        ,
    client_email   VARCHAR(200)        ,
    product_price  SMALLINT            ,
    product_name   VARCHAR(200)
);

INSERT INTO clients (id, name, telephone, mail) VALUES (1, 'Jessica', '2345', 'jessica@2345.com');
INSERT INTO clients (id, name, telephone, mail) VALUES (2, 'Mathew', '1234', 'mathiew@1234.com');
INSERT INTO clients (id, name, telephone, mail) VALUES (3, 'Andrew', '3456', 'andrew@4567.com');

INSERT INTO products (id, name, price, client_id) VALUES (1, 'phone', 10, 1);
INSERT INTO products (id, name, price, client_id) VALUES (2, 'car', 20, 1);
INSERT INTO products (id, name, price, client_id) VALUES (3, 'table', 100, 2);
INSERT INTO products (id, name, price, client_id) VALUES (4, 'chair', 200, 2);
INSERT INTO products (id, name, price, client_id) VALUES (5, 'fork', 300, 2);
INSERT INTO products (id, name, price) VALUES (6, 'bazooka', 2000);
INSERT INTO products (id, name, price) VALUES (7, 'katana', 3000);

INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price) VALUES (1, 'Jessica', '2345', 'jessica@2345.com', 'phone', 10);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price) VALUES (2, 'Jessica', '2345', 'jessica@2345.com', 'car', 20);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price) VALUES (3, 'Mathew', '1234', 'mathiew@1234.com', 'table', 100);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price) VALUES (4, 'Mathew', '1234', 'mathiew@1234.com', 'chair', 200);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price) VALUES (5, 'Mathew', '1234', 'mathiew@1234.com', 'fork', 300);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price) VALUES (6, 'Andrew', '2345', 'jessica@2345.com', null, null);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price) VALUES (7, null, null, null, 'bazooka', 2000);
INSERT INTO clients_and_products (id, client_name, client_email , client_phone, product_name, product_price) VALUES (8, null, null, null, 'katana', 3000);
