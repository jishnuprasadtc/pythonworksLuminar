create database vegstore;
use vegstore;
create table items (id int auto_increment primary key,
					name varchar(200)
);

insert into items (name) values("potato"),("onion"),("drumstick"),("tomatto");
select * from items;

create table stock (id int auto_increment primary key,
					quantity varchar(200) not null,
                    price int not null,
                    selling int not null,
                    item_id int,
                    foreign key (item_id) references items(id) on delete cascade);
select * from stock;

insert into stock(quantity,price,selling,item_id) values(10,30,45,1);
insert into stock(quantity,price,selling,item_id) values(50,25,40,3);
insert into stock(quantity,price,selling,item_id) values(40,20,35,2);
insert into stock(quantity,price,selling,item_id) values(10,80,105,4);


create table bill ( id int auto_increment primary key,
user varchar(200) not null,
phone varchar(200),
date varchar(200)
);
insert into bill(user,phone,date)values("jishnu","9874563210","08/09/2023"),("prasad","9865871210","09/09/2023"),("amal","9879535410","10/09/2023");
select * from bill;


create table billitems( id int auto_increment primary key,
bill_id int,
foreign key(bill_id) references bill(id) on delete no action,
item_id int,
foreign key(item_id) references items(id) on delete no action,
quantiy int
);

insert into billitems(bill_id,item_id,quantiy)values(2,2,2),(2,1,1),(1,4,2),(1,3,1);
select * from billitems;