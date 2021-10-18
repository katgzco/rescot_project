
/*CREACIÓN DE LA BASE DE DATOS 'PEDIDOS' */
/********** Befor to run the script create user *************/
/* useradd kat || echo "User already exists." */

/********** How to run *************/
/* sudo -u postgres psql postgres */
/* \i database_settings.sql */
/* exit */

/********** How to test *************/
/* sudo su - kat */
/* psql rescot_test */

DROP ROLE IF EXISTS kat;
CREATE ROLE kat LOGIN PASSWORD '2021';

DROP DATABASE IF EXISTS rescot_test;
CREATE DATABASE rescot_test OWNER kat;
