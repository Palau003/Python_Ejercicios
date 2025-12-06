#Validaciones

def entero(mensaje):
    bandera = False
    while not bandera:
        bandera = False
        num = input(mensaje)
        if(num.isnumeric): bandera = True
        else: print("Error, introduce un número!")
    return num

def positivo(mensaje):
    bandera = False
    while not bandera:
        bandera = False
        num = input(mensaje)
        if(num.isnumeric and num >= 0): bandera = True
        else: print("Error! Introduce un número positivo!")
    return num

