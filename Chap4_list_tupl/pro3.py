#Check touple cannot be changed in python

my_touple = (1, 2, "Harry", "Potter")
print(my_touple)
my_touple[2] = "Raj" # This is wrong and will give error because touple is immutable 

print(my_touple)