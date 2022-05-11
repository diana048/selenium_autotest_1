class Animal:
    def voice(self):
        pass

class Dogs(Animal):
    def voice(self):
        print ('Собака гавкает')

class Cats(Animal):
    def voice(self):
        print ('Кошка мяукает')

class Mouses(Animal):
    def voice(self):
        print('Мышь пищит')

cat = Cats()
mouse = Mouses()
dog = Dogs()
dog.voice()
cat.voice()
mouse.voice()