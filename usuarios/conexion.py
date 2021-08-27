# Se importan las bibliotecas necesarias
import mysql.connector

def conectar():
    # Se realiza la conexion con la bd
    database = mysql.connector.connect(
        host = "",
        user = "",
        passwd = "",
        database = "master_python",
        port = 3306
    )

    # Permite ejecutar muchas consultas con el mismo cursor
    cursor = database.cursor(buffered = True)

    return [database, cursor]