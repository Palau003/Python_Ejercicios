### Tuples ###

#Las Tuplas contienen datos Inmutables (No se pueden modificar)

tupla_1 = tuple()
tupla_2 = ()

tupla_1 = (20,750.5,"Arturo","Palau")
print(tupla_1)
print(type(tupla_1))

print("Valor en la posición 2 =>",tupla_1[2])
print("Último valor ==>", tupla_1[-1])

print(tupla_1.count("Palau")) #Palau sale 1 veces
print(len(tupla_1)) #Longitud => 4

print(tupla_1.index("Palau")) #Nos da el index de "Palau" Posición ==>[3]

#Error
#tupla_1[3] = "Palao" #En una Tupla no se pueden modificar los datos así
#print(tupla_1)

tupla_2 = (12,24,36)
print(tupla_2[1:3]) # (12, |24, 36| )
print(tupla_1 + tupla_2)

print(type(tupla_1))
tupla_1 = list(tupla_1) #Cambiamos Tupla a Lista
print(type(tupla_1))
#Al ser Lista, ya podemos insertar y modificar
print(tupla_1)
tupla_1[0] = 21
print(tupla_1)

print(type(tupla_1))
tupla_1 = tuple(tupla_1) #Cambiamos Lista a Tupla
print(type(tupla_1))
#Al cambiar a Tupla, los datos ya no cambian
print(tupla_1)