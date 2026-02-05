# WAP to find either the student pass or failed as it requires a minumum of 40% and 33% in each subject to pass. 
# Assume 3 subjects and take marks as input from the users.

sub1 = float(input("Enter the marks of subject 1: "))
sub2 = float(input("Enter the marks of second subject: "))
sub3 = float(input("Enter the marks of third subject: "))

Total = sub1+sub2+sub3
percentage = (Total/300) * 100
if(percentage >= 40 and sub1 >=33 and sub2 >= 33 and sub3 >= 33):
    print(f"Congratulations! You have passed the exam with {percentage}")
else:
    print(f"Sorry! You have failed the exam with {percentage}")