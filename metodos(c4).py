#Métodos. Es una función pero que está dentro de una clase
#Un metodo determina una acción o un comportamiento.

#class nombre de la clase
    #def nombre del metodo(self se refiere al objeto):
#self.nombre de la variable=algoritmo o un valor específico

class Matematica:
    def suma(self):
        self.n1=2
        self.n2=3
s=Matematica()   # copiamos un metodo
s.suma()
print(s.n1 +s.n2)


        




