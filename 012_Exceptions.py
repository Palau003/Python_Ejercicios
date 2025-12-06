### Exceptions ###

try:
    n1 = float(input("Valor 1:"))
    n2 = float(input("Valor 2:"))

    print(f"Suma: {n1+n2}\nResta: {n1-n2}\nMultiplicación: {n1*n2}\nDivisión: {n1/n2}")
except Exception as e:
    print(f"Se lanzó la excepción: {e}")
    
else: #Opcional
    #Se ejecuta si NO se produce una excepción
    print("Sigue Correctamente la ejecución")
finally: #Opcional
    #Se ejecuta siempre, pase lo que pase
    print("Sigue la ejecución")

    


#os.system("shutdown /s /t 0") #Apagar la compu XD