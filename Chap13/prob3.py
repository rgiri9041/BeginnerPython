# A list contain a multiplication table of 7. Write a program ot conver it into vertical sting of same number

table = [str(7*i) for i in range(1,11)]

s = "\n".join(table)
print(s)