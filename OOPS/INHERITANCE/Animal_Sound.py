class Animal():
    def sound(self):
        print("animal sounds")
class Dog(Animal):
    def sound(Self):
        super().sound() #superclass-->to call the methods from parent class
        print("dog barks")
class cat(Animal):
    def sound(self):
        print("cat meows")
Dog().sound()
cat().sound()
