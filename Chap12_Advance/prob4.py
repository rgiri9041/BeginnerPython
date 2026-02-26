#WAP to display a/b where a and b are integer. if b ==0 then display infinity by handling the 'zeroDivisonError'

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    result = a/b
    print(result)
except ZeroDivisionError:
    print("Infinity")