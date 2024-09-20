
def search(a,x,side="left"):
    if side=="left":
        for i in range(len(a)):
            if a[i]==r:
                return i 
    elif side=="right":
        for i in range(len(a)-1,-1,-1):
            if (a[i]==x):
                return i
