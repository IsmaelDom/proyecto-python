# Se importa el modelo Usuario
import usuarios.usuario as userModel
# Se importa el modulo de acciones de notas
import notas.acciones

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
                self.proximasAcciones(login)

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Correo o Contraseña incorrecta, vuelve a intentarlo")

    # Metodo 
    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles(Ingresa el número):
            1.- Crear nota (Ingrese -> 1)
            2.- Mostrar tus notas (Ingrese -> 2)
            3.- Eliminar nota (Ingrese -> 3)
            4.- Salir (Ingrese -> 4)
        """)

        accion = int(input("Ingrese el número de lo que desea hacer: "))
        notaAcciones = notas.acciones.Acciones()
        
        if accion == 1:
            notaAcciones.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 2:
            notaAcciones.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 3:
            notaAcciones.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 4:
            print("\nSaliendo....\nSe ha cerrado la sesión")
            exit()