create user admin@'localhost' identified by 'admin';
create database blog_db default character set utf8 collate utf8_general_ci;
grant all on blog_db.* to admin@'localhost';