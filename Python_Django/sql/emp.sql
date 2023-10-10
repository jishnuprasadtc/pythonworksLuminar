use employe;
create database emp;
use emp;
drop table emp;
create table emp(id int unique,
				emp_name varchar(200),
                dept varchar(200),
                salary int);
                
                
insert into emp values (101,'jishnu','it',50000);
insert into emp values (102,'sanjay','acc',45000);
insert into emp values (103,'akhilsh','hr',53000);
insert into emp values (104,'sidhu','tec',55000);

select * from emp;


select * from emp where salary>50000;

select count(*) from emp;

select emp_name from emp where dept!="hr";

select sum(salary) from emp;

select max(salary)from emp;

select * from emp;
select * from emp where salary=(select max(salary ) from emp);
select* from emp where salary=(select max(salary)from emp where salary!=(select max(salary) from emp));
select dept ,count(*) from emp group by (dept);
update  emp set salary=65000 where id =101;
update emp set emp_name="raju" where id=2;



