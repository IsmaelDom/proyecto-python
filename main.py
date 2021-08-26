from usuarios import acciones

print("""
    Acciones disponibles:
        1.- Registro
        2.- Login
""")

# Se crea la instancia a la clase acciones
actions = acciones.Acciones()
accion = int(input("¿Qué desea hacer?(Ingrese el número):"))

if accion == 1:
    actions.registro()

elif accion == 2:
    actions.login()