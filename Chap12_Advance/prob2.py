'''WAP to print the third fifth and seventh element of list using enumarate function'''

fruits = ['Apple', 'Banana', 'Orange', 'Guava', 'Grapes', 'Watermellon', 'Papaya', 'Tomato']

for i, fruit in enumerate (fruits):
    if i ==2 or i == 4 or i ==6:
        print(fruit)