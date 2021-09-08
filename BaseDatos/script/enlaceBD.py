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
        consulta = "INSERT INTO Socios(id,Nombre, Apellido) VALUES (?, ?);"
        cursor.execute(consulta, (1, "socio1", "apellido1"))
        cursor.execute(consulta, (2, "socio2", "apellido2"))
    # No olvidemos hacer commit cuando hacemos un cambio a la BD
    conexion.commit()
    print("carga realizada con éxito")

except Exception as e:
    print("Ocurrió un error al insertar: ", e)
finally:
    conexion.close()

try:
    with conexion.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT * FROM Socios;")
       
except Exception as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()