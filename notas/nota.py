# Se importan las bibliotecas necesarias
import usuarios.conexion as conexion

# Se obtienen los datos de la conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

# Clase para interactuar con la tabla notas
class Nota:

    # Constructor de la clase
    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    # Metodo para insertar en la tabla notas
    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW());"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]