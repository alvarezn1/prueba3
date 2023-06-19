import funciones as fn



menu = True

while menu == True:
    print("----Bienvenidos a 'Auto Seguro'----")
    print("1) Grabar")
    print("2) Buscar")
    print("3  Imprimir certificados")
    print("4) Salir")
    op = input()
    if op == "1":
        fn.grabar()
    elif op == "2":
        fn.buscar()
    elif op == "3":
        fn.imprimir()
    else:
        fn.salir()
        menu = False
        break