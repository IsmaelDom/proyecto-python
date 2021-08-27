import mysql.connector

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

    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, email, password):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.email = email
        self.password = password
    
    def registrar(self):
        return self.nombre

    def identificar(self):
        return self.nombre