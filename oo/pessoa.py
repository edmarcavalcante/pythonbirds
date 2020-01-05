class Pessoa:
    def __init__(self, nome, idade=35):
        self.idade = idade
        self.nome = nome


    def cumprimenrar(self): #isso é um método. Método não passa de uma função no corpo de uma classe
        return 'Olá'

if __name__=='__main__':
    p = Pessoa('Edmar',20)

    print(Pessoa.cumprimenrar(p))
    print(p.cumprimenrar()) # essa é a forma correta de chamar um objeto junto com um método
    print(p.nome)
    print(p.idade)



