class Pessoa:
    olhos = 2 #aqui foi criado um atributo de classe. Trata-se de uma técnica para economizar espaço na memória.
    #como é um valor default para todas as pessoa, não é necessário criar dentro do método __init__.


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

    #criação de um atributo dinâmico, que não consta do __init__

    Edmar.sobrenome = 'cavalcante'
    print(Edmar.sobrenome)
    del Edmar.sobrenome
    # criei e depois removi um atributo dinâmico sobrenome para Edmar

    # atributo especial que permite conferir todos os atributos de instância
    # __dict__
    print(Edmar.__dict__)
    print(Pai.__dict__)

    #Nesse tópico você vai ver como economizar memória
    # com os atributos de dados, também chamados de atributos padrão (default) em Python.

    print(Pessoa.olhos) #acesso o atributo olhos diretamente da classe. Isso só é possível porque o atributo olhos é de
    # classe.
    print(Edmar.olhos) # acesso o atributo olhos também através do objeto.

# relembrado - foram vistos 3 tipos de atributos 1- de instância (método __init__, 2- atributo dinâmico e
# 3- atributo de classe