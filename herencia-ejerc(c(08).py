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
        print('El resultado es: ',s)

    def resta(self):
        a,b,=self.datos
        r=a-b
        print('El resultado es: ',r)


class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def cuadrada(self):
        import math
        a, = self.datos
        print('El resultado es: ',math.sqrt(a))

#ejemplo = op_basicas()
 #print(ejemplo.ingresardato())
#print(ejemplo.suma())

ejemplo = raiz()
print(ejemplo.ingresardato())
print(ejemplo.cuadrada())

