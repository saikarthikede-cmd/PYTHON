class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(self.name,self.marks)
s1=Student("Sai",85)
s1.display()

s2=Student("Karthik",50)
s2.display()
