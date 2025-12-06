### Listas :O ###

mi_lista = list()
otra_lista = []

print(mi_lista)
print(len(mi_lista))

mi_lista = [13, 45, 44, 36, 7, 90, 89]
print(mi_lista)
print(len(mi_lista))

otra_lista = ["Arturo", "HatsuNeo", 20, 750.5]
nombre, gamertag, age, money = otra_lista # Desempaquetamos los datos de la lista en variables
print(otra_lista)
print(nombre, gamertag, age, money)
""""
print(otra_lista[1])
print(otra_lista[2])
print(otra_lista[-1]) #Último elemento
print(otra_lista[-2])
"""
print(mi_lista[len(mi_lista)-1])

nombres = ["Jaime","Paco","Andres","Jaime","Alberto","Jaime"]

print(nombres.count("Jaime"))# Hay 3 registros de "Jaime"

print(mi_lista + otra_lista) #Imprimir 2 listas
#print(list[1,2,3,4])
#print([1,2,3,4])

mi_lista = ["Nombre", 12]
mi_lista.append("Descripcion") #Insertar al Final
mi_lista.insert(1,"Apellido") # Insertar en una posición

#del mi_lista[2] #Otra forma de eliminar

#mi_lista.clear #Limpiar toda la lista

print(mi_lista)
mi_lista.remove("Nombre") #Elimina el primer elemento que coincida con el parámetro
print(mi_lista)

print(nombres.pop(1)) #Eliminar un elemento de la lista
print(nombres.pop()) #Imprimir el elemento que se acaba de eliminar
print(nombres)

elemento_eliminado = nombres.pop() #Guardar el elemento eliminado

nombres[2] = "Edgardo" #Modificar un elemento en cierta posición

lista_copiada = mi_lista.copy() # Copiar una lista

print(mi_lista)
mi_lista.reverse()
print(mi_lista)

lista = [9,8,7,6,5,4,3,2,1]
print(lista)
lista.sort() #Ordena la lista
print(lista) 