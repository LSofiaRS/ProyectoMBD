#**********************************ANÁLISIS DE LOS EVASORES*****************************************************

#Evasores a nivel nacional durante 2014-2021
def EvasoresAnio():
    return """select date_part('year', fecha_inicio) as año, sum(cantidad_evasores) as evasores
                from trafico
                where fecha_inicio != '2020-03-25'
                     AND (id_peaje_peaje != 75 OR id_peaje_peaje != 5)
                group by(1)
                order by(1)"""
                
#Comparación entre tráfico total y evsaores  
def EvasoresCompAnio():
    return """select date_part('year', fecha_inicio) as año, sum(cantidad_evasores) as evasores, sum(cantidad_total_trafico) as trafico
                from trafico
                where fecha_inicio != '2020-03-25'
                    AND (id_peaje_peaje != 75 OR id_peaje_peaje != 5)
                group by(1)
                order by(1)"""

#Evasores por peaje                
def EvasoresPeaje():
    return """select id_peaje_peaje as id, nombre_peaje as nombre, sum(cantidad_evasores) as evasores
                from trafico, peaje
                where fecha_inicio != '2020-03-25'
                     AND (id_peaje_peaje != 75 OR id_peaje_peaje != 5)
                     AND id_peaje_peaje = id_peaje
                  group by(1,2)
                  having sum(cantidad_evasores) > 0
                  order by(sum(cantidad_evasores)) asc"""

#10 Peajes con más evasores               
def EvasoresAnioPeajeL():
    return """select id_peaje_peaje as id, nombre_peaje as nombre, sum(cantidad_evasores) as evasores
                from trafico, peaje
                where fecha_inicio != '2020-03-25'
                     AND (id_peaje_peaje != 75 OR id_peaje_peaje != 5)
                     AND id_peaje_peaje = id_peaje
                group by(1,2)
                order by(evasores) desc
                limit(10);"""

#Evasores por categoría                               
def EvasoresCategoria():
    return """select id_categoria_categoria_vehicular as id_categoria, categoria,
    		sum(cantidad_evasores) as evasores
            from trafico, categoria_vehicular
            where fecha_inicio != '2020-03-25'
                 AND (id_peaje_peaje != 75 OR id_peaje_peaje != 5)
                 AND id_categoria_categoria_vehicular = id_categoria
            group by(1,2)
            order by(1)"""

#Evasores por categoría y por año
def EvasoresCatAnio():
    return """select id_categoria_categoria_vehicular as id_categoria, categoria, date_part('year', fecha_inicio) as año,
    		sum(cantidad_evasores) as evasores
            from trafico, categoria_vehicular
            where fecha_inicio != '2020-03-25'
                 AND (id_peaje_peaje != 75 OR id_peaje_peaje != 5)
                 AND id_categoria_categoria_vehicular = id_categoria
              group by(1,2,3)
              order by(año)"""