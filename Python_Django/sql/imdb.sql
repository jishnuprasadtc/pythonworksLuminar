create database imdb;
use imdb;
create table language( id int auto_increment primary key,
						name varchar(200) not null unique
					);
				
insert into language (name) values("malayalam"),("tamil"),("kannada"),("english"),("hindi");
select * from language order by id;


create table movies(
					id int auto_increment primary key,
                    name varchar(200) not null unique,
                    year varchar(200) not null,
                    language_id int not null,
                    foreign key(language_id)references language(id) on delete no action 


);
insert into movies (name,year,language_id)values("kgf","2022",1),("rdx","2023",2),("jailer","2023",3),("beast","2022",4);
insert into movies (name,year,language_id)values("2018","2023",1),("vikram","2022",2),("kazhithi","2018",2),("javan","2023",4);
select * from movies;
select language.name,movies.name,movies.year from language,movies where language.id=movies.language_id;
-- print one data only
select language.name,movies.name,movies.year from language,movies where language.id=movies.language;
select name from movies where language_id=1;
select movies.name from movies,language where movies.language_id = language.id and language.name="malayalam";


create table reviews ( 
						id int auto_increment primary key,
                        comment varchar(200) not null,
                        rating int check (rating<6),
                        user varchar(200) not null,
                        movies_id int,
                        foreign key(movies_id)references movies(id) on delete no action					
);
insert into reviews (comment,rating,user,movies_id) values("good",5,"jishnu",1),("good",4,"prasad",1),("average",3,"vishnu",4);
insert into reviews (comment,rating,user,movies_id) values("mustwatch",5,"jishnu prasad",2),("mustwatch",5,"prasad varky",4);
insert into reviews (comment,rating,user,movies_id)values("mustwatch",5,"prasad varky",8);
select * from reviews;
insert into reviews (comment,rating,user,movies_id) values("mustwatch",15,"jishnu prasad",2);

select movies.name,reviews.comment,reviews.rating,reviews.user from movies inner join reviews on movies.id=reviews.movies_id; -- take matching record from both table"inner join"


select movies.name , reviews.comment,reviews.rating,reviews.user from movies left join reviews on movies.id=reviews.movies_id; -- all data from left and matching from right  right join is just opposit
select 
