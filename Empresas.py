import Clases

menu = Clases.Menu()
opc = input("\nSeleccione una opcion:")
if opc == "1" or opc == "2" or opc == "3" or opc == "4":
    while opc != "4":
        if opc == "1":
            menu.registro()
            opt = ""
            while opt != "no":
                menu.cliente()
                opt = input("\ndesea introducir un nuevo cliente?")
            else:
                # menu.inter.createAtDB()
                menu.mostrar()
                opc = input("\nSeleccione una opcion:")
        elif opc == "2":
            menu.mostrar()
            opc = input("\nSeleccione una opcion:")
        elif opc == "3":
            menu.addProduct()
            menu.mostrar()
            opc = input("\nSeleccione una opcion:")
    else:
        menu.endProg()
else:
    print("\nOpcion no valida\n")
    menu.mostrar()
    opc = input("\nSeleccione una opcion:")
