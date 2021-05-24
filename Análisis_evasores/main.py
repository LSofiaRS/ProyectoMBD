import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from Connection import Connection
import analisis as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash **********************************************************************************************************
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Creación gráficas evasores al año a nivel nacional ***********************************************************
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.EvasoresAnio(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["año", "evasores"]) # Mismos nombres
# Grafico barras exentos
figBarCases = px.bar(dfCases.head(20), x="año", y="evasores", color='evasores',color_continuous_scale='aggrnyl')
#Grafico pie
figBarCasesP = px.pie(dfCases.head(20), values="evasores", names = "año")#, color_discrete_sequence=px.colors.sequential.Turbo)

#Comparación entre trafico y evasores *****************************************************************************
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.EvasoresCompAnio(), con.connection)
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

# Creación gráficas evasores por Peaje ************************************************************************
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.EvasoresPeaje(), con.connection)
con.closeConnection()

dfCases = pd.DataFrame(query, columns=["id", "nombre", "evasores"]) # Mismos nombres
# Grafico barras exentos
figBarPeajeH = px.bar(dfCases.head(139), x="evasores", y="nombre",orientation = 'h', color='evasores',color_continuous_scale='aggrnyl')

# Creación gráficas evasores por Peaje max 10 ************************************************************************
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.EvasoresAnioPeajeL(), con.connection)
con.closeConnection()

dfCases = pd.DataFrame(query, columns=["id", "nombre", "evasores"]) # Mismos nombres
#Grafico pie
figP = px.bar(dfCases.head(27), x="nombre", y="evasores", color='evasores',color_continuous_scale='aggrnyl')

# Creación gráficas evasores por Categoría ************************************************************************
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.EvasoresCategoria(), con.connection)
con.closeConnection()

dfCases = pd.DataFrame(query, columns=["id_categoria", "categoria", "evasores"]) # Mismos nombres
#Grafico pie
figBarCat = px.bar(dfCases.head(27), x="categoria", y="evasores", color='evasores',color_continuous_scale='aggrnyl')

# Creación gráficas evasores por Categoría ************************************************************************
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.EvasoresCatAnio(), con.connection)
con.closeConnection()

dfCases = pd.DataFrame(query, columns=["id_categoria", "categoria", "año", "evasores"]) # Mismos nombres

#Grafico de linea
figLineCatAnio = px.line(dfCases, x="año", y="evasores", color="categoria",
              line_group="categoria", hover_name="categoria")

# Layout, mostramos las gráficas *******************************************************************************

app.layout = html.Div(children=[
    html.H1(children='Análisis Tráfico y Recaudo Vehicular ANI', style={'color': 'black'}, ),
    
    #Grid- container ancho completo
    html.Div(className = "container-fluid", children = [
        #row for cases
        html.Div(className = "row", children = [
            #col for bar graph
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Exentos por Año a nivel nacional grafico de barras', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='barEvasores',
                                figure=figBarCases
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
                        html.H2(children='Exentos por Año a nivel nacional\n grafico de Pie', style={'color': 'blue', 'fontSize': 24}),
                        html.Div(className = "card-body", children = [
                            dcc.Graph(
                                id='PieEvasores',
                                figure=figBarCasesP
                            ),
                        ])
                    ]),
                ]),
            ]),
            html.Div(className = "col-12 col-xl-6", children = [
                #card bar graph
                html.Div(className = "card", children = [
                    html.Div(className = "card-header", children = [
                        html.H2(children='Comparación evasores y trafco total', style={'color': 'blue', 'fontSize': 24}),
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
                        html.H2(children='Comparación evasores y trafco total', style={'color': 'blue', 'fontSize': 24}),
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
                        html.H2(children='Comparación evasores y trafco total', style={'color': 'blue', 'fontSize': 24}),
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


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)