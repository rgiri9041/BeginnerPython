# WAP to find the spam message which contain the following keywords "make a lot of money", "buy now", "click this", "subscribe this"

m1 = "make a lot of money"
m2 = "buy now"
m3 = "click this"
m4 = "subscribe this"

message = input("Enter the message: ")

if(m1 in message) or (m2 in message) or (m3 in message) or (m4 in message):
    print("The given message is a spam message")
else:
    print("Message is not a spam. You are safe!!")