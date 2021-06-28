from datetime import datetime


# método é uma função que pertence a uma classe
class Pessoa:  # classes começam com letra maiúscula e não podem ser separadas por nada (PascalCase)
    ano_atual = datetime.now().year  # ano_atual é uma variável da classe
    # ou seja
    print(ano_atual)
# self se refere às instâncias p1/p2 que são os objetos ... no arquivo principal
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo  # estas são variáveis das instâncias(objetos)
        self.falando = falando

    def outro_metodo(self):
        print(self.nome)

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo {alimento}')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
