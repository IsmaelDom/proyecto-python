# Se importan las bibliotecas necesarias
import usuarios.conexion as conexion

# Se obtienen los datos de la conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

# Clase para interactuar con la tabla notas
class Nota:

    # Constructor de la clase
    def __init__(self, usuario_id, titulo = "", descripcion = ""):
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

    # Metodo para listas las notas del usuario logueado
    def listar(self):
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"

        cursor.execute(sql)
        result = cursor.fetchall()
        
        return result

    # Metodo para eliminar una nota
    def eliminar(self):
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%';"

        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]