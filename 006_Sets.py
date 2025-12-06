### Sets ###

"""
1. Un set es una estructura desordenada
2. No guarda datos repetidos
"""

mi_set = set()
otro_set = {}

print(type(mi_set)) # set
print(type(otro_set)) # dict "Inicialmente es un Diccionario"

otro_set = {"Arturo","Palau",20,750.50}
print(type(otro_set)) # Ahora sí es un set

print(len(otro_set)) # Longitud del Set

#print(otro_set[2]) #Error, ya que esta desordenado
otro_set.add("HatsuNeo") #Lo mete donde quiere
print(otro_set)
otro_set.add("Buenas tardes") #Lo mete donde quiere
print(otro_set)
otro_set.add("HatsuNeo") #Dato repetido, NO lo va a guardar
print(otro_set) # Un set no admite datos repetidos

#Comprobar si hay un dato en el Set
print("Palao" in otro_set) # Comprobar si un dato esta en el Set =>False
print("Palau" in otro_set) # ==> True

otro_set.clear() # Limpiamos el Set
print(otro_set, "Longitud: ",len(otro_set))

del otro_set #Eliminamos el set, y la variable

mi_set = {"Arturo","Palau",20,750.50}
mi_lista = list(mi_set) # Cambiar Set a Lista
print(mi_lista[0])

otro_set = {"Java","Python","DevC++"}
#Unimos en el Set
nuevo_set = mi_set.union(otro_set)
#Unimos únicamente para este print, no se guarda en la variable
print(nuevo_set.union(nuevo_set).union(otro_set).union({"JavaScript","MySQL"})) 

print(nuevo_set.difference(mi_set)) # Le quitamos a "nuevo_set" los elementos de "mi_set"