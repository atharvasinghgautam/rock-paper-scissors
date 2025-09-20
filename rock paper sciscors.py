import random
options=["rock","paper","scissors"]
user_choice=input("Choose from rock,paper,scissors: ")
computer_choice=random.choice(options)
print("User choice: ",user_choice)
print("Computer choice: ",computer_choice)
if(computer_choice==user_choice):
    print("It is a tie!")
elif(user_choice=="paper" and computer_choice=="rock"):
    print("You win! Yay! ")
elif(user_choice=="scissors" and computer_choice=="paper"):
    print("You win! Yay!")
elif(user_choice=="rock" and computer_choice=="scissors"):
    print("You win! Yay!")
else:

    print("You loose! Try again!")
