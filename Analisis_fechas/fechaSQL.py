#Analisis por festividades

#-----------------------------------------Semana santa por años

# Semana santa 2014 - categoria mas economica y mas cara
def ss14c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20140201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Semana santa 2015 - categoria mas economica y mas cara
def ss15c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20150201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Semana santa 2016 - categoria mas economica y mas cara
def ss16c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20160201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Semana santa 2017 - categoria mas economica y mas cara
def ss17c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20170201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Semana santa 2018 - categoria mas economica y mas cara
def ss18c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20180201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Semana santa 2019 - categoria mas economica y mas cara
def ss19c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20190201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Semana santa 2020 - categoria mas economica y mas cara
def ss20c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20200201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Semana santa total años
def semanasanta():
    return """select sum(t.cantidad_total_trafico) as trafico, EXTRACT(YEAR FROM fecha_inicio) as año
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje  and t.id_categoria_categoria_vehicular = 1 and fecha_inicio = '20140201' or fecha_inicio = '20150201' or fecha_inicio = '20160201' or fecha_inicio = '20170201' or fecha_inicio = '20180201' or fecha_inicio = '20190201' or fecha_inicio = '20200201'
group by fecha_inicio;
"""

#--------------------------------------------------------#Vacaciones mitad de año por años

# Vacaciones mitad de año 2014 - categoria mas economica y mas cara
def vm14c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20140601' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Vacaciones mitad de año  2015 - categoria mas economica y mas cara
def vm15c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20150601' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Vacaciones mitad de año 2016 - categoria mas economica y mas cara
def vm16c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20160601' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Vacaciones mitad de año  2017 - categoria mas economica y mas cara
def vm17c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20170601' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Vacaciones mitad de año  2018 - categoria mas economica y mas cara
def vm18c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20180601' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Vacaciones mitad de año 2019 - categoria mas economica y mas cara
def vm19c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20190601' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Vacaciones mitad de año 2020 - categoria mas economica y mas cara
def vm20c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20200601' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


#-------------------------------------------------------- Diciembre por años

# Diciembre 2014 - categoria mas economica y mas cara
def dc14c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20141201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Diciembre 2015 - categoria mas economica y mas cara
def dc15c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20151201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Diciembre 2016 - categoria mas economica y mas cara
def dc16c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20161201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Diciembre  2017 - categoria mas economica y mas cara
def dc17c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20171201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Diciembre  2018 - categoria mas economica y mas cara
def dc18c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20181201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# Diciembre 2019 - categoria mas economica y mas cara
def dc19c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20191201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Diciembre 2020- categoria mas economica y mas cara
def dc20c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20201201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""

# ------------------------------------------------------Mes Muerto Febrero por años

# Mes Muerto Febrero  2014 - categoria mas economica y mas cara
def mmf14c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20140201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Mes Muerto Febrero 2015 - categoria mas economica y mas cara
def mmf15c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20150201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Mes Muerto Febrero  2016 - categoria mas economica y mas cara
def mmf16c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20160201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Mes Muerto Febrero  2017 - categoria mas economica y mas cara
def mmf17c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20170201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Mes Muerto Febrero   2018 - categoria mas economica y mas cara
def mmf18c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20180201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Mes Muerto Febrero  2019 - categoria mas economica y mas cara
def mmf19c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20190201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""


# Mes Muerto Febrero  2020- categoria mas economica y mas cara
def mmf20c1():
    return """select t.id_peaje_peaje as id_peaje, t.fecha_inicio ,p.nombre_peaje, t.cantidad_total_trafico, t.id_categoria_categoria_vehicular as id_categoria
from trafico t, peaje p
where t.id_peaje_peaje = p.id_peaje and fecha_inicio = '20200201' and t.id_categoria_categoria_vehicular = 1
order by fecha_inicio;
"""
