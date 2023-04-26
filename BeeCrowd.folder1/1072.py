N = int(input())
O = 0
I = 0
for F in range(0,N):
    X = int(input())
    if 10 <= X <=20: 
        I += 1
    else:
        O += 1
print(f"{I} in")
print(f"{O} out")
