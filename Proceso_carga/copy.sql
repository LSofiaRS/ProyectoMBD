--copy peaje
copy peaje
from 'C:\Users\ximen\OneDrive\Escritorio\Semestres\Tercer Semestre 2021-1\MBD\PROYECTO\git\ProyectoMBD-master\Tablas_excel\peaje.csv'
with delimiter ';' csv header;

select * from peaje;

--copy categoria
copy categoria_vehicular
from 'C:\Users\ximen\OneDrive\Escritorio\Semestres\Tercer Semestre 2021-1\MBD\PROYECTO\git\ProyectoMBD-master\Tablas_excel\categoria.csv'
with delimiter ';' csv header;

select * from categoria_vehicular;

--copy tarifa
copy tarifa
from 'C:\Users\ximen\OneDrive\Escritorio\Semestres\Tercer Semestre 2021-1\MBD\PROYECTO\git\ProyectoMBD-master\Tablas_excel\tarifa.csv'
with delimiter ';' csv header;

select * from tarifa;

--copy recaudo
copy recaudo
from 'C:\Users\ximen\OneDrive\Escritorio\Semestres\Tercer Semestre 2021-1\MBD\PROYECTO\git\ProyectoMBD-master\Tablas_excel\recaudo.csv'
with delimiter ';' csv header;

select * from recaudo;

--copy trafico
copy trafico
from 'C:\Users\ximen\OneDrive\Escritorio\Semestres\Tercer Semestre 2021-1\MBD\PROYECTO\git\ProyectoMBD-master\Tablas_excel\trafico.csv'
with delimiter ';' csv header;

select * from trafico;