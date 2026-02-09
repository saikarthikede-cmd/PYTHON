def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student_details(name="Sai", age=22, course="Python")
