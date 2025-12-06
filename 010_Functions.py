### Functions ###
# Definir valores por defecto
def saludar(nombre = "Null",apellido = "Null",edad = "Null"):
    print(f"Hola {nombre} {apellido}! Tu edad es: {edad} años")

#Con el asterísco, imprimimos todos los datos que nos manden
def imprimir(*mensajes):
    print(mensajes)

def fibonacci (n):
    if n == 0: return 0
    elif n == 1 : return 1
    elif n > 1 : return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0: return 1
    if n > 0: return n*factorial(n-1)
        

def resta(n1,n2):
    return n1-n2



n = int(input("Valor de n:"))

for i in range(n):
    print(fibonacci(i),", ")
print(fibonacci(n))

print(f"Factorial de {n} : {factorial(n)}")



n1 = 6
n2 = 3
print(f"La resta de {n1} - {n2} es {resta(n1,n2)}")

saludar()
saludar("Arturo", "Palau", 20)
imprimir("Hola","Buenas","Tardes")