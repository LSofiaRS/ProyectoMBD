# -*- coding: utf-8 -*-
"""
Created on Tue May 18 08:10:12 2021

@author: ximen
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from connection import Connection
import peajesSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Trafico por años
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.TraficYear(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["trafic", "year"])

# Grafico barras
figBarCases = px.bar(dfCases.head(7), x="year", y="trafic")
# Graifco de pie
figPieCases = px.pie(dfCases.head(7), values="trafic", names="year")

# Trafico 2020-2019
con.openConnection()
query = pd.read_sql_query(sql.Trafico1920(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["trafic", "month", "year"])

#histograma de comparacion
figHisCases = px.histogram(query, x = "month", color = "year",y = "trafic")
figHisCases.update_traces(opacity=0.75,xbins = dict(start = 1, end = 13, size = 1))

#grafico de puntos
figDotCases = px.scatter(query, x="month", color = "year", y="trafic",size='month')
figDotCases.update_traces(opacity=0.75)

#Grafico de barras horizontales
figBarCasesH = px.bar(dfCases.head(24), y="month",color ="year", height=400,
                     x="trafic", orientation  = 'h')

#Recaudo por años
con.openConnection()
query = pd.read_sql_query(sql.CollectionYear(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["year", "recaudo"])

#linechart
figlineCases = px.line(query, x = "year", y = "recaudo")

#pie recaudo
figPieRCases = px.pie(dfCases.head(6), values="recaudo", names ="year")

#Tarifa comparacion 
con.openConnection()
query = pd.read_sql_query(sql.Tarifa192021(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["name", "valor_tarifa","month"])

#linchart tarifa
figlinetarifa = px.line(query,x = "month", y = "valor_tarifa", color = "name")

#puntos tarifa
figDottCases = px.scatter(query, x="month", color = "name", y="valor_tarifa",size='month')



#layaout

app.layout = html.Div(children=[
    html.H1(children='Impacto Covid 19 '),
    
    # Grid-Container ancho completo
    html.Div(className="container-fluid", children=[
        # Row for cases
         html.Div(className="row", children=[
             #Col for bar graph
             html.Div(className="col-12 col-xl-7", children=[
                 # Card bar graph
                   html.Div(className="card", children=[
                       html.Div(className="card-header", children=[
                           html.H2(children='Trafico por Años Barras'),
                       ]),
                   html.Div(className="card-body", children=[
                            dcc.Graph(
                                id='TraficByYear',
                                figure=figBarCases
                                ),
                       ]),
                   ]),
             ]),
             html.Div(className="col-12 col-md-5", children=[
                 # Card bar graph
                   html.Div(className="card", children=[
                       html.Div(className="card-header", children=[
                           html.H2(children='Trafico por Años Pie'),
                       ]),
                   html.Div(className="card-body", children=[
                                dcc.Graph(
                                    id='barHCasesByCountry',
                                    figure=figPieCases
                                    ),
                       ]),
                   ]),
             ]),
                     ]),
              html.Div(className="row", children=[
             #Col for pie graph
             html.Div(className="col-32 col-xs-5", children=[
                 # Card bar graph
                   html.Div(className="card", children=[
                       html.Div(className="card-header", children=[
                           html.H2(children='Comparacion 2019-2020 Histograma'),
                       ]),
                   html.Div(className="card-body", children=[
                               
                           dcc.Graph(
                               id='Trafic1920',
                               figure=figHisCases
                
                               ), 
                       ]),
                   ]),
             ]),
                html.Div(className="col-32 col-xs-5", children=[
                 # Card bar graph
                   html.Div(className="card", children=[
                       html.Div(className="card-header", children=[
                           html.H2(children='Comparacion 2019-2020  Barras'),
                       ]),
                   html.Div(className="card-body", children=[
                               
                           dcc.Graph(
                               id='Trafic1920bar',
                               figure=figBarCasesH
                
                               ), 
                       ]),
                   ]),
             ]),
        ]),

        html.Div(className="row", children=[
              #Col for pie graph
              html.Div(className="col-32 col-xs-5", children=[
                  # Card bar graph
                    html.Div(className="card", children=[
                        html.Div(className="card-header", children=[
                            html.H2(children='Tarifa por meses 2020 Lineas'),
                        ]),
                    html.Div(className="card-body", children=[
                               
                            dcc.Graph(
                                id='Tarifabyyear',
                                figure=figlinetarifa
                
                                ), 
                        ]),
                    ]),
              ]),
              #Col for pie graph
              html.Div(className="col-32 col-xs-5", children=[
                  # Card bar graph
                    html.Div(className="card", children=[
                        html.Div(className="card-header", children=[
                            html.H2(children='Tarifa por meses 2020 Puntos'),
                        ]),
                    html.Div(className="card-body", children=[
                               
                            dcc.Graph(
                                id='Tarifabyyeardot',
                                figure=figDottCases
                
                                ), 
                        ]),
                    ]),
              ]),
              ]),
              html.Div(className="row", children=[
                  html.Div(className="col-12 col-xl-7", children=[
                  # Card bar graph
                    html.Div(className="card", children=[
                        html.Div(className="card-header", children=[
                            html.H2(children='Recaudo por Años Lineas'),
                        ]),
                    html.Div(className="card-body", children=[
                               
                            dcc.Graph(
                                id='Collectionbyyear',
                                figure=figlineCases 
                
                                ), 
                        ]),
                    ]),
              ]),
            html.Div(className="col-12 col-xl-5", children=[
                  # Card bar graph
                    html.Div(className="card", children=[
                        html.Div(className="card-header", children=[
                            html.H2(children='Recaudo por Años Pie '),
                        ]),
                    html.Div(className="card-body", children=[
                               
                            dcc.Graph(
                                id='PieRbyyear',
                                figure=figPieRCases
                
                                ), 
                        ]),
                    ]),
              ]),
              
        ]),
        
    ]),

])



if __name__ == '__main__':
    app.run_server(debug=True)






