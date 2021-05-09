create table Tarifas
(
	idPeaje integer,
	Peaje varchar(20),
	UltimoFechaCambioPeaje date,
	IdCategoriaTarifa char(7),
	Valor integer
);

COPY tarifas FROM 'C:\Workspace\Tarifas.csv' with delimiter ';' csv header;
select * from tarifas;

--**************************************************************************************************************************************

create table Trafico
(
	idPeaje integer,
	Peaje varchar(20),
	CategoriaTarifa char(7),
	Desde date,
	Hasta date,
	ValorTarifa integer,
	CantidadTrafico integer,
	CantidadEvasores integer,
	CantidadExentos787 integer
);

COPY trafico FROM 'C:\Workspace\Trafico.csv' with delimiter ';' csv header;
select * from trafico;
drop table trafico cascade;

--*************************************************************************************************************************************
drop table Recaudo cascade;
create table Recaudo
(
	id serial,
	idPeaje integer,
	Peaje varchar(20),
	Desde date,
	Hasta date,
	TarifaFsv integer,
	RecaudoFsv integer,
	RecaudoSobrante integer,
	Recaudo numeric
);
	
COPY recaudo (idpeaje, peaje, desde, hasta, tarifafsv, recaudofsv, recaudosobrante, recaudo) FROM 'C:\Workspace\Recaudo_original.csv' with delimiter ';' csv header;
select * from recaudo;