from abc import abstractmethod, ABC


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def inserir_conta(self, conta):
        self.conta = conta


class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia} '
              f'Conta: {self.numero} '
              f'Saldo: {self.saldo} ')

    @abstractmethod
    def sacar(self, valor): pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo Insuficiente')
            return

        self.saldo -= valor
        self.detalhes()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_clientes(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return None

        if cliente.conta not in self.contas:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True


if __name__ == '__main__':
    banco = Banco()
    cliente1 = Cliente('Mateus', 30)
    cliente2 = Cliente('Davi', 18)
    cliente3 = Cliente('João', 58)

    conta1 = ContaPoupanca(1111, 528956, 0)
    conta2 = ContaPoupanca(3333, 124956, 0)
    conta3 = ContaCorrente(2222, 285956, 0)

    cliente1.inserir_conta(conta1)
    cliente2.inserir_conta(conta2)
    cliente3.inserir_conta(conta3)

    banco.inserir_clientes(cliente1)
    banco.inserir_conta(conta1)
    banco.inserir_clientes(cliente2)
    banco.inserir_conta(conta2)
    banco.inserir_clientes(cliente3)
    banco.inserir_conta(conta3)

    if banco.autenticar(cliente1):
        cliente1.conta.depositar(230)
        cliente1.conta.sacar(150)
    else:
        print('Cliente não autenticado.')

    print('############################')

    if banco.autenticar(cliente2):
        cliente2.conta.depositar(9850)
        cliente2.conta.sacar(2500)
    else:
        print('Cliente não autenticado.')

    print('############################')

    if banco.autenticar(cliente3):
        cliente3.conta.depositar(100)
        cliente3.conta.sacar(200)  # valores de saque maiores que o limite retornam (saldo insuficiente)
    else:
        print('Cliente não autenticado.')
