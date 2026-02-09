class Animal():
    def sound(self):
        print("makes sounds")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("barks")
a=Dog()
a.sound()
