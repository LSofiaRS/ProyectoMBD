import psycopg2

try:
    conexion = psycopg2.connect(user = "postgres",
				password = "12345",
				database = "peajes",
				host = "localhost",
				port = "5432")
    print ("Conexion correcta \n")
    conexion.autocommit = False

    sql1 = """ select * from categoria_vehicular; """
    sql2 = """ select * from peaje; """
    sql3 = """ select * from tarifa; """
    sql4 = """ select * from recaudo; """
    sql5 = """ select * from trafico; """
    
    #Consulta tabla categoria_vehicular
    cursor = conexion.cursor()
    cursor.execute(sql1)
    categorias = cursor.fetchall()
    print ("*** CATEGORIA *** \n")
    for categoria in categorias:
        print(categoria[0], '|' ,categoria[1])
        print("---------------------------------------------")
    print("\n")
    
    #Consulta tabla peaje
    cursor.execute(sql2)
    peajes = cursor.fetchall()
    print ("*** PEAJE *** \n")
    for peaje in peajes:
        print(peaje[0], '|', peaje[1])
        print("---------------------------------------------")
    print("\n")
    #Consulta tabla tarifa
    cursor.execute(sql3)
    tarifas = cursor.fetchall()
    print("*** TARIFA *** \n")
    for tarifa in tarifas:
        print(tarifa[0], '|', tarifa[1], '|',tarifa[2], '|', tarifa[3])
        print("--------------------------------------------")
    print("\n")
    
    #Consulta tabla recaudo
    cursor.execute(sql4)
    recaudos = cursor.fetchall()
    print ("*** RECAUDOS *** \n")
    for recaudo in recaudos:
        print(recaudo[0], '|',recaudo[1],'|',recaudo[2],'|',recaudo[3], '|',recaudo[4],'|',recaudo[5],'|',recaudo[6])
        print("--------------------------------------------")
    print("\n")
    
    #Consulta tabla trafico
    cursor.execute(sql5)
    traficos = cursor.fetchall()
    print("*** TRAFICO ***")
    for trafico in traficos:
        print(trafico[0],'|',trafico[1],'|',trafico[2],'|',trafico[3],'|', trafico[4],'|',trafico[5],'|',trafico[6],'|',trafico[7])
        print("--------------------------------------------")
    print("\n")

except psycopg2.Error as e:
   print ("Error al consultar",e)

finally:
   cursor.close()
   conexion.close() 
   print("Conexion cerrada")
