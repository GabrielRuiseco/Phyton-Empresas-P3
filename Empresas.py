import Clases

menu = Clases.Menu()
opc = input("\nSeleccione una opcion:")
while opc != "3":
    if opc == "1":
        menu.registro()
        opt = ""
        while opt != "no":
            menu.empleado()
            opt = input("\ndesea introducir un nuevo cliente?")
        else:
            menu.mostrar()
            opc = input("\nSeleccione una opcion:")
    elif opc == "2":
        menu.mostrar()
        opc = input("\nSeleccione una opcion:")
else:
    menu.salir()
