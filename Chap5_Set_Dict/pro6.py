# Create a empty directory and allow four friend to enter theri favourt language as value and their name as key, assume that the name are unique

friends = {}

name = input("Enter your name:")
language = input("Enter your favourite language: ")
friends.update({name: language})
name = input("Enter your name:")
language = input("Enter your favourite language: ")
friends.update({name: language})
name = input("Enter your name:")
language = input("Enter your favourite language: ")
friends.update({name: language})
name = input("Enter your name:")
language = input("Enter your favourite language: ")
friends.update({name: language})

print(type(friends), friends)