# WAP to find the sum of first n natural number 
n = int(input("Enter the number: "))
sum = 0
for i in range (1, n+1):
    sum += i
    print(f"The sum of firt {i} natural number is {sum}")
print("\n print using while loop \n")
# using while loop
n = int(input("Enter the number: "))
summ = 0
i = 1
while i<=n:
    summ += i
    print(f"The sum of first {i} natural number is {summ}")
    i+=1