class Company:
    company_name = "fisionlabs"   #class
    def __init__(self, emp_name):
        self.emp_name = emp_name   #instance

c1 = Company("karthik")
print(c1.company_name)
print(c1.emp_name)
