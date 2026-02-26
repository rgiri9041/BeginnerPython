'''WAP to list comprehenson print a list which contain the multiplication table of user entered number'''

num = int(input("Enter a number: "))

table = [num*i for i in range(1,11)]
print(table)