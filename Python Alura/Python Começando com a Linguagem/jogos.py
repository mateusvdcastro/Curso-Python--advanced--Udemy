
import adivinhacao
import forca

def escolhe_jogo():
    print("*********************************")
    print("**Escolha o jogo que quer jogar!*")
    print("*********************************")


    jogo = int(input("(1) Jogo da Adivinhação (2) Jogo da Forca: "))

    if (jogo == 1):
        print("Jogo da Adivinhação selecionado...")
        adivinhacao.jogar()
    else:
        print("Jogo da Forca selecionado...")
        forca.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()
