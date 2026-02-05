# WAP to replace the letter

letter = '''Dear <|name|>
Congratulations! You are selected!
<|date|>'''

name = input("Enter your name: ")
date = input("Enter date: ")

letter = letter.replace("<|name|>", name).replace("<|date|>", date)

print(letter)