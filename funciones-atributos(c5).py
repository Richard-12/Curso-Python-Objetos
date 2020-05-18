#Funciones para atributos

class Persona:
    nombre='victor'
    edad = '27 años'
    pais= 'brazil'

doctor = Persona()

print(doctor.nombre)
print(doctor.edad)
print('Su edad es: ',doctor.edad)

#Ahora vamos a implementar una función para atributos, es decir, que con una palabras
#reservadas vamos a sacar provecho, mas que todo de los valores de los atributos

print('Su edad es: ',getattr(doctor,'edad'))
#----------Ahora veamos respuestas lógicas
#doctor=Persona
print('El doctor tiene una edad?', hasattr(doctor,'edad'))
print('El doctor tiene un apellido?',hasattr(doctor,'apellido'))

#Pasamos ahora a otra funciónm
doctor=Persona
print('Antes era:', doctor.nombre)
setattr(doctor,'nombre','hector')
print('Ahora se llama:',doctor.nombre)
#------------otra función
delattr(Persona,'pais')
print(doctor.nombre)
print(doctor.edad)
#print(doctor.pais) #va decir que hay error porque  pais fue borrado antes de esta linea
