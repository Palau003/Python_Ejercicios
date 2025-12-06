### Loops ###

# While

bandera = True

i = 0
while bandera:
    i+=1
    print(" Valor actual: "+str(i))
    
    if(i == 8): 
        print("Hora de salir!") 
        break #Salimos, y no se ejecuta el "else" de abajo
    if i==10: bandera = False
else:
    print("  Acabo el ciclo!")

print("Hola XD")

# For

lista = [12,24,36,48,60]
tupla = (10,20,30,40,50)
set = {5,10,15,20,25}
dic = {"Nombre":"Arturo","Apellido":"Palau","Edad":20}

for element in lista:
    print(element)
    
for element in tupla:
    print(element)

for element in set:
    print(element)
    if element == 20:
        print("Se encontró el 20, salir del ciclo!")
        break

for element in dic:
    print(element,dic[element])
    if element == "Edad":
        continue #Terminar este ciclo, iniciar el siguiente del For
        #Este break no se ejecutará por culpa de "continue"
        break #Terminar por completo el ciclo For
    print("Ejecutando...")
else:
    print("Fin del diccionario")

#Imprime todo
for element in lista,tupla,set,dic:
    print(element)



