class Pessoa:
    ano_atual = 2021  # método/atributo de classe

    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):  # get_ano...é um método de instância
        print(self.ano_atual - self.idade)

    @classmethod   # não precisa da instância Self apenas da Classe
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)  # cls retorna a própria classe Pessoa


p1 = Pessoa.por_ano_nascimento('luiz', 1987)  # p1 é a minha instância da classe
# p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
