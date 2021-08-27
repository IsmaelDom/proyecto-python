# Se importan las bibliotecas necesarias
import datetime
import hashlib
import usuarios.conexion as conexion

# Se obtienen los datos de la conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

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

    # Metodo que valida si existe el usuario con la contraseña ingresada
    def identificar(self):
        # Consulta para saber si la contraseña le pertenece al email
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Se toman los datos ingresados por el usuario
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result