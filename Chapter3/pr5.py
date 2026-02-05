# WAP to replace the double space with single spcce in a string 

string = "Hello World  ! I am learning a python  programming language  ."

print("Original string: ", string)
print("Find the double space at index: ", string.find("  "))
print("Replaced string: ", string.replace("  ", " "))