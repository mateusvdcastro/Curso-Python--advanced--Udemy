class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('A', '@')

    # Getter  # o getter obtém um valor (ele é um decorador)
    @property
    def preco(self):
        return self._preco

    # Setter  # seter configura um valor
    # sempre que executar a função desconto, ela antes passa por este
    # setter e configura o preço
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):  # str é uma instância da classe str
            valor = float(valor.replace('R$', ''))
        self._preco = valor


p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$15') # Aqui eu informei uma STR que me entregaria um erro, com o getter e setter nós
p2.desconto(10)                # contornamos o erro
print(p2.nome, p2.preco)
