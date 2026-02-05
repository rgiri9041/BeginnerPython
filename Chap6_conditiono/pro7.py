# WAP to calculate the grade of a student for the following criteria: 

# 90-100: A+
# 80-89: A
# 70-79: B+
# 60-69: B
# 50-59: C+
# 40-49: C
# 33-39: D

marks = float(input("Enter the marks of the student: "))

if(marks < 0 or marks > 100):
    print("Invalid marks! Please enter the marks between 0 and 100")

if(marks >= 90 and marks <=100):
    print("Congratulations! You got A+ grade")
elif(marks >= 80 and marks < 90):
    print("Congratulations! You got A grade")
elif(marks >= 70 and marks < 80):
    print("Congratulations You got B+ grade")
elif(marks >= 60 and marks < 70):
    print("Congratulations! You got B grade")
elif(marks >= 50 and marks < 60):
    print("You got C+ grade")
elif(marks >= 40 and marks < 50):
    print("You got C grade")    
elif(marks >= 33 and marks < 40):
    print("You got D grade")    
else:
    print("Sorry! You are failed in the exam")