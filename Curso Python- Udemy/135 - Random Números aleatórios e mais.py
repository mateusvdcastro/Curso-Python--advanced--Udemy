import random
import string

# Gera um número inteiro entra A e B
# inteiro = random.randint(10, 20)

# Gerar um número aleatório usando a função range()
inteiro = random.randrange(900, 1000, 10)  # início, fim, passo

# Gera um número de ponto flutuante entra A e B
# flutuante = random.uniform(10, 20)

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()

lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

# Seleciona aleatóriamente valores de uma lista
sorteio = random.sample(lista, 2)  # sorteia 2 itens diferentes na lista
# sorteio = random.choices(lista, k=2)  # sortear 2 itens aleatórios de uma lista
# sorteio = random.choice(lista)  # vai escolher um nome na lista aleatóriamente

# Embaralha a lista
random.shuffle(lista)

# Gera senha aleatória
letras = string.ascii_letters  # retorna maiúsculas e minúsculas
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)
