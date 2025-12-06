### Conditionals ###

bandera = True

if bandera:
    print("Hola")
    bandera = False
    if not bandera:
        print("Es falso")
else:
    print("1+1 es:",(1+1))

if 5 > 6:
    print("Baboso")
else:
    print("Bien")

calif = 8.2
pago = True

if calif >= 7 and pago:
    print("Bien hecho, pasaste!")
elif (calif >= 7) and (not pago):
    print("Pasaste, pero te falta pagar")
else:
    print("Algo falta, y me da hueva validarlo")


cadena = "" # False

if cadena: print("La cadena NO está vacía")
else: print("La cadena está vacía")

cadena = "Krakatoa"

if cadena: print("La cadena NO está vacía")
else: print("La cadena está vacía")

if "Hola" == "hola":
    print("Son iguales")
if "Papa" == "Papa":
    print("Papa")