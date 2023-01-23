from bcolors import bcolors
from style import Dots

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        # __numero é um atributo privado que só pode ser acessado pelo metodo da classe, evitando uma alteração indevida como conta.saldo = 350 sem o uso do metodo deposita. Mas o atributo pode ser acessado por conta._Conta__saldo, mas não é recomendado.
        self.__numero = numero 
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        # Cor no terminal em python
        # https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
        print("\033[40m" + "Extrato" + "\033[0;0m")
        string = f"Saldo de {self.__saldo} do titular {self.__titular}"
        dots = Dots(string)
        dots.estilo_extrato()

    def deposita(self, valor):
        string_d = bcolors.OKGREEN + f"> Depositando {valor} na conta de {self.__titular}" + bcolors.ENDC
        dots = Dots(string_d)
        dots.estilo_sacar_depositar()
        self.__saldo += valor

    def saca(self, valor):
        string_s = bcolors.OKGREEN + f"> Sacando {valor} da conta de {self.__titular}" + bcolors.ENDC
        dots = Dots(string_s)
        dots.estilo_sacar_depositar()
        self.__saldo -= valor

    def transfere(self, valor, destino):
        string_t = bcolors.WARNING + f"> Transferindo {valor} da conta de {self.__titular} para a conta de {destino.__titular}" + bcolors.ENDC
        dots = Dots(string_t)
        dots.estilo_transferir()
        self.saca(valor) # Caso nossa função pedisse um parâmetro "origem" ficaria origem.saca(valor). Mas, isso pode ser substituido por self.saca(valor) eliminando a necessidade de mais um parâmetro.
        destino.deposita(valor)

if __name__ == "__main__":
    conta1 = Conta(123, "Nico", 55.5, 1000.0)
    conta2 = Conta(321, "Flávio", 100.0, 100)

    conta1.deposita(50)

    conta1.extrato()

    conta1.transfere(10, conta2)

    conta2.extrato()


