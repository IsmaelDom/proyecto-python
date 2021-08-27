# Se importa el modelo Nota
import notas.nota as notaModel

# Clase para hacer CRUD con la tabla notas
class Acciones:

    # Metodo para insertar una nota en la tabla notas
    def crear(self, usuario):
        print(f"\n{usuario[1]}, se creará una nueva nota....")

        titulo = input("Ingresa el titulo de la nota: ")
        descripcion = input("Ingresa el contenido de la nota: ")

        nota = notaModel.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nSe ha guardado correctamente la nota: {nota.titulo}")
        
        else:
            print(f"\nNo se pudo guardar la nota: {nota.titulo}")