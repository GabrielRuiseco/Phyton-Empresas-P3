import Clases

menu = Clases.Menu()
opc = input("\nSeleccione una opcion:")
if opc == "1" or opc == "2" or opc == "3":
    while opc != "3":
        if opc == "1":
            menu.registro()
            opt = ""
            while opt != "no":
                menu.empleado()
                opt = input("\ndesea introducir un nuevo cliente?")
            else:
                menu.inter.createAtDB()
                menu.mostrar()
                opc = input("\nSeleccione una opcion:")
        elif opc == "2":
            menu.mostrar()
            opc = input("\nSeleccione una opcion:")
    else:
        menu.salir()
else:
    print("\nOpcion no valida\n")
    menu.mostrar()
    opc = input("\nSeleccione una opcion:")
