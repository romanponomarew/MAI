-- Для установки функций в БД
-- psql -d fitness_club1 -f club_pg_script.sql -U postgres
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;
 
DROP TABLE IF EXISTS tickets CASCADE;
DROP TABLE IF EXISTS client_list CASCADE;
DROP TABLE IF EXISTS goods_sale CASCADE;
DROP TABLE IF EXISTS tickets_sales CASCADE;
DROP SCHEMA IF EXISTS goods_list CASCADE;
DROP SCHEMA IF EXISTS schedule CASCADE;
DROP SCHEMA IF EXISTS visit_tracking CASCADE;
DROP SCHEMA IF EXISTS training_types CASCADE;
DROP SCHEMA IF EXISTS services_list CASCADE;
DROP SCHEMA IF EXISTS employees_list CASCADE;
DROP DATABASE IF EXISTS  fitness_club1;

CREATE DATABASE fitness_club1;


\connect fitness_club1;

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--
CREATE SCHEMA public1;


--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';

SET search_path = public1;

--
-- Name: now(); Type: FUNCTION; Schema: public; Owner: -
--

CREATE OR REPLACE FUNCTION now() RETURNS timestamp with time zone
    LANGUAGE sql IMMUTABLE COST 0.00999999978
    AS $$SELECT '2016-10-13 17:00:00'::TIMESTAMP AT TIME ZONE 'Europe/Moscow';$$;

--
-- Name: FUNCTION now(); Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON FUNCTION now() IS 'Момент времени, относительно которого сформированы данные';

SET default_tablespace = '';

SET default_with_oids = false;

--Create Tables:


CREATE TABLE client_list (
	client_id int NOT NULL,
	surname varchar(50) NOT NULL,
	name varchar(50) NOT NULL);
CREATE TABLE

CREATE TABLE tickets (
	ticket_id int NOT NULL,
	training_type varchar(50) NOT NULL,
	price decimal(12,2) NOT NULL,
	visits_quantity int NOT NULL,
	service_type varchar(50) NOT NULL);
CREATE TABLE

CREATE TABLE goods_sale (
	client_id int NOT NULL,
	counts int NOT NULL,
	sale_id int NOT NULL,
	good_id int NOT NULL);
CREATE TABLE


CREATE TABLE tickets_sales (
	card_id int NOT NULL,
	remaining_number int NOT NULL,
	ticket_id int NOT NULL,
	client_id int NOT NULL);
CREATE TABLE


CREATE TABLE goods_list (
	good_id int NOT NULL,
	name varchar(50) NOT NULL,
	price decimal(12,2) NOT NULL);
CREATE TABLE

 
CREATE TABLE schedule (
	record_id int NOT NULL,
	employee_id int NOT NULL,
	service_id int NOT NULL,
	training_id int NOT NULL);
CREATE TABLE


CREATE TABLE visit_tracking (
	visit_id int NOT NULL,
	card_id int NOT NULL,
	record_id int NOT NULL);
CREATE TABLE
                                   ^
CREATE TABLE training_types (
	training_id int NOT NULL,
	training_type varchar(50) NOT NULL
);
CREATE TABLE


CREATE TABLE services_list (
	service_id int NOT NULL,
	service_type varchar(50) NOT NULL
);
CREATE TABLE

CREATE TABLE employees_list (
	employee_id int NOT NULL,
	surname varchar(50) NOT NULL,
	name varchar(50) NOT NULL,
	salary decimal(12,2) NOT NULL);
CREATE TABLE

--Adding Constraints

--Primary Keys:

ALTER TABLE tickets ADD
	CONSTRAINT PK_tickets PRIMARY KEY
	(
	ticket_id
	)
	;

ALTER TABLE client_list ADD
	CONSTRAINT PK_client_list PRIMARY KEY
	(
	client_id
	);

ALTER TABLE tickets_sales ADD
	CONSTRAINT PK_tickets_sales PRIMARY KEY
	(
	card_id
	);

ALTER TABLE goods_sale ADD
	CONSTRAINT PK_goods_sale PRIMARY KEY
	(
	sale_id
	);

ALTER TABLE goods_list ADD
	CONSTRAINT PK_goods_list PRIMARY KEY
	(
	good_id
	);

ALTER TABLE schedule ADD
	CONSTRAINT PK_schedule PRIMARY KEY
	(
	record_id
	);

ALTER TABLE visit_tracking ADD
	CONSTRAINT PK_visit_tracking PRIMARY KEY
	(
	visit_id
	);

ALTER TABLE training_types ADD
	CONSTRAINT PK_training_types PRIMARY KEY
	(
	training_id
	);

ALTER TABLE employees_list ADD
	CONSTRAINT PK_employees_list PRIMARY KEY
	(
	employee_id
	);

ALTER TABLE services_list ADD
	CONSTRAINT PK_services_list PRIMARY KEY
	(
	service_id
	);

--FOREIGN KEYS:

ALTER TABLE goods_sale ADD
	CONSTRAINT FK_goods_sale__client_list FOREIGN KEY
	(
	client_id
	) REFERENCES client_list (
	client_id
	)
	ON DELETE CASCADE ON UPDATE CASCADE
	;

ALTER TABLE goods_sale ADD
	CONSTRAINT FK_goods_sale__goods_list FOREIGN KEY
	(
	good_id
	) REFERENCES goods_list (
	good_id
	)
	ON DELETE CASCADE ON UPDATE CASCADE
	;

ALTER TABLE tickets_sales ADD
	CONSTRAINT FK_tickets_sales__tickets FOREIGN KEY
	(
	ticket_id
	) REFERENCES tickets (
	ticket_id
	)
	ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE tickets_sales ADD
	CONSTRAINT FK_tickets_sales__client_list FOREIGN KEY
	(
	client_id
	) REFERENCES client_list (
	client_id
	)
	ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE schedule ADD
	CONSTRAINT FK_schedule__employees_list FOREIGN KEY
	(
	employee_id
	) REFERENCES employees_list (
	employee_id
	)
	ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE schedule ADD
	CONSTRAINT FK_schedule__services_list FOREIGN KEY
	(
	service_id
	) REFERENCES services_list (
	service_id
	)
	ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE schedule ADD
	CONSTRAINT FK_schedule__training_types FOREIGN KEY
	(
	training_id
	) REFERENCES training_types (
	training_id
	)
	ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE visit_tracking ADD
	CONSTRAINT FK_visit_tracking__tickets_sales FOREIGN KEY
	(
	card_id
	) REFERENCES tickets_sales (
	card_id
	)
	ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE visit_tracking ADD
	CONSTRAINT FK_visit_tracking__schedule FOREIGN KEY
	(
	record_id
	) REFERENCES schedule (
	record_id
	)
	ON DELETE CASCADE ON UPDATE CASCADE;


---INSERT VALUES INTO TABLES:------------------------------------------------------------------

---------tickets----------------

---SELECT * FROM tickets;
--- training_type | price | visits_quantity | service_type | ticket_id 
---------------+-------+-----------------+--------------+-----------
---(0 строк)

insert into tickets values('MMA', 15000, 20, 'group_training', 1990);
insert into tickets values('Boxing', 12000, 20, 'group_training', 1895);
insert into tickets values('Fitness', 9000, 15, 'gym_training', 1896);
insert into tickets values('Fitness', 10000, 17, 'gym_training', 1996);
insert into tickets values('swimming', 15000, 17, 'swimming_pool', 1936);
insert into tickets values('MMA', 30000, 20, 'individual_training', 1946);

-------SELECT * FROM tickets;
 ----training_type |  price   | visits_quantity |    service_type     | ticket_id 
---------------+----------+-----------------+---------------------+-----------
 ---MMA           | 15000.00 |              20 | group_training      |      1990
 ---Boxing        | 12000.00 |              20 | group_training      |      1895
 ---Fitness       |  9000.00 |              15 | gym_training        |      1896
 ---Fitness       | 10000.00 |              17 | gym_training        |      1996
 ---swimming      | 15000.00 |              17 | swimming_pool       |      1936
 ---MMA           | 30000.00 |              20 | individual_training |      1946
----(6 строк)

---------client_list------------------

-------SELECT * FROM client_list;
 -------client_id | surname | name 
-----------+---------+------
------(0 строк)
                                              ^
insert into client_list values(135, 'Ivanov', 'Petr');
insert into client_list values(178, 'Petrov', 'Ivan');
insert into client_list values(58, 'Musaev', 'Semen');
insert into client_list values(98, 'Sidorov', 'Pavel');
insert into client_list values(149, 'Beglov', 'Ivan');
insert into client_list values(243, 'Ivanov', 'Victor');

-------  SELECT * FROM client_list;
 --------client_id | surname |  name  
-----------+---------+--------
-------       135 | Ivanov  | Petr
-------         178 | Petrov  | Ivan
-------          58 | Musaev  | Semen
-------          98 | Sidorov | Pavel
-------         149 | Beglov  | Ivan
-------         243 | Ivanov  | Victor
-------  (6 строк)

-----------------tickets_sales--------------

insert into tickets_sales values(34, 7, 1990, 135);
insert into tickets_sales values(56, 15, 1895, 178);
insert into tickets_sales values(15, 15, 1896, 58);
insert into tickets_sales values(98, 13, 1996, 98);
insert into tickets_sales values(41, 17, 1936, 149);
insert into tickets_sales values(66, 19, 1946, 243);

----------SELECT * FROM tickets_sales;
 ----------card_id | remaining_number | ticket_id | client_id 
-------------------+------------------+-----------+-----------
----------      34 |                7 |      1990 |       135
----------      56 |               15 |      1895 |       178
----------      15 |               15 |      1896 |        58
----------      98 |               13 |      1996 |        98
----------      41 |               17 |      1936 |       149
----------      66 |               19 |      1946 |       243
----------(6 строк)

-------------------goods_list--------------

insert into goods_list values(3, 'barbell', 7000);
insert into goods_list values(2, 'protein', 2000);
insert into goods_list values(1, 'towel', 500);
-------SELECT * FROM goods_list;
------- good_id |  name   |  price  
----------------+---------+---------
-------       3 | barbell | 7000.00
-------       2 | protein | 2000.00
-------       1 | towel   |  500.00
-------(3 строки)

-------------------goods_sale--------------

insert into goods_sale values(135, 2, 1, 2);
insert into goods_sale values(135, 1, 2, 1);
insert into goods_sale values(98, 1, 3, 3);
insert into goods_sale values(243, 3, 4, 1);
insert into goods_sale values(58, 2, 5, 3);

-------SELECT * FROM goods_sale;
------- client_id | counts | sale_id | good_id 
------------------+--------+---------+---------
-------       135 |      2 |       1 |       2
-------       135 |      1 |       2 |       1
-------        98 |      1 |       3 |       3
-------       243 |      3 |       4 |       1
-------        58 |      2 |       5 |       3
-------(5 строк)


-------------------training_types-------------

insert into training_types values(1, 'MMA');
insert into training_types values(2, 'Boxing');
insert into training_types values(3, 'Fitness');
insert into training_types values(4, 'swimming');

--------SELECT * FROM training_types;
-------- training_id | training_type 
---------------------+---------------
--------           1 | MMA
--------           2 | Boxing
--------           3 | Fitness
--------           4 | swimming
--------(4 строки)


-------------------services_list---------------

insert into services_list values(1, 'group_training');
insert into services_list values(2, 'gym_training');
insert into services_list values(3, 'swimming_pool');
insert into services_list values(4, 'individual_training');
------------SELECT * FROM services_list;
------------ service_id |    service_type     
------------------------+---------------------
------------          1 | group_training
------------          2 | gym_training
------------          3 | swimming_pool
------------          4 | individual_training
------------(4 строки)


------------------employees_list---------------

insert into employees_list values(1, 'Smirnov', 'Sergey', 70000);
insert into employees_list values(2, 'Kovalenko', 'Kirill', 90000);
insert into employees_list values(3, 'Cherchesov', 'Stanislav', 40000);
insert into employees_list values(4, 'Ignatenko', 'Igor', 70000);
insert into employees_list values(5, 'Kozlov', 'Anton', 35000);
---------SELECT * FROM employees_list;
--------- employee_id |  surname   |   name    |  salary  
----------------------+------------+-----------+----------
---------           1 | Smirnov    | Sergey    | 70000.00
---------           2 | Kovalenko  | Kirill    | 90000.00
---------           3 | Cherchesov | Stanislav | 40000.00
---------           4 | Ignatenko  | Igor      | 70000.00
---------           5 | Kozlov     | Anton     | 35000.00
---------(5 строк)


----------------schedule---------------

insert into schedule values(134, 2, 1, 1);
insert into schedule values(201, 3, 2, 3);
insert into schedule values(156, 1, 1, 2);
insert into schedule values(172, 4, 1, 2);
insert into schedule values(57, 5, 3, 4);
insert into schedule values(68, 2, 4, 1);

---------SELECT * FROM schedule;
--------- record_id | employee_id | service_id | training_id 
--------------------+-------------+------------+-------------
---------       134 |           2 |          1 |           1
---------       201 |           3 |          2 |           3
---------       156 |           1 |          1 |           2
---------        57 |           5 |          3 |           4
---------       172 |           4 |          1 |           2
---------        68 |           2 |          4 |           1
---------(6 строк)




----------------visit_tracking----------------------

insert into visit_tracking values(4, 34, 134);
insert into visit_tracking values(2, 15, 134);
insert into visit_tracking values(7, 98, 172);
insert into visit_tracking values(15, 41, 172);
insert into visit_tracking values(1, 66, 57);
insert into visit_tracking values(76, 15, 201);

--------SELECT * FROM visit_tracking;
-------- visit_id | card_id | record_id 
------------------+---------+-----------
--------        4 |      34 |       134
--------        2 |      15 |       134
--------        7 |      98 |       172
--------       15 |      41 |       172
--------        1 |      66 |        57
--------       76 |      15 |       201
--------(6 строк)


-----------functions-------------------

---------Function that returns quantity of goods sold----------
CREATE OR REPLACE FUNCTION count_good( good_type text)
 RETURNS bigint AS $$
 SELECT SUM(counts) FROM goods_sale as g_sale
 JOIN goods_list as g_list ON g_sale.good_id = g_list.good_id
 WHERE g_list.name = good_type;
$$ LANGUAGE sql;
 
------SELECT count_good('protein');
------ count_good 
------------------
------          2
------(1 строка)


--------Function returns coach's surname that training 'sport_type'
CREATE OR REPLACE FUNCTION sport_coach(sport_type text)
RETURNS text AS $$
SELECT DISTINCT coaches.surname as coach FROM employees_list as coaches
JOIN schedule ON coaches.employee_id = schedule.employee_id
WHERE schedule.training_id = (SELECT DISTINCT types.training_id FROM training_types as types
JOIN schedule ON schedule.training_id = types.training_id
WHERE types.training_type = sport_type);
$$ LANGUAGE sql;

-----SELECT sport_coach('Boxing');
----- sport_coach 
------------------
----- Ignatenko
-----(1 строка)




----------------triggers-----------------------------------------------------
CREATE OR REPLACE FUNCTION ndfl()
RETURNS trigger AS
$$
BEGIN 
 NEW.salary = NEW.salary*1.13;
 RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS ndfl ON employees_list;

CREATE TRIGGER ndfl BEFORE INSERT OR UPDATE ON employees_list
 FOR EACH ROW EXECUTE PROCEDURE ndfl();


CREATE OR REPLACE FUNCTION nds()
RETURNS trigger AS
$$
BEGIN
 NEW.price = NEW.price * 1.2;
 RETURN NEW;
END;
$$ LANGUAGE plpgsql;

 
CREATE TRIGGER nds BEFORE INSERT OR UPDATE ON goods_list    
 FOR EACH ROW EXECUTE PROCEDURE nds();













