x=int(input("Enter your number"))
if x>1:
    for i in range(2,(x//2)+1):
        if (x%i) ==0:
            print("not prime number")
            break
        else:
            print("prime")
            break
else:
    print("is not a prime number")
