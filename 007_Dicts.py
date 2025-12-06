### Dictionaries ###

mi_dict = dict()
otro_dict = {}

print(mi_dict, type(mi_dict))
print(otro_dict, type(otro_dict))

otro_dict = {"Nombre":"Arturo","Apellido":"Palau","Edad":20,"Matrícula":178561,1:"Python"}
mi_dict = {
    "Nombre":"Arturo",
    "Apellido:":"Palau",
    "Edad":20,
    "Lenguajes":{"Python","Java","PHP"},
    1:1.78
}

print(otro_dict,"Longitud:",len(otro_dict))
print(mi_dict,"Longitud:",len(mi_dict))

print(mi_dict["Nombre"]) #Imprimirá "Arturo"

mi_dict["Nombre"] = "Hatsu" #Modificamos "Nombre"
print(mi_dict["Nombre"]) #Imprimirá "Hatsu"

mi_dict[1] = 1.80

mi_dict["Calle"] = "Metales #133" #Agregamos un nuevo campo al diccionario
print(mi_dict)

del mi_dict["Calle"] #Eliminamos un elemento del diccionario
print(mi_dict)

print("Nombre" in mi_dict) # True
print("Hatsu" in mi_dict["Nombre"]) # True

print(mi_dict.items()) #Retorna la lista de cada item "Key y valor"
print(mi_dict.keys()) #Retorna las keys "Nombre","Apellido"
print(mi_dict.values()) #Retorna los valores de las keys

#Creamos un nuevo diccionario con keys iguales, pero sin datos
nuevo_dict = otro_dict.fromkeys(("Nombre",1))
#nuevo_dict = dict.fromkeys(("Nombre",1, "Piso"))
print(nuevo_dict)

lista = ["Nombre",1,"Piso"]

nuevo_dict = dict.fromkeys((lista))
print(nuevo_dict)
nuevo_dict = dict.fromkeys(("Nombre",1,"Piso"))
print(nuevo_dict)
#Hago una copia de un dict únicamente con las keys, no tienen valores
nuevo_dict = dict.fromkeys((mi_dict))
print(nuevo_dict)

#Todas las keys tendrán el valor "Arturo","Palau"
nuevo_dict = dict.fromkeys(mi_dict,("Arturo","Palau"))
print(nuevo_dict)

valores = nuevo_dict.values()
print(type(valores))

print(nuevo_dict.values())
print(list(nuevo_dict.values()))
print(dict.fromkeys(list(nuevo_dict.values())))
print(tuple(nuevo_dict))
print(set(nuevo_dict))