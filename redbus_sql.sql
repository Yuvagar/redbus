SET AUTOCOMMIT = 0;
SET SAFE_UPDATES = 0;



create table red_bus.detail(
ID  INT AUTO_INCREMENT primary key,
States varchar(50),
Bus_route varchar(150),
Bus_name varchar(150),
Bus_type varchar(150),
Departing_time time,
Duration varchar(150),
Reaching_time time,
star_rating float,
Price float,
Seat_availability varchar (100)

);	

select * from redbus.detail;


select count(id) from redbus.detail;
