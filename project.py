#stone paper scissor game
from random import randint
us=0
cs=0
for i in range(5):
    ui=int(input("Enter your choice \n 1 of stone \n 2 for paper \n 3 for scissor : \n "))
    ci=randint(1,3)
    if ui==1:
        if ci==1:
            print("Draw computer choice is stone")
        elif ci==2:
            cs+=1
            print("computer win and choice is paper")
        else:
            us+=1
            print("You win computer choice is scissor")

    elif ui==2:
         if ci==2:
             print("Draw computer choice is paper")
         elif ci==3:
            cs+=1
            print("computer win and choice is scissor")
         else:
            us+=1
            print("You win computer choice is stone")

    elif ui==3:
        if ci==3:
            print("Draw computer choice is scissor")
        elif ci==1:
            cs+=1
            print("Computer win choice is stone")
        else:
            us+=1
            print("You win computer choice is paper")
if cs>us:
    print("computer win with",cs-us)
else:
    print("You win with",us-cs)
