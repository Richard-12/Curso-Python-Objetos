#Herencia: Orientación y encapsulación. La herencia es una de las característica mas importantes de la programación orientada a objetos-
#Consiste en la creación de una nueva clase a partir de una o varias clases existentes.
#Las clases reciben formas que se denominan clases secundarias, clases primarias, clases hijo, clases padre.

     # class NombreSubclase(NombreClaseSuperior):

     # class ClaseBase:
     #     Cuerpo de la clase base

     #class DerivadoClase (ClaseBase):
     #     Cuerpo de la clase derivada

class Pokemon:
    pass
    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo

    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre,self.tipo)

class Pikachu(Pokemon):
    def ataque (self,tipoataque):
        return '{} Tiene un tipo de ataque: {}'.format(self.nombre,tipoataque)

class Charmander(Pokemon):
    def ataque(self,tipoataque):
        return '{} Tiene un tipo de ataque: {}'.format(self.nombre, tipoataque)

nuevo_Pokemon=Pikachu('Boby','Eléctrico')
print(nuevo_Pokemon.descripcion())
print(nuevo_Pokemon.ataque('Impacto trueno'))

