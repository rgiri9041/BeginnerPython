'''We are going to generate a random number and ask the user to guess it 
if the user guss is higher then program say lower number please, when user guess the lower number then
program say higher number number please and when the user guess exact number then it print congratulations you win
'''



import random

comp = random.randint(1,100)
player = -1
guess = 0
while( player != comp):
    guess+=1
    player = int(input("Enter the number between 1-100: "))
    if(player == comp):
        print("Congratulations!!! You win the game")
        print(f"You guess successfully in {guess} guess")
    
    elif(player < comp):
        print("Please enter a bit higher number")
    
    elif(player > comp):
        print("Please enter a bit lower number")
    
    else:
        print("please enter number between 1-100")
   