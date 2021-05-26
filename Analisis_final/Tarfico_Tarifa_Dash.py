import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import proyectoSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Casos por pais
con = Connection()
con.openConnection()
queryTraf_Tar = pd.read_sql_query(sql.trafico_total_tarifa_promedio(), con.connection)
query_particulares = pd.read_sql_query(sql.trafico_total_particulares(), con.connection)

con.closeConnection()

#DATAFRAMES
dfTrafTar = pd.DataFrame(queryTraf_Tar, columns=["valor_promedio_tarifa", "trafico_total"])
dfParticulares = pd.DataFrame(query_particulares, columns=["nombre_peaje","valor_promedio_tarifa", "trafico_total", "anio"])



# Grafico barras
figScatter_TarfTar = px.scatter(dfTrafTar, x="valor_promedio_tarifa", y="trafico_total", title = 'Distribución general por año')
figScatter_Particulares = px.scatter(dfParticulares, x="anio", y="trafico_total", size = 'valor_promedio_tarifa', color = 'nombre_peaje' , title = 'Casos Particulares por año')

#

# Layout 
app.layout = html.Div(children=[
    html.H1(children='Dashboard Peajes ANI'),
    #Grid container de ancho completo
    html.Div(className= 'container-fluid', children=[
    	#Row for cases
    	html.Div(className= 'row', children=[
    		#Columna Scatterplot
    		html.Div(className= 'col-12 col-xl-6', children=[
    			html.Div(className='card', children=[
    				html.Div(className='card-header', children=[
    					html.H2(children='Trafico/tarifa'),
    				]),	
    				html.Div(className='card-body', children=[
    					dcc.Graph(
        					id='Distribucion_general por año',
       						figure=figScatter_TarfTar
    					),
    				]),	
    			]),
    		]),
            html.Div(className= 'col-12 col-xl-6', children=[
                html.Div(className='card', children=[
                    html.Div(className='card-header', children=[
                        html.H2(children='Casos Particulares'),
                    ]), 
                    html.Div(className='card-body', children=[
                        dcc.Graph(
                        id= 'Caso_Las_Palmas',
                        figure= figScatter_Particulares
                        ),
                    ]), 
                ]),
            ]),
    	]),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
