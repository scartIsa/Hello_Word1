V = float(input())
if int(0 < V < 1000000.00):
    print("NOTAS:")
    print("{} nota(s) de R$ 100.00".format(int(V/100)))
    aux = V % 100
    print("{} nota(s) de R$ 50.00".format(int(aux/50)))
    aux = aux % 50
    print("{} nota(s) de R$ 20.00".format(int(aux/20)))
    aux = aux % 20
    print("{} nota(s) de R$ 10.00".format(int(aux/10)))
    aux = aux % 10
    print("{} nota(s) de R$ 5.00".format(int(aux/5)))
    aux = aux % 5
    print("{} nota(s) de R$ 2.00".format(int(aux/2)))
    aux = aux % 2
    print("MOEDAS:")
    print("{} moeda(s) de R$ 1.00".format(int(aux/1)))
    aux = aux % 1
    print("{} moeda(s) de R$ 0.50".format(int(aux/0.5)))
    aux = aux % 0.5
    print("{} moeda(s) de R$ 0.25".format(int(aux/0.25)))
    aux = aux % 0.25
    print("{} moeda(s) de R$ 0.10".format(int(aux/0.1)))
    aux = aux % 0.1
    print("{} moeda(s) de R$ 0.05".format(int(aux/0.05)))
    aux = aux % 0.05
    print("{} moeda(s) de R$ 0.01".format(int(aux/0.01)))
    aux = aux % 0.01