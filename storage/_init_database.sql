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
    client_id     INTEGER             NOT NULL
);

ALTER TABLE ONLY products
    ADD CONSTRAINT fk_products_client_id FOREIGN KEY (client_id) REFERENCES clients(id);

CREATE TABLE clients_and_products (
    id             INTEGER PRIMARY KEY NOT NULL,
    client_name    VARCHAR(200)        NOT NULL,
    product_price  SMALLINT            NOT NULL,
    product_name   VARCHAR(200)
);

INSERT INTO clients (id, name, telephone, mail) VALUES (1, 'Jessica', '2345', 'jessica@2345.com');
INSERT INTO clients (id, name, telephone, mail) VALUES (2, 'Mathiew', '1234', 'mathiew@1234.com');
INSERT INTO clients (id, name, telephone, mail) VALUES (3, 'Andrew', '3456', 'andrew@4567.com');INSERT INTO clients (id, name, telephone, mail) VALUES (1, 'Jessica', '2345', 'jessica@2345.com');

INSERT INTO products (id, name, price, client_id) VALUES (1, 'phone', 10, 1);
