"""
To better explain how conditionals work,
grade.py will allow for a grade(int) to
be entered as input ,it will then take
that grade and assign a letter grade to it.

A = 90 - 100
B = 80 - 89
C = 70 - 79
D = 60 - 69
F = 50 - 59
"""

score = int(input("Enter your grade? "))

if score >= 90 or score == 100:
    print("Your grade is an A ")
elif score >= 80 or score == 89:
    print("Your grade is a B ")
elif score >= 70 or score == 79:
    print("Your grade is a C")
elif score >= 60 or score == 69:
    print("Your grade is a D")
else:
    print("Your score is a F")