### Classes ###

class Animal:
    #Constructor default
    def __init__(self, nombre = "Nombre", tipo="Tipo", color="Color", edad = "Edad"):
        self.nombre = nombre
        self.tipo = tipo
        self.color = color
        self.__edad = edad # Hacemos Private la edad
    
    #Métodos
    def comer(self,comida):
        print("Estoy comiendo "+comida)

    def saludar(self):
        print(f"Mi nombre es {self.nombre}, soy un {self.tipo} de color {self.color}")
    
    def dormir(self,sonido):
        print(sonido)
    
    #Métodos Get y Set
    def get_edad(self):
        return self.edad
    
    def set_edad(self,edad):
        self.edad = edad

#Instanciamos enviando parámetros        
gordo = Animal("Gordo","gato","Vaca")

gordo.saludar()
gordo.comer("Atún")
gordo.dormir("Miau zzzzzz")
#Con los datos por defecto
guero = Animal()
guero.saludar()
#Mandamos datos
guero = Animal("Wero","gato","Naranja")
guero.nombre = "Guero"
guero.saludar()
guero.comer("Croquetas")
guero.dormir("Palau zzzzzz")

guero.set_edad(5)
print(f"La edad de {guero.nombre} es: {guero.get_edad()}")