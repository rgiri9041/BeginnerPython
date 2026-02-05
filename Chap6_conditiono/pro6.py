# WAP to find whether the given name is present in the list of not 

name = ["Raj", "Hari", "Sita", "Gita", "Rina"]

user_name = input("Enter the name: ")
if user_name in name:
    print(f"{user_name} is present in the list")
else:
    print(f"{user_name} is not present in the list. ")
    