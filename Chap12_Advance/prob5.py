#Store the multiplication table generated in problem 3 in file name table.txt

n = int(input("Enter a number: "))

table = [n*i for i in range(1,11)]

with open("table.txt", "a") as f:
    f.write(f"The table of {n} is: {str(table)} \n")
