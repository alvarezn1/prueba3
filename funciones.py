
import random as rd



vehiculos = []
patentes = []
def grabar():

    
    print("Ingrese tipo de auto")
    tipo = input()
    vehiculos.append(tipo)
    print("Ingrese patente de auto")
    patente = input()
    patentes.append(patente)
    print("Ingrese marca de auto")
    marca = input()
    vehiculos.append(marca)
    
    print("Ingrese precio del auto")
    precio = int(input())
    if precio < 5000000:
        print("Ingrese un precio correcto")
        precio = int(input())
    else:
        vehiculos.append(precio)
    
    print("¿El vehiculo reistra multa? 1) SI 2) NO")
    peer = int(input())
    if peer == 1:
        monto = int(input("Ingrese monto de la multa"))
        vehiculos.append(monto)
        fecha = input("Ingrese fecha de multa")
        vehiculos.append(fecha)
    
    else:
        monto = 0
        vehiculos.append(monto)
        fecha = 0
        vehiculos.append(fecha)
    
    registro = input("Ingrese fecha de registro del vehiculo")
    vehiculos.append(registro)
    dueno = input("Ingrese nombre del dueño del vehiculo")
    vehiculos.append(dueno)

    print(vehiculos)
    return grabar



def imprimir():

    valores = [rd.randint(1500,3500) for i in range(1)]
    valores2 = [rd.randint(1500,3500) for i in range(1)]
    valores3 = [rd.randint(1500,3500) for i in range(1)]

    print("1) Certificado de emision de contaminantes $",valores)
    print("2) Certificado de anotaciones vigentes $:", valores2)
    print("3) Certificado de multas $:", valores3)
    elec = int(input())
    if elec == 1:
        
        print("-----------------------------------------")
        print("Certificado de emision de contaminantes")
        print("Patente:", patentes)
        print("Datos:",vehiculos)
    elif elec == 2:
       
        print("-----------------------------------------")
        print("Certificado de anotaciones vigentes")
        print("Patente:",patentes)
        print("Datos:", vehiculos)
    
    else:
        
        print("-----------------------------------------")
        print("Certificado de emision de multas")
        print("Patente:", patentes)
        print("Datos:", vehiculos)
        


 

    

    

    return imprimir


def salir():
    print("Gracias por usar esta plataforma!!")
    print("---------------------------------")
    print("----------- ATENTAMENTE------------")
    print("-----------Kevin Alvarez-------------")
    print("-----------Version: 1.0----------------")

    return salir

    



def buscar():
    pat = input("Ingrese patente a buscar")

    if pat == patentes:
        print(patentes)
        print(vehiculos)
    else:
        print("Ingrese una patente valida")
        pat = input()
        print(patentes)
        print(vehiculos)

    return buscar

















