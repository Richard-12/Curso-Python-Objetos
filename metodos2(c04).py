#Metodos pero ahora como constructores
#Se le llama: _init_(seft)
           #(iniciar)

class Ropa:
    def __init__(self):
        self.marca='wilow'
        self.talla='M'
        self.color='rojo'
#Ahora creamos el objeto.

camisa=Ropa()
print(camisa.talla)
print(camisa.marca)
#------------- creamos otra clase

class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1+n2
        self.resta = n1 - n2
        self.producto = n1*n2
        self.division = n1/n2

#Ahora creamos el objeto
operacion = Calculadora(2,3)
print(operacion.producto)
print(operacion.division)
print(operacion.resta)
print(operacion.suma)

