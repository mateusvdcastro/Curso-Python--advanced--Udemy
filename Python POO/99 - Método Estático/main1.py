from random import randint


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

    @staticmethod  # não podemos usar self e cls
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa.por_ano_nascimento('luiz', 1987)  # p1 é a minha instância da classe
# p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())

# os métodos de classe recebem a própria classe como primeiro argumento.
# São muito úteis para fazer algo a nível de classe, como gerar novos objetos
# da classe por exemplo. Os métodos estáticos são praticamente funções simples
# que estão dentro da classe. Uma regra de ouro: use métodos estáticos sempre
# que não precisar usar nada da classe para que ele funcione corretamente, ou
# melhor, sempre que NÃO precisar usar a palavrinha "self" o método pode ser
# estático. Use métodos de classe para manipular objetos e atributos a nível de
# classe, isso pode afetar todas as instâncias da classe em si.
