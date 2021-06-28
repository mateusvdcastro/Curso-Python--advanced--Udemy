def converte_numero(valor):
    try:
        valor = int(valor)  # isso esta tentando converter uma str em int e depois em float
        return valor        # para conseguir contornar valores errados do usuário como 'dois', '2.5a'
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:     # se ele não conseguir converter ele retorna None
            pass

while True:
    numero = converte_numero(input('Digite um número: '))
    if numero is not None:
        print(numero * 5)
    else:
        print('Isso não é número')
