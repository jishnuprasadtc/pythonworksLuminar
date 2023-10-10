show databases;
create database hotel;
create database cakebox;

-- use database
use hotel;
-- create table
create table items (
					id int unique,
					name varchar(100)not null,
                    category varchar(120) not null,
                    price int not null,
                    type varchar(120) not null);
                    
                    
-- list tables


show tables;


-- insertion
insert into items(id,name,category,price,type)values(1,'vegbiriyani','veg',80,'chines');
insert into items(id,name,category,price,type)values(2,'chickenbiriyani','na_veg',80,'indian');
insert into items(id,name,category,price,type)values(3,'octopusfry','na_veg',80,'japnes');
insert into items(id,name,category,price,type)values(4,'alfham','na_veg',90,'arabic');
insert into items(id,name,category,price,type)values(5,'noodles','na_veg',180,'chines');
insert into items(id,name,category,price,type)values(6,'matthifry','na_veg',280,'thai');
-- fetch all record

select * from items;
select name,price from items;

-- select items available under 160

select * from items where price<160;



select * from items where price>80 and price<280;
-- heke


select count(*) from items;


select count(*) from items;


select name from items where type !="chines";

select max(price) from items;

select sum(price) from items;
select max(price) from items;
select * from items where price=(select max(price)from items);
select * from items where price=(select min(price) from items);
select * from items where price=(select max(price) from items where category="na_veg");
select* from items where price=(select max(price)from items where price!=(select max(price) from items));
select category,count(*) from items group by(category);
select type,count(*)from items group by(type);

-- make order
select * from items order by price asc limit 2;

select *from items where name=" octopusfry";

select * from items;
update items set price=180 where id=2;

update items set category="veg" where id =5;


update items  set price=210 where id=3;
update items  set price=110 where id=4;
-- modify

alter table items add column courses enum ("main course","dessert","staret") default "main course";

update items set  courses="starter" where id =3;
