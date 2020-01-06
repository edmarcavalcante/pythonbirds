class Pessoa:
    def __init__(self, nome, idade=35, *filhos):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimenrar(self): #isso é um método. Método não passa de uma função no corpo de uma classe
        return 'Olá'

if __name__=='__main__':
    Edmar = Pessoa('Edmar',20)
    Pai = Pessoa('Evaldo', 55,Edmar)

    print(Pessoa.cumprimenrar(Edmar))
    print(Edmar.cumprimenrar()) # essa é a forma correta de chamar um objeto junto com um método
    print(Edmar.nome)
    print(Edmar.idade)
    print(Pai.filhos)
    for filho in Pai.filhos:
        print(filho.nome)




