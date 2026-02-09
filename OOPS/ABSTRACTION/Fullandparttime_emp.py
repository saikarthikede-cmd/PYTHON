from abc import ABC, abstractmethod
class employee(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def calculate_salary(self):
        pass
class fulltimeemployee(employee):
    def calculate_salary(self):
        return f"Full-time Employee {self.name} has a fixed monthly salary."
class parttimeemployee(employee):
    def calculate_salary(self):
        return f"Part-time Employee {self.name} is paid hourly."
e1=fulltimeemployee("Sai")
e2=parttimeemployee("Karthik")
print(e1.calculate_salary())
print(e2.calculate_salary())
