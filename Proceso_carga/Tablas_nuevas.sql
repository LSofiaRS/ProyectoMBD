create table categoria 
(
	idCategoria serial,
	Categoria char(7),
);

drop table categoria;

insert into categoria(Categoria)
select categoria 
from(
select t.idcategoriatarifa as categoria
from tarifas t
UNION
select tr.categoriatarifa as categoria
from trafico tr) as ct
order by categoria;

select * from categoria;

insert into categoria(Categoria)
select categoria || '*'
from(
select t.idcategoriatarifa as categoria
from tarifas t
UNION
select tr.categoriatarifa as categoria
from trafico tr) as ct
order by categoria;

--**************************************************************************************************************************************
create table peaje
(
	id_peaje serial,
	nombre_peaje varchar(30)
);

insert into peaje(nombre_peaje)
select t.peaje from trafico t
UNION
select ta.peaje from tarifas ta
UNION
select r.peaje from recaudo r;

select * from peaje;
