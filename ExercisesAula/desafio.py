A = input("Nome: ") 
lista = ["Igor","Fernando","Paulo"]
for i in lista:
    if i in A:
        print("Você não é apto para este cadastro")
        quit()
B = int(input("Idade: "))
if B < 18 or B > 30:
    print("Você não pode continuar com o seu cadastro")
    quit()
C = input("Endereço: ")




















