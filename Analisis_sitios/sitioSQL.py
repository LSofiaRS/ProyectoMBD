#Analisis trafico por sitios turisticos


def s2014():
    return """select p.nombre_peaje, sum(t.cantidad_total_trafico) as total_trafico
from peaje p, trafico t
where p.id_peaje =t.id_peaje_peaje and EXTRACT(YEAR FROM fecha_inicio)= '2014' and (p.id_peaje=110 or p.id_peaje=9 or p.id_peaje=125 or p.id_peaje=71 or p.id_peaje=130 or p.id_peaje=76 or p.id_peaje=23 or p.id_peaje=54 or p.id_peaje=27 or p.id_peaje=4 or p.id_peaje=87)
group by p.nombre_peaje;
"""

def s2015():
    return """select p.nombre_peaje, sum(t.cantidad_total_trafico) as total_trafico
from peaje p, trafico t
where p.id_peaje =t.id_peaje_peaje and EXTRACT(YEAR FROM fecha_inicio)= '2015' and (p.id_peaje=110 or p.id_peaje=9 or p.id_peaje=125 or p.id_peaje=71 or p.id_peaje=130 or p.id_peaje=76 or p.id_peaje=23 or p.id_peaje=54 or p.id_peaje=27 or p.id_peaje=4 or p.id_peaje=87)
group by p.nombre_peaje;
"""

def s2016():
    return """select p.nombre_peaje, sum(t.cantidad_total_trafico) as total_trafico
from peaje p, trafico t
where p.id_peaje =t.id_peaje_peaje and EXTRACT(YEAR FROM fecha_inicio)= '2016' and (p.id_peaje=110 or p.id_peaje=9 or p.id_peaje=125 or p.id_peaje=71 or p.id_peaje=130 or p.id_peaje=76 or p.id_peaje=23 or p.id_peaje=54 or p.id_peaje=27 or p.id_peaje=4 or p.id_peaje=87)
group by p.nombre_peaje;
"""

def s2017():
    return """select p.nombre_peaje, sum(t.cantidad_total_trafico) as total_trafico
from peaje p, trafico t
where p.id_peaje =t.id_peaje_peaje and EXTRACT(YEAR FROM fecha_inicio)= '2017' and (p.id_peaje=110 or p.id_peaje=9 or p.id_peaje=125 or p.id_peaje=71 or p.id_peaje=130 or p.id_peaje=76 or p.id_peaje=23 or p.id_peaje=54 or p.id_peaje=27 or p.id_peaje=4 or p.id_peaje=87)
group by p.nombre_peaje;
"""

def s2018():
    return """select p.nombre_peaje, sum(t.cantidad_total_trafico) as total_trafico
from peaje p, trafico t
where p.id_peaje =t.id_peaje_peaje and EXTRACT(YEAR FROM fecha_inicio)= '2018' and (p.id_peaje=110 or p.id_peaje=9 or p.id_peaje=125 or p.id_peaje=71 or p.id_peaje=130 or p.id_peaje=76 or p.id_peaje=23 or p.id_peaje=54 or p.id_peaje=27 or p.id_peaje=4 or p.id_peaje=87)
group by p.nombre_peaje;
"""

def s2019():
    return """select p.nombre_peaje, sum(t.cantidad_total_trafico) as total_trafico
from peaje p, trafico t
where p.id_peaje =t.id_peaje_peaje and EXTRACT(YEAR FROM fecha_inicio)= '2019' and (p.id_peaje=110 or p.id_peaje=9 or p.id_peaje=125 or p.id_peaje=71 or p.id_peaje=130 or p.id_peaje=76 or p.id_peaje=23 or p.id_peaje=54 or p.id_peaje=27 or p.id_peaje=4 or p.id_peaje=87)
group by p.nombre_peaje;
"""

def s2020():
    return """select p.nombre_peaje, sum(t.cantidad_total_trafico) as total_trafico
from peaje p, trafico t
where p.id_peaje =t.id_peaje_peaje and EXTRACT(YEAR FROM fecha_inicio)= '2020' and (p.id_peaje=110 or p.id_peaje=9 or p.id_peaje=125 or p.id_peaje=71 or p.id_peaje=130 or p.id_peaje=76 or p.id_peaje=23 or p.id_peaje=54 or p.id_peaje=27 or p.id_peaje=4 or p.id_peaje=87)
group by p.nombre_peaje;
"""

def s2021():
    return """select p.nombre_peaje, sum(t.cantidad_total_trafico) as total_trafico
from peaje p, trafico t
where p.id_peaje =t.id_peaje_peaje and EXTRACT(YEAR FROM fecha_inicio)= '2021' and (p.id_peaje=110 or p.id_peaje=9 or p.id_peaje=125 or p.id_peaje=71 or p.id_peaje=130 or p.id_peaje=76 or p.id_peaje=23 or p.id_peaje=54 or p.id_peaje=27 or p.id_peaje=4 or p.id_peaje=87)
group by p.nombre_peaje;
"""
