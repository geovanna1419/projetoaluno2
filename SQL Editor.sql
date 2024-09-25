create database projetoalunos_db;
use projetoalunos_db;


CREATE TABLE tbl_professores
   id_professores int NOT NULL AUTO_INCREMENT,
   prof_nome VARCHAR (45),
   prof_endereço VARCHAR (80)
   prof_email VARCHAR (45)
   prof_telefone DECIMAL (9)
   prof_cpf DECIMAL (11)
   prof_nascimento DATE 
CREATE TABLE tbl_cidades
   id_cidades int NOT NULL AUTO_INCREMENT,
   cid_nome VARCHAR (45)
   cid_uf VARCHAR  (2)
CREATE TABLE tbl_alunos 
   id_alunos int NOT NULL AUTO_INCREMENT,
   alu_nome VARCHAR (45)
   alu_endereço VARCHAR (80)
   alu_email VARCHAR (45)
   alu_telefone DECIMAL (9)
   alu_cpf DECIMAL (11)
   alu_nascimento DATE
CREATE TABLE tbl_cursos 
   id_cursos int NOT NULL AUTO_INCREMENT,
   cur_nome
   cur_valor
CREATE TABLE tbl_usuarios (
  id_usuarios int NOT NULL AUTO_INCREMENT,
  usu_nome varchar(45)
  usu_username VARCHAR(45),
  usu_senha varchar(45)
);