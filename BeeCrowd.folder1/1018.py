A = int(input())
if int(0 < A < 1000000):
    print(f"{A}")
    print("{} nota(s) de R$ 100,00".format(int(A/100)))
    aux = A % 100
    print("{} nota(s) de R$ 50,00".format(int(aux/50)))
    aux = aux % 50
    print("{} nota(s) de R$ 20,00".format(int(aux/20)))
    aux = aux % 20
    print("{} nota(s) de R$ 10,00".format(int(aux/10)))
    aux = aux % 10
    print("{} nota(s) de R$ 5,00".format(int(aux/5)))
    aux = aux % 5
    print("{} nota(s) de R$ 2,00".format(int(aux/2)))
    aux = aux % 2
    print("{} nota(s) de R$ 1,00".format(int(aux/1)))