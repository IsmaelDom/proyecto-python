import usuarios.usuario as userModel

class Acciones():
    """docstring for Acciones."""

    # Metodo que obtiene los datos a guardar en la bd
    def registro(self):
        print("Se va a registrar en el sistema....\n")

        nombre = input("Ingresa tu nombre: ")
        apellidoPaterno = input("Ingresa tu apellido paterno: ")
        apellidoMaterno = input("Ingresa tu apellido materno: ")
        email = input("Ingresa tu correo: ")
        password = input("Ingresa tu contraseña: ")

        # Se llama a la clase Usuario
        usuario = userModel.Usuario(nombre, apellidoPaterno, apellidoMaterno, email, password)
        # Se llama al metodo para registrar
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Bienvenido, {registro[1].nombre} te has registrado con el correo {registro[1].email}")
        else:
            print("No se pudo realizar el registro")
    
    # Metodo para iniciar sesion
    def login(self):
        print("Por favor, identificate en el sistema....\n")

        email = input("Ingresa tu correo: ")
        password = input("Ingresa tu contraseña: ")