## Preparation for unit testing 

### Prepare two PostgreSQL servers
1. Install PostgreSQl server on local machine with port `5432`, start server
2. Run another PostgreSQl server in docker container, expose port `5433`
```shell
$ docker run \
-d \
-p 5433:5432 \
-e POSTGRES_PASSWORD=password \
-e POSTGRES_HOST_AUTH_METHOD=trust \
--name db postgres:13-alpine
```
### On Local Postgre server
1. create two databases: `test`, `test2` for running unit tests `test_db.py`
```sql
create database test;
create database test2;
```
2. create table
```sql
create table student
(
    id     integer      not null
        constraint student_pkey
            primary key,
    name   varchar(255) not null,
    status integer default 0
);
```
3. insert 1 record into test
```sql
insert into student(id, name, status) values(000, 'John Snow', 2);
```
4. insert 2 records into test2
```sql
insert into student(id, name, status) values(000, 'John Snow', 2);
insert into student(id, name, status) values(001, 'Snow White', 2);
```
### On Postgre server in docker container
1. create database: `test`
```sql
create database test;
```
2. create table
```sql
create table student
(
    id     integer      not null
        constraint student_pkey
            primary key,
    name   varchar(255) not null,
    status integer default 0
);
```
3. insert 3 records into test
```sql
insert into student(id, name, status) values(000, 'John Snow', 2);
insert into student(id, name, status) values(001, 'Snow White', 2);
insert into student(id, name, status) values(002, 'White Walker', 2);
```
### Run all unit test cases
```shell
$ python3 -m unittest discover
```