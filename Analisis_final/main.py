import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from Connection import Connection
import fechaSQL as sql1
import sitioSQL as sql2
import proyectoSQL as sql3
import peajesSQL as sql4
import evasoresSQL as sql5

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#*********************************** ANÁLISIS FECHAS ESPECIALES ************************************************
# Grafico barras semana santa por años

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.ss14c1(), con.connection)
con.closeConnection()
ss14dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss14 = px.bar(ss14dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='inferno')


con.openConnection()
query = pd.read_sql_query(sql.ss15c1(), con.connection)
con.closeConnection()
ss15dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss15 = px.scatter(ss15dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='tealrose')

con.openConnection()
query = pd.read_sql_query(sql.ss16c1(), con.connection)
con.closeConnection()
ss16dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss16 = px.bar(ss16dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='rainbow')

con.openConnection()
query = pd.read_sql_query(sql.ss17c1(), con.connection)
con.closeConnection()
ss17dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss17 = px.scatter(ss17dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='electric')

con.openConnection()
query = pd.read_sql_query(sql.ss18c1(), con.connection)
con.closeConnection()
ss18dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss18 = px.bar(ss18dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='turbid')

con.openConnection()
query = pd.read_sql_query(sql.ss19c1(), con.connection)
con.closeConnection()
ss19dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss19 = px.scatter(ss19dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='oranges')

con.openConnection()
query = pd.read_sql_query(sql.ss20c1(), con.connection)
con.closeConnection()
ss20dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss20 = px.bar(ss20dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='agsunset')


# Grafico barras vacaciones mitad de año por años -------------------------------------------------------------

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.vm14c1(), con.connection)
con.closeConnection()
vm14dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm14 = px.bar(vm14dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='inferno')

con.openConnection()
query = pd.read_sql_query(sql.vm15c1(), con.connection)
con.closeConnection()
vm15dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm15 = px.bar(vm15dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='tealrose')

con.openConnection()
query = pd.read_sql_query(sql.vm16c1(), con.connection)
con.closeConnection()
vm16dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm16 = px.bar(vm16dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='rainbow')

con.openConnection()
query = pd.read_sql_query(sql.vm17c1(), con.connection)
con.closeConnection()
vm17dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm17 = px.bar(vm17dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='electric')

con.openConnection()
query = pd.read_sql_query(sql.vm18c1(), con.connection)
con.closeConnection()
vm18dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm18 = px.bar(vm18dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='turbid')

con.openConnection()
query = pd.read_sql_query(sql.vm19c1(), con.connection)
con.closeConnection()
vm19dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm19 = px.bar(vm19dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='oranges')

con.openConnection()
query = pd.read_sql_query(sql.vm20c1(), con.connection)
con.closeConnection()
vm20dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm20 = px.bar(vm20dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='agsunset')


# Grafico barras diciembre por años ----------------------------------------------------------------------------

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.dc14c1(), con.connection)
con.closeConnection()
dc14dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc14 = px.bar(dc14dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='inferno')

con.openConnection()
query = pd.read_sql_query(sql.dc15c1(), con.connection)
con.closeConnection()
dc15dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc15 = px.bar(dc15dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='tealrose')

con.openConnection()
query = pd.read_sql_query(sql.dc16c1(), con.connection)
con.closeConnection()
dc16dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc16 = px.bar(dc16dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='rainbow')

con.openConnection()
query = pd.read_sql_query(sql.dc17c1(), con.connection)
con.closeConnection()
dc17dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc17 = px.bar(dc17dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='electric')

con.openConnection()
query = pd.read_sql_query(sql.dc18c1(), con.connection)
con.closeConnection()
dc18dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc18 = px.bar(dc18dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='turbid')

con.openConnection()
query = pd.read_sql_query(sql.dc19c1(), con.connection)
con.closeConnection()
dc19dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc19 = px.bar(dc19dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='oranges')

con.openConnection()
query = pd.read_sql_query(sql.dc20c1(), con.connection)
con.closeConnection()
dc20dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc20 = px.bar(dc20dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='agsunset')


# Grafico barras mes muerto Febrero por años ----------------------------------------------------------------

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.mmf14c1(), con.connection)
con.closeConnection()
mmf14dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf14 = px.bar(mmf14dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='inferno')

con.openConnection()
query = pd.read_sql_query(sql.mmf15c1(), con.connection)
con.closeConnection()
mmf15dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf15 = px.bar(mmf15dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='tealrose')

con.openConnection()
query = pd.read_sql_query(sql.mmf16c1(), con.connection)
con.closeConnection()
mmf16dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf16 = px.bar(mmf16dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='rainbow')

con.openConnection()
query = pd.read_sql_query(sql.mmf17c1(), con.connection)
con.closeConnection()
mmf17dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf17 = px.bar(mmf17dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='electric')

con.openConnection()
query = pd.read_sql_query(sql.mmf18c1(), con.connection)
con.closeConnection()
mmf18dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf18 = px.bar(mmf18dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='turbid')

con.openConnection()
query = pd.read_sql_query(sql.mmf19c1(), con.connection)
con.closeConnection()
mmf19dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf19 = px.bar(mmf19dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='oranges')

con.openConnection()
query = pd.read_sql_query(sql.mmf20c1(), con.connection)
con.closeConnection()
mmf20dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf20 = px.bar(mmf20dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico",color='cantidad_total_trafico',color_continuous_scale='agsunset')



#*************************************** ANÁLISIS SITIOS TURÍSTICOS ********************************************
# intercalado barras - scartter sitios turisticos 

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql2.s2014(), con.connection)
con.closeConnection()
s2014dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2014 = px.scatter(s2014dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql2.s2015(), con.connection)
con.closeConnection()
s2015dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2015 = px.bar(s2015dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql2.s2016(), con.connection)
con.closeConnection()
s2016dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2016 = px.scatter(s2016dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql2.s2017(), con.connection)
con.closeConnection()
s2017dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2017 = px.bar(s2017dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql2.s2018(), con.connection)
con.closeConnection()
s2018dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2018 = px.scatter(s2018dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql2.s2019(), con.connection)
con.closeConnection()
s2019dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2019 = px.bar(s2019dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql2.s2020(), con.connection)
con.closeConnection()
s2020dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2020 = px.scatter(s2020dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql2.s2021(), con.connection)
con.closeConnection()
s2021dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2021 = px.bar(s2021dfCases.head(25), x="nombre_peaje", y="total_trafico")


#**************************************** ANÁLISIS TRÁFICO-TARIFA **********************************************
# Casos por pais
con = Connection()
con.openConnection()
queryTraf_Tar = pd.read_sql_query(sql3.trafico_total_tarifa_promedio(), con.connection)
query_particulares = pd.read_sql_query(sql3.trafico_total_particulares(), con.connection)
con.closeConnection()

#DATAFRAMES
dfTrafTar = pd.DataFrame(queryTraf_Tar, columns=["valor_promedio_tarifa", "trafico_total"])
dfParticulares = pd.DataFrame(query_particulares, columns=["nombre_peaje","valor_promedio_tarifa", "trafico_total", "anio"])

# Grafico puntos
figScatter_TarfTar = px.scatter(dfTrafTar, x="valor_promedio_tarifa", y="trafico_total", title = 'Distribución general por año')
figScatter_Particulares = px.scatter(dfParticulares, x="anio", y="trafico_total", size = 'valor_promedio_tarifa', color = 'nombre_peaje' , title = 'Casos Particulares por año')


#*************************************** ANÁLISIS COVID-19 *****************************************************

# Trafico por años
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql4.TraficYear(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["trafic", "year"])

# Grafico barras
figBarCases = px.bar(dfCases.head(7), x="year", y="trafic")
# Graifco de pie
figPieCases = px.pie(dfCases.head(7), values="trafic", names="year")

# Trafico 2020-2019 -----------------------------------------------------------------------------------------
con.openConnection()
query = pd.read_sql_query(sql4.Trafico1920(), con.connection)
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

#Recaudo por años --------------------------------------------------------------------------------------------
con.openConnection()
query = pd.read_sql_query(sql4.CollectionYear(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["year", "recaudo"])

#linechart
figlineCases = px.line(query, x = "year", y = "recaudo")

#pie recaudo
figPieRCases = px.pie(dfCases.head(6), values="recaudo", names ="year")

#Tarifa comparacion ------------------------------------------------------------------------------------------
con.openConnection()
query = pd.read_sql_query(sql4.Tarifa192021(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["name", "valor_tarifa","month"])

#linchart tarifa
figlinetarifa = px.line(query,x = "month", y = "valor_tarifa", color = "name")

#puntos tarifa
figDottCases = px.scatter(query, x="month", color = "name", y="valor_tarifa",size='month')


#*************************************** ANÁLISIS EVASORES *****************************************************

# Creación gráficas evasores al año a nivel nacional ----------------------------------------------------------
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql5.EvasoresAnio(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["año", "evasores"]) # Mismos nombres
# Grafico barras exentos
figBarCasesE = px.bar(dfCases.head(20), x="año", y="evasores", color='evasores',color_continuous_scale='aggrnyl')
#Grafico pie
figPieCasesE = px.pie(dfCases.head(20), values="evasores", names = "año")#, color_discrete_sequence=px.colors.sequential.Turbo)

#Comparación entre trafico y evasores ------------------------------------------------------------------------
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql5.EvasoresCompAnio(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["año", "evasores", "trafico"]) # Mismos nombres

#Grafica de barras 
figBar = go.Figure()
figBar.add_trace(go.Bar(
    x=dfCases["año"],
    y=dfCases["evasores"],
    name='Evasores',
    marker_color='royalblue'
))
figBar.add_trace(go.Bar(
    x=dfCases["año"],
    y=dfCases["trafico"],
    name='Trafico',
    marker_color='darkblue'
))

#Gráfico de linea
figLine = go.Figure()
# Create and style traces
figLine.add_trace(go.Scatter(x = dfCases["año"], y=dfCases["evasores"], name='evasores',
                         line=dict(color='cyan', width=4)))
figLine.add_trace(go.Scatter(x=dfCases["año"], y=dfCases["trafico"], name='Trafico',
                         line=dict(color='royalblue', width=4) 
))

#Grafico de sunburst
figSB =px.sunburst(
    dfCases, names='evasores',
    path=['evasores', 'trafico'], values='trafico', color='año', color_continuous_scale='Turbo'
)

# Creación gráficas evasores por Peaje -----------------------------------------------------------------------
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql5.EvasoresPeaje(), con.connection)
con.closeConnection()

dfCases = pd.DataFrame(query, columns=["id", "nombre", "evasores"]) # Mismos nombres
# Grafico barras exentos
figBarPeajeH = px.bar(dfCases.head(139), x="evasores", y="nombre",orientation = 'h', color='evasores',color_continuous_scale='aggrnyl')

# Creación gráficas evasores por Peaje max 10 -----------------------------------------------------------------
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql5.EvasoresAnioPeajeL(), con.connection)
con.closeConnection()

dfCases = pd.DataFrame(query, columns=["id", "nombre", "evasores"]) # Mismos nombres
#Grafico pie
figP = px.bar(dfCases.head(27), x="nombre", y="evasores", color='evasores',color_continuous_scale='aggrnyl')

# Creación gráficas evasores por Categoría -----------------------------------------------------------------
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql5.EvasoresCategoria(), con.connection)
con.closeConnection()

dfCases = pd.DataFrame(query, columns=["id_categoria", "categoria", "evasores"]) # Mismos nombres
#Grafico pie
figBarCat = px.bar(dfCases.head(27), x="categoria", y="evasores", color='evasores',color_continuous_scale='aggrnyl')

# Creación gráficas evasores por Categoría -----------------------------------------------------------------
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql5.EvasoresCatAnio(), con.connection)
con.closeConnection()

dfCases = pd.DataFrame(query, columns=["id_categoria", "categoria", "año", "evasores"]) # Mismos nombres

#Grafico de linea
figLineCatAnio = px.line(dfCases, x="año", y="evasores", color="categoria",
              line_group="categoria", hover_name="categoria")


# ******************************* LAYOUT: MOSTRAMOS LAS GRÁFICAS ***********************************************

app.layout = html.Div(children=[
    html.H1(children='Análisis Fechas especiales y sitios turísticos', style={'color': 'black'}, ),
    
    #Grid- container ancho completo
    html.Div(className = "container-fluid", children = [
        #row for cases
        html.Div(className = "row", children = [
            #col for bar graph
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Semana Santa del 2014', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N1',
                                figure=ss14
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Semana Santa del 2015', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N2',
                                figure=ss15
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Semana Santa del 2016', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N3',
                                figure=ss16
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Semana Santa del 2017', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N4',
                                figure=ss17
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Semana Santa del 2018', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N5',
                                figure=ss18
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Semana Santa del 2019', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N6',
                                figure=ss19
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Semana Santa del 2020', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N7',
                                figure=ss20
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Vacaciones mitad de año 2014', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N8',
                                figure=vm14
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Vacaciones mitad de año 2015', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N9',
                                figure=vm15
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Vacaciones mitad de año 2016', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N10',
                                figure=vm16
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Vacaciones mitad de año 2017', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N11',
                                figure=vm17
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Vacaciones mitad de año 2018', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N12',
                                figure=vm18
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Vacaciones mitad de año 2019', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N13',
                                figure=vm19
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Vacaciones mitad de año 2020', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N14',
                                figure=vm20
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Diciembre de 2014', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N15',
                                figure=dc14
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Diciembre de 2015', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N16',
                                figure=dc15
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Diciembre de 2016', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N17',
                                figure=dc16
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Diciembre de 2017', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N18',
                                figure=dc17
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Diciembre de 2018', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N19',
                                figure=dc18
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Diciembre de 2019', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N20',
                                figure=dc19
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Diciembre de 2020', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N21',
                                figure=dc20
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Mes muerto Febrero 2014', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N22',
                                figure=mmf14
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Mes muerto Febrero 2015', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N23',
                                figure=mmf15
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Mes muerto Febrero 2016', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N24',
                                figure=mmf16
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Mes muerto Febrero 2017', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N25',
                                figure=mmf17
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Mes muerto Febrero 2018', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N26',
                                figure=mmf18
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Mes muerto Febrero 2019', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N27',
                                figure=mmf19
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Mes muerto Febrero 2020', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N28',
                                figure=mmf20
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Sitios turísticos 2014', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N29',
                                figure=s2014
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Sitios turísticos 2015', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N30',
                                figure=s2015
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Sitios turísticos 2016', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N31',
                                figure=s2016
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Sitios turísticos 2017', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N32',
                                figure=s2017
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Sitios turísticos 2018', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N33',
                                figure=s2018
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Sitios turísticos 2019', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N34',
                                figure=s2019
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Sitios turísticos 2020', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N35',
                                figure=s2020
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Sitios turísticos 2021', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='N36',
                                figure=s2021
                                ),
                        ])
                    ]),
                ]),
            ]),
    html.H1(children='Análisis Tráfico y Tarifas', style={'color': 'black'}, ),
    
    #Grid- container ancho completo
    html.Div(className = "container-fluid", children = [
        #row for cases
        html.Div(className = "row", children = [
            #col for bar graph
            html.Div(className = "col-12 col-xl-12", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Tráfico-Tarifa', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='F1',
                                figure=figScatter_TarfTar
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-12", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Casos Particulares', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='F2',
                                figure=figScatter_Particulares
                                ),
                        ])
                    ]),
                ]),
            ]),
        ]),
    ]),
    html.H1(children='Análisis Tráfico-Tarifa y Covid-19', style={'color': 'black'}, ),
    
    #Grid- container ancho completo
    html.Div(className = "container-fluid", children = [
        #row for cases
        html.Div(className = "row", children = [
            #col for bar graph
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Tráfico por años barras', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='X1',
                                figure=figBarCases
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Tráfico por años Pie', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='X2',
                                figure=figPieCases
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Comparación 2019-2020 Histograma', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='X3',
                                figure=figHisCases
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Comparacion 2019-2020  Barras', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='X4',
                                figure=figDotCases
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Tarifa por meses 2020 Lineas', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='X5',
                                figure=figBarCasesH
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Recaudo por Años Lineas', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='X7',
                                figure=figPieRCases
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Recaudo por Años Pie ', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='X8',
                                figure=figlinetarifa
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Tarifa por meses 2020 Puntos', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='X9',
                                figure=figDottCases
                                ),
                        ])
                    ]),
                ]),
            ]),
        ]),
    ]),
    html.H1(children='Análisis comportamiento de los evasores', style={'color': 'black'}, ),
    
    #Grid- container ancho completo
    html.Div(className = "container-fluid", children = [
        #row for cases
        html.Div(className = "row", children = [
            #col for bar graph
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Evasores por Año a nivel nacional grafico de barras', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='barEvasores',
                                figure=figBarCasesE
                                ),
                        ])
                    ]),
                ]),
            ]),
             #col for pie graph
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Evasores por Año a nivel nacional\n grafico de Pie', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='PieEvasores',
                                figure=figPieCasesE
                            ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Comparación evasores y tráfico total', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='barEvasoresComp',
                                figure=figBar
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Comparación evasores y tráfico total', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='LineEvasoresComp',
                                figure=figLine
                                ),
                        ])
                    ]),
                ]),
            ]),  
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Comparación evasores y tráfico total', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='SBEvasoresComp',
                                figure=figSB
                                ),
                        ])
                    ]),
                ]),
            ]), 
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Evasores por Peaje', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='PeajeEvasoresBar',
                                figure=figBarPeajeH
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='10 Peajes con mas evasores', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='PeajeEvasoresPie',
                                figure=figP
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Evasores por categoría', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='CategoriaBar',
                                figure=figBarCat
                                ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Evasores por categoría por año', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='CategoriaLineAnio',
                                figure=figLineCatAnio
                                ),
                        ])
                    ]),
                ]),
            ]),
        ]),
    ]),
])
])
])


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
