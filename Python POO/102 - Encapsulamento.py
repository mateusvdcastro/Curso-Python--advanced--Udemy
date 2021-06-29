# serve para proteger a sua aplicação

"""
public (self.dados)
protected/ private (self._dados) o underline indica pr outros desenvolvedores não usarem a variável dados fora da classe
private stronger (self.__dados)  dois underlines indicam um reforço neste aviso

Também pode ser usado para métodos como: def __inserir_clientes
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}  # ele é "public" acessível dentro e fora da classe

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})  # isso vai atualizar o meu dicionário

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Mateus')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Daniel')
bd.apaga_clientes(2)
bd.lista_clientes()
print(bd.dados)   # <-------
print(bd.__dados)    # para conseguir rodar esse código usamos o decorador na def dados
bd.lista_clientes()
