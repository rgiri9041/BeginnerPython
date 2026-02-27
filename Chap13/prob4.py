#WAP to filter a list number which are divisible by 5

def divisibleBy(n):
    if(n%5 == 0):
        return True
    return False

a = [10,23,44,45,55,100,222,22222,80]
f = list(filter(divisibleBy, a))
print(f)