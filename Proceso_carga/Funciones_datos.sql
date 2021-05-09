-- Borramos todas las tuplas repetidas de la tabla 
CREATE FUNCTION agrupar_recaudo()
	returns void
	as
	$$
	begin
		-- Primero creamos una vista materializada con los datos agrupados
		create materialized view total_recaudo AS
		(
			select r.idpeaje, r.peaje, r.desde, r.hasta, max(r.tarifafsv) as tarifafsv, sum(r.recaudofsv) as recaudofsv , 
			sum(r.recaudosobrante) as recaudosobrante, sum(r.recaudo) as recaudo
			from recaudo r, recaudo re
			where r.id != re.id
				AND r.idpeaje = re.idpeaje
				AND r.desde = re.desde
				AND r.hasta = re.hasta
			GROUP BY(1,2,3,4)
		);
		-- Y una vista con los datos repetidos
		create materialized view recaudo_repetido AS
		(
			select r.*
			from recaudo r, recaudo re
			where r.id != re.id
				AND r.idpeaje = re.idpeaje
				AND r.desde = re.desde
				AND r.hasta = re.hasta
		);
		--luego borramos los datos repetidos
		DELETE FROM recaudo r
			USING recaudo_repetido rr
			WHERE r.idpeaje = rr.idpeaje
				AND r.desde = rr.desde
				AND r.hasta = rr.hasta
				AND r.tarifafsv = rr.tarifafsv
				AND r.recaudofsv = rr.recaudofsv
				AND r.recaudosobrante = rr.recaudosobrante
				AND r.recaudo = rr.recaudo;
				
		-- insertamos los datos agrupados
		INSERT INTO recaudo(idpeaje, peaje, desde, hasta, tarifafsv, recaudofsv, 
			recaudosobrante, recaudo)
		select * from total_recaudo;
	end
	$$
	language plpgsql;

select * from recaudo;
select agrupar_recaudo();
drop function agrupar_recaudo();
-- Actualizamos los id para que concuerden con los de la tabla peaje
update tarifas set idpeaje = (select id_peaje from peaje where tarifas.peaje = peaje.nombre_peaje);
update recaudo set idpeaje = (select id_peaje from peaje where recaudo.peaje = peaje.nombre_peaje);
update trafico set idpeaje = (select id_peaje from peaje where trafico.peaje = peaje.nombre_peaje);

-- Actualizamos categorías "especiales"
update trafico
set categoriatarifa = categoriatarifa || '*'
where exists (select *
			  from (select t.idpeaje, t.peaje, t.categoriatarifa, t.desde, t.hasta, min(t.valortarifa) as valortarifa
					from trafico t, trafico tr
					where t.idpeaje = tr.idpeaje
					AND t.desde = tr.desde
					AND t.hasta = tr.hasta
					AND t.categoriatarifa = tr.categoriatarifa
					AND (t.valortarifa != tr.valortarifa OR t.cantidadtrafico != tr.cantidadtrafico)
			group by(1,2,3,4,5)
			order by(desde)) as tabla
			where trafico.idpeaje = tabla.idpeaje
			AND trafico.peaje = tabla.peaje
			AND trafico.categoriatarifa = tabla.categoriatarifa
			AND trafico.desde = tabla.desde
			AND trafico.hasta = tabla.hasta
			AND trafico.valortarifa = tabla.valortarifa);

-- Generamos id para las categorías como en la tabla categoria
alter table tarifas add column id_categoria integer;
alter table trafico add column id_categoria integer;
update tarifas set id_categoria = (select idcategoria from categoria where tarifas.idcategoriatarifa = categoria.categoria);
update trafico set id_categoria = (select idcategoria from categoria where trafico.categoriatarifa = categoria.categoria);

-- Borramos las vistas que creamos en la función
drop materialized view total_recaudo;
drop materialized view recaudo_repetido;
