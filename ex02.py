class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def escreveNome(abc):
        print("Olá meu nome é: " + abc.nome)
        
        
nome1 = Pessoa("Miranda", 44)
nome1.escreveNome()

nome1.idade = 35
print(nome1.idade)