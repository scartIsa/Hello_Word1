A = float(input())
if A>=0 and A<=400:
    I = A*0.15
    II = A+I
    III = 15
    print(f"Novo salario: {II:.2f}")
    print(f"Reajuste ganho: {I:.2f}")
    print(f"Em percentual: {III} %")
elif A>=400.01 and A<=800.00:
    I = A*0.12
    II = A+I
    III = 12
    print(f"Novo salario: {II:.2f}")
    print(f"Reajuste ganho: {I:.2f}")
    print(f"Em percentual: {III} %")
elif A>=800.01 and A<=1200.00:
    I = A*0.10
    II = A+I
    III = 10
    print(f"Novo salario: {II:.2f}")
    print(f"Reajuste ganho: {I:.2f}")
    print(f"Em percentual: {III} %")
elif A>=1200.01 and A<=2000.00:
    I = A*0.07
    II = A+I
    III = 7
    print(f"Novo salario: {II:.2f}")
    print(f"Reajuste ganho: {I:.2f}")
    print(f"Em percentual: {III} %")
elif A>2000.00:
    I = A*0.04
    II = A+I
    III = 4
    print(f"Novo salario: {II:.2f}")
    print(f"Reajuste ganho: {I:.2f}")
    print(f"Em percentual: {III} %")