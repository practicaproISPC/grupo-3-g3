--crear base de datos
create database BochasSportClub
use BochasSportClub

--crear tablas
create table Actividades(
	id int primary key identity (1,1) not null,
	Nombre varchar(50) not null,
);
create table Socios(
	id int primary key identity (1,1) not null,
	Nombre varchar(50) not null,
	Apellido varchar(50) not null,
	id_Actividad int not null,
	constraint fk_Socios foreign key (id_Actividad) references Actividades (id) 
);


--procedimientos carga de datos 
create procedure CargarActividad
	@Nombre varchar(50)
as
	insert into Actividades values (@Nombre)
go

create procedure CargarSocio
	@Nombre varchar(50),
	@Apellido varchar(50),
	@id_Actividad int
as
	insert into Socios values (@Nombre, @Apellido, @id_Actividad)
go

