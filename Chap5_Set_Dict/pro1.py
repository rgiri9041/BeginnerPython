# WAP to create a directory of nepali word with menaing in english  

nepali_dict = {
    "ghar": "house",
    "paani": "water",
    "mitra": "friend",
    "khana": "food",
    "pustak":"book"
}

print(f"The meaning of nepali words in english are {nepali_dict}")
words = input("enter nepali words to know english meaning: ")
print(nepali_dict[words])