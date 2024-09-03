'''
1 fro snake
-1 for water
0 for gun
'''

import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = { "s": 1, "w": -1, "g": 0}
reverseDict = { 1: "Sanke", -1: "Water", 0: "Gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You Loss!")
        
    elif(computer == 1 and you == -1):
        print("You Loss!")

    elif(computer == 1 and you == 0):
        print("You Win!")

    elif(computer == 0 and you == -1):
        print("You win!")

    elif(computer == 0 and you == 1):
        print("You Loss!")
        
    else:
        print("Something went wrong!")