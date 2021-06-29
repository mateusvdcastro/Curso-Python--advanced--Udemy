class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclass = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclass} falando...')


class Clientes(Pessoa):
    def comprar(self):
        print(f'{self.nomeclass} comprando...')

    def falar(self):
        print(f'{self.nomeclass} falando...')


class ClienteVIP(Clientes):
    def falar(self):  # note que há duas def falar, o python avisou com aquele simplo azul e vermelho,
        print('Outra coisa qualquer')  # ele irá executar o falar desta def aqui e não o da superclasse Pessoa
        Pessoa.falar(self)  # irá executar agora o falar da superclasse Pessoa
        super().falar()  # super(), irá subir a herança e executará a def falar da Classe Clientes



class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclass} estudando...')


