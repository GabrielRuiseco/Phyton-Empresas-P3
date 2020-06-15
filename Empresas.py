import Clases

menu = Clases.Menu()
opc = input("\nSeleccione una opcion:")
if opc == "1" or opc == "2" or opc == "3" or opc == "4" or opc == "5" or opc == "6":
    while opc != "6":
        if opc == "1":
            menu.inter.agregarEmpresa()
            opt = input("\ndesea introducir un nuevo cliente?")
            while opt != "no":
                menu.inter.agregarCliente()
                opt = input("\ndesea introducir un nuevo cliente?")
            else:
                menu.mostrar()
                opc = input("\nSeleccione una opcion:")
        elif opc == "2":
            menu.mostrar()
            opc = input("\nSeleccione una opcion:")
        elif opc == "3":
            menu.addProduct()
            menu.mostrar()
            opc = input("\nSeleccione una opcion:")
        elif opc == "4":
            menu.inter.agregarCompra()
            menu.mostrar()
            opc = input("\nSeleccione una opcion:")
        elif opc == "5":
            opt = ""
            while opt != "no":
                menu.inter.agregarCliente()
                opt = input("\ndesea introducir un nuevo cliente?")
            else:
                menu.mostrar()
                opc = input("\nSeleccione una opcion:")
    else:
        menu.endProg()
else:
    print("\nOpcion no valida\n")
    menu.mostrar()
    opc = input("\nSeleccione una opcion:")
