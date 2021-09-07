import pyodbc
direccion_servidor = 'localhost'
nombre_bd = 'BochasSportClub'
nombre_usuario = 'sa'
password = '1234'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa
    print('la conexion es correcta')
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)


try:
    with conexion.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT id, Nombre FROM Actividades")
        # Hacer un while, mientras fetchone no regrese None
        actividad = cursor.fetchone()
        while actividad:
            print(actividad)
            actividad = cursor.fetchone()
except Exception as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()