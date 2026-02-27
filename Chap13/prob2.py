#WAP to enter name, phone number and  marks of student in the format like :
'''The name of student is Hari his mark is 29 and his phone number is 999999999'''

name = input("Enter the name of student: ")
mark = int(input("Enter the mark of student: "))
phoneNo = int(input("Enter the phone number of student: "))

s = "The name of student is {} his mark is {} and his phone number is {}".format(name, mark, phoneNo)
print(s)