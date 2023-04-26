X = int(input())
Y = int(input())
Z = 0
if Y < X:
    aux = X
    X = Y
    Y = aux - 1
while X < Y:
    X = X + 1
    if X % 2 != 0:
        Z = Z + X
print(Z)
