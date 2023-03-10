valor = int(input("Digite o valor total: "))
desconto = 10
porcentagem = int((10/100) * valor)
todo = {valor - porcentagem}
print(f"O valor total é: R${valor}")
print(f"A porcentagem do desconto é: {desconto}%")
print(f"O valor do desconto é: R${porcentagem}")
print(f"O valor total com desconto é: R${todo}")
