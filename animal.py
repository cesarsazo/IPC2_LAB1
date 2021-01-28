class animal:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return 'Soy un animal y mi nombre es: {}, y mi edad es: {}'.format(self.nombre, self.edad)

class perro(animal):

    def sonido(self):
        print('Guau!')
    
class gato(animal):

    def sonido(self):
        print('Miiauu!!')