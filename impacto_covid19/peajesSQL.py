
def TraficYear():
    return """select extract(year from fecha_inicio) as year,
              sum(cantidad_total_trafico) as trafic
              from trafico group by(year) order by (year)"""

def Trafico1920():
    return """select extract(month from fecha_inicio) as month,
            sum(cantidad_total_trafico) as trafic,
            extract(year from fecha_inicio)::int as year
            from trafico
            where (extract(year from fecha_inicio)::int = 2020
            or extract(year from fecha_inicio)::int = 2019)
            group by (month,year)
            order by month"""
            
def CollectionYear():
    return """select extract(year from fecha_inicio) as year, 
            sum(recaudo_total) as recaudo
            from recaudo
            where extract(year from fecha_inicio)!=2021 and
            extract(year from fecha_inicio)!=2014
            group by(year) order by(year)"""
            
def Tarifa192021():
    return """select nombre_peaje as name,extract(month from fecha_inicio) as month
            ,valor_tarifa from trafico inner join
			peaje on trafico.id_peaje_peaje = peaje.id_peaje where 
             (extract(year from fecha_inicio) =2020) and 
            (id_categoria_categoria_vehicular = 6) and
        	(id_peaje_peaje = 115  or
        	 id_peaje_peaje=9 or  id_peaje_peaje=134
             or id_peaje_peaje = 87 or
              id_peaje_peaje = 71) order by (month)"""