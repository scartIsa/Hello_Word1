Peso = float(input("Quantos Kg você pesa? "))
Altura = float(input("E qual sua altura? em metros por favor "))
IMC = Peso / (Altura * Altura)
print(f"O seu indice de massa corporal é {IMC}")
if IMC < 18.5:
    print("E você esta baixo do peso")
elif IMC >= 18.6 and IMC <= 24.9:
    print("E você é saudável")
elif IMC >= 25 and IMC <= 29.9:
    print("E você tem peso em excesso")
elif IMC >= 30 and IMC <= 34.9:
    print("E você tem obesidade grau I")
elif IMC >= 35 and IMC <= 39.9:
    print("E você obesidade grau II/severa")
elif IMC >= 40:
    print("E você tem obesidade grau III/morbida")