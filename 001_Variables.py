mensaje = "Quiero molito" #String
flag = True #Boolean
num = 123 #Integer
dec = 123.45 #Float

cambio1 = str(num) #convierte a String
cambio2 = int("123") #convierte a Integer
cambio3 = float("123.45") #convierte a Float

#Declarar variables en una sola línea (NO RECOMENDABLE)
nombre, apellido, edad = "Arturo" , "Palau" , 20

#print("Tipo de print(): ",type(print()))
"""print("Nombre: ",nombre, "\tApellido: ",apellido,"\tEdad: ",edad)

print("Var 1: ", mensaje, type(mensaje))
print("Var 2: ", flag, type(flag))
print("Var 3: ", num, type(num))
print("Var 4: ", dec, type(dec))
print("Var 5: ", cambio1, type(cambio1))
print("Var 6: ", cambio2, type(cambio2))
print("Var 7: ", cambio3, type(cambio3))

print("Tamaño del mensaje (",mensaje,") :",len(mensaje)) #Tamaño de un String"""

#Ingresamos Datos "Inputs"
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
print("Nombre: ",nombre,"\tApellido: ",apellido,"\tEdad: ",edad)

#Cambiamos el tipo de los datos
nombre = 20
edad = "Palau"

print(nombre,type(nombre))
print(edad,type(edad))

#¿Forzamos el tipo de dato?
address : str = "Metales #133"
print("Dirección: ",address,type(address))
address = 32
print("Dirección: ",address,type(address))