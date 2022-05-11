class Animal:
    def voice(self):
        pass

    numInstance = 0
    def __init__(self):
        Animal.numInstance = Animal.numInstance + 1

    def __int__(self):
       print(Animal.numInstance)

    numInstance = staticmethod(numInstance)


class Dogs(Animal):
    def voice(self):
        print ('Собака гавкает')

class Cats(Animal):
    def voice(self):
        print ('Кошка мяукает')

class Mice(Animal):
    def voice(self):
        print ('Мышь пищит')


cat = Cats()
dog = Dogs()
mouse = Mice()

dog.voice()
cat.voice()
mouse.voice()

Animal.__int__(Animal.numInstance)