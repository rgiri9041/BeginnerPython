# WAP to remove the word from the list using function 

def rem(l, word):
    if word in l:
        l.remove(word)
        return l
    else:
        return "Word not found in the list"
list1 = ['apple', 'banana', 'cherry', 'date']
words = input("Enter the word to be removed: ")
print(f"the updated list is: {rem(list1, words)}")