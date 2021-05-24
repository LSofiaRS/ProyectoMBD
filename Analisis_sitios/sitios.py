import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from Connection import Connection
import sitioSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# intercalado barras - scartter sitios turisticos 

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.s2014(), con.connection)
con.closeConnection()
s2014dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2014 = px.scatter(s2014dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.s2015(), con.connection)
con.closeConnection()
s2015dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2015 = px.bar(s2015dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.s2016(), con.connection)
con.closeConnection()
s2016dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2016 = px.scatter(s2016dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.s2017(), con.connection)
con.closeConnection()
s2017dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2017 = px.bar(s2017dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.s2018(), con.connection)
con.closeConnection()
s2018dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2018 = px.scatter(s2018dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.s2019(), con.connection)
con.closeConnection()
s2019dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2019 = px.bar(s2019dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.s2020(), con.connection)
con.closeConnection()
s2020dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2020 = px.scatter(s2020dfCases.head(25), x="nombre_peaje", y="total_trafico")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.s2021(), con.connection)
con.closeConnection()
s2021dfCases = pd.DataFrame(query, columns=["nombre_peaje", "total_trafico"])
s2021 = px.bar(s2021dfCases.head(25), x="nombre_peaje", y="total_trafico")

# Layout
app.layout = html.Div(children=[
    html.H1(children='Analisis sitios turisticos'),
    html.H2(children=' 2014 '),
    dcc.Graph(
        id='s2014',
        figure=s2014

    ),
    html.H2(children=' 2015 '),
    dcc.Graph(
        id='s2015',
        figure=s2015

    ),
    html.H2(children=' 2016 '),
    dcc.Graph(
        id='s2016',
        figure=s2016

    ),
    html.H2(children=' 2017 '),
    dcc.Graph(
        id='s2017',
        figure=s2017

    ),
    html.H2(children=' 2018 '),
    dcc.Graph(
        id='s2018',
        figure=s2018

    ),
    html.H2(children=' 2019 '),
    dcc.Graph(
        id='s2019',
        figure=s2019

    ),
    html.H2(children=' 2020 '),
    dcc.Graph(
        id='s2020',
        figure=s2020

    ),
    html.H2(children=' 2021 '),
    dcc.Graph(
        id='s2021',
        figure=s2021

    ),
])
# port=8051
if __name__ == '__main__':
    app.run_server(debug=True)
