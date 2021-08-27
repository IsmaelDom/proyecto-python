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

        try:
            email = input("Ingresa tu correo: ")
            password = input("Ingresa tu contraseña: ")

            usuario = userModel.Usuario('', '', '', email, password)
            login = usuario.identificar()

            if email == login[4]:
                print(f"\nBienvenido, {login[1]}, te has registrado en el sistema el {login[6]}")

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Correo o Contraseña incorrecta, vuelve a intentarlo")