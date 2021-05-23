def trafico_total_tarifa_promedio():
    return """select id_peaje_peaje, sum(cantidad_total_trafico) as trafico_total, round(avg(valor_tarifa)) as valor_promedio_tarifa, EXTRACT(YEAR from fecha_inicio) as anio
			from trafico 
			group by id_peaje_peaje, anio
			order by id_peaje_peaje asc, anio desc"""

def trafico_total_particulares():
    return """select nombre_peaje, id_peaje_peaje, sum(cantidad_total_trafico) as trafico_total, round(avg(valor_tarifa)) as valor_promedio_tarifa, EXTRACT(YEAR from fecha_inicio) as anio
		FROM trafico INNER JOIN peaje on trafico.id_peaje_peaje = peaje.id_peaje
		WHERE (id_peaje_peaje = 71 or id_peaje_peaje = 87 or id_peaje_peaje = 9 or id_peaje_peaje = 134 or id_peaje_peaje = 115 or id_peaje_peaje = 56
			or id_peaje_peaje = 110 or id_peaje_peaje = 28 or id_peaje_peaje = 27 or id_peaje_peaje = 81 or id_peaje_peaje = 42 or id_peaje_peaje = 68 )
		GROUP BY nombre_peaje, id_peaje_peaje, anio
		oRDER BY id_peaje_peaje ASC, anio ASC, valor_promedio_tarifa ASC"""
            
