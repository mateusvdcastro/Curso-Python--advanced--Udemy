from random import randint


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


    num_aleatorio = randint(1, 100)

    pontos = 1000
    total_de_tentativas = 3
    rodada = 1
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while (rodada <= total_de_tentativas):
        
        print("Tentativa", rodada, "de", total_de_tentativas)

        num_chutado = int(input('Chute um número de 1 a 100: '))

        if (num_chutado < 1 or num_chutado > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue  # Continue pula para a próx iteração

        if (num_chutado == num_aleatorio):
            print(f"Você acertou!!! Chutou {num_chutado} e era {num_aleatorio}. Terminou com {pontos} pontos.")
            break
        elif (num_chutado > num_aleatorio):
                print("Você errou! O seu chute foi maior que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(num_aleatorio, pontos))
        elif (num_chutado < num_aleatorio):
            print("Você errou! O seu chute foi menor que o número secreto.")
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {} pontos.".format(num_aleatorio, pontos))
        pontos_perdidos = abs(num_aleatorio - num_chutado)
        pontos = pontos - pontos_perdidos
        # else:
        #     print(f"Você errou :( Chutou {num_chutado} e era {num_aleatorio}.")

        rodada += 1


    print(f"\nFim do jogo!")


if (__name__ == "__main__"):
    jogar()
