#Ejercicios prácticos sobre herencia.
class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos= [0 for i in range(numero)]

    def ingresardato(self):
        self.datos= [int(input('Ingrese los datos '+str(i+1)+ ' = ')) for i in range(self.n)]

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
        a,b,=self.datos
        s=a+b
        print('El resultado de la suma es: ',s)

    def resta(self):
        a,b,=self.datos
        r=a-b
        print('El resultado de la resta es: ',r)

    def producto(self):
        a,b,=self.datos
        p=a*b
        print('El resultado del producto  es: ',p)

    def potencia(self):
        a, b, = self.datos
        pot = a ** b
        print('El resultado de la potencia  es: ', pot)
#Segunda subclase
class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math
        a, = self.datos
        print('El resultado de la raiz cuadrada  es: ',math.sqrt(a))


# Creación de objeto 1
ejemplo = op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.suma())
print(ejemplo.resta())
print(ejemplo.producto())
print(ejemplo.potencia())
#Creación de objeto 2
ejemplo = raiz()
print(ejemplo.ingresardato())
print(ejemplo.cuadrada())


