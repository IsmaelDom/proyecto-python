# Se importan las bibliotecas necesarias
import mysql.connector
import datetime
import hashlib

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

class Usuario():
    """docstring for Usuario."""

    # Constructor de la clase
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, email, password):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.email = email
        self.password = password
    
    # Metodo que guarda en la bd los registros que recibe acciones.registro
    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s, %s);"

        usuario = (self.nombre, self.apellidoPaterno, self.apellidoMaterno, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except Exception as e:
            # raise e
            result = [0, self]

        return result

    def identificar(self):
        return self.nombre