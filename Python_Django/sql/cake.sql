create database cakehut;
use cakehut;
create table cake(
		id int auto_increment primary key,
        name varchar(200) not null
);
-- id will auto increment
insert into cake(name) values('white forest'),('blue berry'),('black forest'),('peanut butter');
select * from cake;
delete from cake where id=null;

create table cakevarient(
					id int auto_increment primary key,
                    weight enum("1kg","2kg","3kg","4kg"),
                    price int not null ,
                    flavour varchar(200) not null,
                    shape enum("round","square","heart") default "round",
                    cake_id int,
					foreign key (cake_id) references  cake(id) on delete cascade,  -- cascade for delet the data if 
                    unique(weight,price,flavour,shape)
						
                    
                    );
select * from cakevarient;
insert into cakevarient values (1,'1kg',800,'vanila','round',1);
insert into cakevarient values (3,'1kg',850,'blue berry','square',2);
insert into cakevarient(weight,price,flavour,cake_id)values("2kg",1560,'choloate',3);
insert into cakevarient(weight,price,flavour,cake_id)values("2kg",560,'vanila',1);
-- taking data from table ("tablename.need from table where condition table priamry key = foreign key of next table
select cake.name,cakevarient.weight,cakevarient.price from cake,cakevarient where cake.id=cakevarient.cake_id;
select cake.name from cake;

-- cake avable @1 kg