import random
randomno = random.randint(1,100)
userguess = None
guesses = 0
while (userguess != randomno):
    userguess = int(input("enter your guess:"))
    guesses+=1
    if (userguess == randomno):
        print("wow,you entered right guess")
    else:
        if (userguess>randomno):
            print("you entered it wrong! pls enter smaller number")
        else:
            print("you entered it wrong! pls enter larger number")
print(f"you entered {guesses} to reached right guess")
with open("highscore.txt","r") as f:
    highscore = int(f.read())
if guesses<highscore:
    print("congrates, you break the record")
    with open("highscore.txt","w") as f: 
        f.write(str(guesses)) 
     

