create database NotasFiscais;

use notasfiscais;

create table estabelecimento (
	idEst int unsigned auto_increment,
    nomeEst varchar(255) unique,
    primary key (idEst)
) default charset = utf8mb4;

insert into estabelecimento (nomeEst) values ("Frassul"); 

select * from estabelecimento;

create table produto (
	codProd varchar(255),
    descricao varchar(255),
    precoUn decimal(4,2),
    nomeEst varchar(255),
    primary key (descricao, nomeEst),
    foreign key (nomeEst) references estabelecimento (nomeEst)
) default charset = utf8mb4;

insert into produto values (33, "Batata", "5", "Frassul");

select * from produto;