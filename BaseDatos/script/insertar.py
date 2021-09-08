from enlaceBD import conexion
try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO Socios(Nombre, Apellido) VALUES (?, ?);"
        cursor.execute(consulta, ("socio1", "apellido1"))
        cursor.execute(consulta, ("socio2", "apellido2"))
    # No olvidemos hacer commit cuando hacemos un cambio a la BD
    conexion.commit()

except Exception as e:
    print("Ocurrió un error al insertar: ", e)
finally:
    conexion.close()

try:
    with conexion.cursor() as cursor:
        # En este caso no necesitamos limpiar ningún dato
        cursor.execute("SELECT id, Nombre, Apellido FROM Socios;")
        # Hacer un while, mientras fetchone no regrese None
        socio = cursor.fetchone()
        while socio:
            print(socio)
            socio = cursor.fetchone()

except Exception as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()