
#Basic conditions
#If statement
if 5 > 3:
    print("5 is greater than 3")
    print("This is inside the if block")

print("This is outside the if block")

#else statement and elif statement
x = 10
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")  

#elif statement
y = 15
if y < 10:
    print("y is less than 10")
elif y == 10:
    print("y is equal to 10")
else:
    print("y is greater than 10")

# Compare marks for students
Mina_marks = 50
Student_marks = float(input("Enter the marks of the student: "))

if Student_marks >= Mina_marks:
    print("The student has passed the exam.")
else:
    print("The student has failed the exam.")

