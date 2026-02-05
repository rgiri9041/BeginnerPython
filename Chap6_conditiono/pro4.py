# WAP to find the weather the given username ccontain atleast 10 characters or not 

username = input("Enter the username: ")
if(len(username) >= 10):
    print("The username is valid and contain atleast 10 characters")
else:
    print("The username is invalide and doesn't contain 10 characters")
    