score = int(input("Enter score: "))
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >=40:
    grade = "C"
elif score<40:
    grade = "Fail"
else:
    grade="AB"
print("Grade:", grade)
