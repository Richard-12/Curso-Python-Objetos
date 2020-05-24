#Constructor:

class Persona:
    pass
    def __init__(self,nombre,año):
        self.nombre=nombre
        self.año=año  #Hasta aquí se tiene la base del contructor
    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre,self.año)

    def comentario(self,frase):
        return '{} dice: {}'.format(self.nombre,frase)

doctor=Persona('jose',26)
print(doctor.descripcion())
print(doctor.comentario('hola que tal'))


