from bcolors import bcolors

"""
Classe para estilizar a impressão de strings no terminal.
"""

class Dots:
    def __init__(self, string):
        self.__string = string

    def estilo_transferir(self):
        print(bcolors.WARNING + "-"*len(self.__string) + bcolors.ENDC)
        print(bcolors.WARNING + self.__string + bcolors.ENDC)
        print(bcolors.WARNING + "-"*len(self.__string) + bcolors.ENDC)

    def estilo_sacar_depositar(self):
        print(bcolors.OKGREEN + "*"*len(self.__string) + bcolors.ENDC)
        print(bcolors.OKGREEN + self.__string + bcolors.ENDC)
        print(bcolors.OKGREEN + "*"*len(self.__string) + bcolors.ENDC)
    
    def estilo_extrato(self):
        print(bcolors.FUNDOPRETO + "*"*len(self.__string) + bcolors.ENDC)
        print(bcolors.FUNDOPRETO + self.__string + bcolors.ENDC)
        print(bcolors.FUNDOPRETO + "*"*len(self.__string) + bcolors.ENDC)
