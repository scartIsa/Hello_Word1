N = int(input())
for J in range(N):
    X = int(input())
    if(X<0):
        if(X % 2 == 0):
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    elif(X>0):
        if(X % 2 == 0):
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif(X==0):
        print("NULL")