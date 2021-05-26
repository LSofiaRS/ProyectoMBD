import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from Connection import Connection
import fechaSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Grafico barras semana santa por años

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.ss14c1(), con.connection)
con.closeConnection()
ss14dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss14 = px.scatter(ss14dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.ss15c1(), con.connection)
con.closeConnection()
ss15dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss15 = px.bar(ss15dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.ss16c1(), con.connection)
con.closeConnection()
ss16dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss16 = px.scatter(ss16dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.ss17c1(), con.connection)
con.closeConnection()
ss17dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss17 = px.bar(ss17dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.ss18c1(), con.connection)
con.closeConnection()
ss18dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss18 = px.scatter(ss18dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.ss19c1(), con.connection)
con.closeConnection()
ss19dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss19 = px.bar(ss19dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.ss20c1(), con.connection)
con.closeConnection()
ss20dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
ss20 = px.scatter(ss20dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

#con.openConnection()
#query = pd.read_sql_query(sql.semanasanta(), con.connection)
#con.closeConnection()
#ssdfCases = pd.DataFrame(query, columns=["trafico","fecha"])
#ss = px.bar(ssdfCases.head(25), x="fecha", y="trafico")
# Grafico barras vacaciones mitad de año por años

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.vm14c1(), con.connection)
con.closeConnection()
vm14dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm14 = px.bar(vm14dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.vm15c1(), con.connection)
con.closeConnection()
vm15dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm15 = px.bar(vm15dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.vm16c1(), con.connection)
con.closeConnection()
vm16dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm16 = px.bar(vm16dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.vm17c1(), con.connection)
con.closeConnection()
vm17dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm17 = px.bar(vm17dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.vm18c1(), con.connection)
con.closeConnection()
vm18dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm18 = px.bar(vm18dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.vm19c1(), con.connection)
con.closeConnection()
vm19dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm19 = px.bar(vm19dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.vm20c1(), con.connection)
con.closeConnection()
vm20dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
vm20 = px.bar(vm20dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

# Grafico barras diciembre por años

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.dc14c1(), con.connection)
con.closeConnection()
dc14dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc14 = px.bar(dc14dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.dc15c1(), con.connection)
con.closeConnection()
dc15dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc15 = px.bar(dc15dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.dc16c1(), con.connection)
con.closeConnection()
dc16dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc16 = px.bar(dc16dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.dc17c1(), con.connection)
con.closeConnection()
dc17dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc17 = px.bar(dc17dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.dc18c1(), con.connection)
con.closeConnection()
dc18dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc18 = px.bar(dc18dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.dc19c1(), con.connection)
con.closeConnection()
dc19dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc19 = px.bar(dc19dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.dc20c1(), con.connection)
con.closeConnection()
dc20dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
dc20 = px.bar(dc20dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

# Grafico barras mes muerto Febrero por años

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.mmf14c1(), con.connection)
con.closeConnection()
mmf14dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf14 = px.bar(mmf14dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.mmf15c1(), con.connection)
con.closeConnection()
mmf15dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf15 = px.bar(mmf15dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.mmf16c1(), con.connection)
con.closeConnection()
mmf16dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf16 = px.bar(mmf16dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.mmf17c1(), con.connection)
con.closeConnection()
mmf17dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf17 = px.bar(mmf17dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.mmf18c1(), con.connection)
con.closeConnection()
mmf18dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf18 = px.bar(mmf18dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.mmf19c1(), con.connection)
con.closeConnection()
mmf19dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf19 = px.bar(mmf19dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

con.openConnection()
query = pd.read_sql_query(sql.mmf20c1(), con.connection)
con.closeConnection()
mmf20dfCases = pd.DataFrame(query, columns=["id_peaje", "fecha_inicio", "nombre_peaje", "cantidad_total_trafico"])
mmf20 = px.bar(mmf20dfCases.head(25), x="nombre_peaje", y="cantidad_total_trafico")

#semanasanta = go.Figure(data=[go.Scatter(x=[ss16,ss17,ss18,ss19,ss20],y=[ss16,ss17,ss18,ss19,ss20])])

# Layout
app.layout = html.Div(children=[
    html.H1(children='Analisis festividades'),
    html.H2(children=' Semana santa 2014'),
    dcc.Graph(
        id='ss14',
        figure=ss14

    ),
    html.H2(children=' Semana santa 2015'),
        dcc.Graph(
            id='ss15',
            figure=ss15

        ),
    html.H2(children=' Semana santa 2016'),
        dcc.Graph(
            id='ss16',
            figure=ss16

        ),
    html.H2(children=' Semana santa 2017'),
        dcc.Graph(
            id='ss17',
            figure=ss17

        ),
    html.H2(children=' Semana santa 2018'),
        dcc.Graph(
            id='ss18',
            figure=ss18

        ),
    html.H2(children=' Semana santa 2019'),
        dcc.Graph(
            id='ss19',
            figure=ss19

        ),
    html.H2(children=' Semana santa 2020'),
        dcc.Graph(
            id='ss20',
            figure=ss20

        ),

#    html.H2(children=' Semana santa años'),
#        dcc.Graph(
#            id='ss',
#            figure=ss

        #),
    html.H2(children=' Vacaciones mitad de año 2014 '),
    dcc.Graph(
        id='vm14',
        figure=vm14

    ),
    html.H2(children=' Vacaciones mitad de año 2015'),
        dcc.Graph(
            id='vm15',
            figure=vm15

        ),
    html.H2(children=' Vacaciones mitad de año 2016'),
        dcc.Graph(
            id='vm16',
            figure=vm16

        ),
    html.H2(children=' Vacaciones mitad de año 2017'),
        dcc.Graph(
            id='vm17',
            figure=vm17

        ),
    html.H2(children=' Vacaciones mitad de año 2018'),
        dcc.Graph(
            id='vm18',
            figure=vm18

        ),
    html.H2(children=' Vacaciones mitad de año 2019'),
        dcc.Graph(
            id='vm19',
            figure=vm19

        ),
    html.H2(children=' Vacaciones mitad de año 2020'),
        dcc.Graph(
            id='vm20',
            figure=vm20

        ),

    html.H2(children=' Diciembre 2014 '),
    dcc.Graph(
        id='dc14',
        figure=dc14

    ),
    html.H2(children=' Diciembre 2015'),
        dcc.Graph(
            id='dc15',
            figure=dc15

        ),
    html.H2(children=' Diciembre 2016'),
        dcc.Graph(
            id='dc16',
            figure=dc16

        ),
    html.H2(children=' Diciembre 2017'),
        dcc.Graph(
            id='dc17',
            figure=dc17

        ),
    html.H2(children=' Diciembre 2018'),
        dcc.Graph(
            id='dc18',
            figure=dc18

        ),
    html.H2(children=' Diciembre 2019'),
        dcc.Graph(
            id='dc19',
            figure=dc19

        ),
    html.H2(children=' Diciembre 2020'),
        dcc.Graph(
            id='dc20',
            figure=dc20

        ),

    html.H2(children=' Mes muerto Febrero 2014 '),
    dcc.Graph(
        id='mmf14',
        figure=mmf14

    ),
    html.H2(children=' Mes muerto Febrero 2015'),
        dcc.Graph(
            id='mmf15',
            figure=mmf15

        ),
    html.H2(children=' Mes muerto Febrero 2016'),
        dcc.Graph(
            id='mmf16',
            figure=mmf16

        ),
    html.H2(children=' Mes muerto Febrero 2017'),
        dcc.Graph(
            id='mmf17',
            figure=mmf17

        ),
    html.H2(children=' Mes muerto Febrero 2018'),
        dcc.Graph(
            id='mmf18',
            figure=mmf18

        ),
    html.H2(children=' Mes muerto Febrero 2019'),
        dcc.Graph(
            id='mmf19',
            figure=mmf19

        ),
    html.H2(children=' Mes muerto Febrero 2020'),
        dcc.Graph(
            id='mmf20',
            figure=mmf20

        ),


])

# port=8051
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
