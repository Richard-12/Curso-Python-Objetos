# Herencia: funciones de prueba.
# Se utilizará el ejemplo anterior
class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [int(input('Ingrese los datos ' + str(i + 1) + ' = ')) for i in range(self.n)]


class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self):
        a, b, = self.datos
        s = a + b
        print('El resultado de la suma  es: ', s)

    def resta(self):
        a, b, = self.datos
        r = a - b
        print('El resultado de la resta es: ', r)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        import math
        a = self.datos[0]
        print('La raíz cuadrade es: ', math.sqrt(a))


ejemplo = op_basicas()
ejemplo.ingresardato()
ejemplo.suma()
ejemplo.resta()
ejemplo_raiz = raiz()
ejemplo_raiz.ingresardato()
ejemplo_raiz.cuadrada()

# isinstance permite verificar la herencia
objeto = op_basicas()
print('objeto es heredero de raiz?: ')
print(isinstance(objeto, raiz))
print('objeto es heredero de op_basicas?: ')
print(isinstance(objeto,op_basicas))
print('objeto es heredero de Calculadora?: ')
print(isinstance(objeto,Calculadora))
#Tambien permite verificar si tenemos una clase hijo pertenece a la clase padre.
print('Calculadora es heredero de op-basicas?: ')
print(issubclass(Calculadora,op_basicas))
print('op-basicas es heredero de Calculadora?: ')
print(issubclass(op_basicas,Calculadora))
