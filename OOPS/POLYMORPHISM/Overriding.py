class Employee:
    def role(self):
        return "General Employee"
class Developer(Employee):
    def role(self):
        return "Software Developer" #overriding
dev = Developer()
print(dev.role())
emp=Employee()
