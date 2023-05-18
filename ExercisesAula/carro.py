class Carro():
    def __init__(self, nome, modelo, cor, ano, buzina):
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.buzina = buzina
    def print(self):
        print(f"O nome é {self.nome} o modelo é {self.modelo} a cor é {self.cor} e o ano é {self.ano}, e tem uma linda {self.buzina}!!!!")

meu_carro = Carro("Fusca", "1500", "rosa", 1975, "buzina")
meu_carro.print()
