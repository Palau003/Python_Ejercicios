cad1 = 'Hola '
cad2 = "wenas."
cad3 = cad1+cad2

print(cad3, "Longitud: ",len(cad3))
print("Salto de línea '\\n'\nTabulación'\\t'")

### Formatear Strings ###
nombre, apellido, edad = "Arturo","Palau",20

print("Nombre: ",nombre,apellido,", Edad: ",edad)
print("Nombre: {} {}, Edad: {}".format(nombre,apellido,edad))
print("Nombre: %s %s, Edad: %d" %(nombre,apellido,edad))
print(f"Nombre: {nombre} {apellido}, Edad: {edad}") # La mejor forma

#Desempaquetado de caracteres
pez = "Fish"
a,b,c,d = pez
print(pez)
print(f"{a}{b}{c}{d}")

pe = pez[1:3]
print(pe) # F|is|h => is

saludo = "Buenasss"
print(saludo[2:]) #enasss
print(saludo[-4]) # Buen|a|sss => a

#Reverse

odulas = saludo[::-1]
print(odulas) #sssaneuB

print("arturo".capitalize()) #Arturo
print("arturo".upper()) # ARTURO
print("ARTURO".lower()) # arturo
print("arturo".count("r")) #A|r|tu|r|o => 2
print("trece".isnumeric()) # False
print("13".isnumeric()) # True
print("trece".upper().islower()) # "TRECE".islower() => False

print("Hola".startswith("Ho")) # True
print("Hola".endswith("la")) # True

print("hola" == "Hola") # False