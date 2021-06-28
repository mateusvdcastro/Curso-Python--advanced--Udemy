while True:
    cpf_list = []
    cpf_list2 = []
    cpf = str(input('Digite um Cpf: '))
    # cpf = '168.995.350-09'
    pdig = cpf[:-3].replace('.', '')
    count = 10
    for l in pdig:
        p = int(l) * count
        cpf_list.append(p)
        print(f'{l} * {count} = {p}')
        count -= 1
    som = sum(cpf_list)
    calc = 11 - (som % 11)
    if som > 9:
        digito = 0
    elif som <= 9:
        digito = som
    pdig2 = pdig + f'{digito}'
    for l2 in pdig2:
        p2 = int(l2) * calc
        cpf_list2.append(p2)
        print(f'{l2} * {calc} = {p2}')
        calc -= 1
    som1 = sum(cpf_list2)
    calc = 11 - (som1 % 11)
    novo_cpf = pdig2 + f'{calc}'
    cpf = cpf.replace('.', '').replace('-', '')
    if cpf == novo_cpf:
        print('Este CPF é válido')
    else:
        print('Este CPF é inválido')
