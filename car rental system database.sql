create database cars;

use cars;

create table vehicle
  (id    int,
   class_id    int,
   vehicle_type    varchar(40),
   model   varchar(50),
   cost    int(10),
   primary key (id, class_id)
  );




create table vehicle_details
  (id    int,
   color    varchar(50),
   motor_CCs  int,
   vehicle_year       int,
   primary key (id)
  );



create table rental
  (id    int,
   customer_id    int,
   recieve_date   date,
   return_date       date,
  vehicle_id      int,
  class_id       int,
   primary key (id)
  );





create table customer
  (id    int,
   gender   varchar(50),
   DOB   date,
   name      varchar(50),
  emaile_id      int,
  job      varchar(50),
  email    varchar(50),
  address  varchar(50),
   primary key (id));


create table agency
  (id    int,
   location   varchar(50),
   primary key (id))
   ;









#insert statements
INSERT INTO `cars`.`customer` (`id`, `gender`, `DOB`, `name`, `emaile_id`, `job`, `email`, `address`) VALUES ('3', 'male', '1990-4-4', 'mowafeek', '221', 'hammam', 'icewiuf@oasinjid', 'alexandria');

INSERT INTO `cars`.`vehicle` (`id`, `class_id`, `vehicle_type`, `model`, `cost`) VALUES ('3', '300', 'audi', 'a-5', '3500'); 

INSERT INTO `cars`.`vehicle_details` (`id`, `color`, `motor_CCs`, `vehicle_year`) VALUES ('4','red',2500,2014);

INSERT INTO `cars`.`vehicle_details` (`id`, `color`, `motor_CCs`, `vehicle_year`) VALUES ('3','red',2500,2019);

INSERT INTO `cars`.`agency` (`id`, `location`) VALUES ('7','helwan');

INSERT INTO `cars`.`rental` (`id`, `customer_id`, `recieve_date`, `return_date`,`vehicle_id`,`class_id`) VALUES ('4','1221','2020-6-18','2020-6-29',4,400);

#sub query statements
SELECT name,job FROM Customer where id=3;

SELECT cost, class_id FROM vehicle where model = 'a-5'; 

SELECT location FROM agency where id = 7;


#update statements
UPDATE Customer
SET name = 'Alfred Schmidt', address= 'Frankfurt'
WHERE id = 3;

UPDATE vehicle
SET vehicle_type = 'renault', cost= 1000
WHERE id = 3;

UPDATE vehicle_details
SET color = 'green', vehicle_year = '2019'
WHERE id = 3;

UPDATE rental
SET vehicle_id = 3, class_id = '400'
WHERE id = 4;

UPDATE agency
SET id = 5, location = 'Mansoura'
WHERE id = 7;


#delete statements
DELETE FROM Customer WHERE name=' mowafeek';

DELETE FROM vehicle where id=3;

DELETE FROM vehicle_details where color='red';

DELETE FROM	agency where location = 'tanta';

DELETE FROM rental where class_id=400;


#joins statements
SELECT agency.location, Customer.address
FROM agency
INNER JOIN Customer ON agency.location = customer.address;

SELECT agency.location, Customer.address
FROM agency
left outer JOIN Customer ON agency.location = customer.address;

SELECT customer.id, vehicle.id
FROM customer
right outer JOIN vehicle ON vehicle.id = customer.id;

SELECT agency.location, Customer.address
FROM agency
cross JOIN Customer ON agency.location = customer.address;

SELECT rental.class_id, vehicle.class_id
FROM vehicle
left JOIN rental ON vehicle.class_id = rental.class_id;


#count and grouping statements
SELECT COUNT(model), cost
FROM vehicle
GROUP BY cost;

SELECT COUNT(id), address
FROM Customer
GROUP BY address;

