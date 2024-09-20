# hand cricket game 
print("Rules of Game : \n  You have to toss for your Bat or Bowl First")
toss=int(input("Enter Number for toss :"))
if toss%2==0:
    print("Congratulations! Yon Win The toss")
    choice=int(input("Here's a choice for you Enter 1 for BAT first 2 for BOWL first :")) 
    if choice==1:
        print("You choose to BAT first")    
    else:
        print("You choose to BOWL first")
else:
    print("Yon loss The toss ,Computer Win the TOSS and selected to BAT first")



from random import randint
us=0
cs=0
score=0
for i in range(6):
    ui=int(input("Enter your choice \n 1 for one run \n 2  for two run \n 3 for three run \n 4 for four run \n 5 for five run \ 6 for six run : \n "))
    ci=randint(1,6)
    if ui==ci:
        print("OUT , Back to Pavilion")
    else:
        us+=1
        score+=us
        print("total user score",score)