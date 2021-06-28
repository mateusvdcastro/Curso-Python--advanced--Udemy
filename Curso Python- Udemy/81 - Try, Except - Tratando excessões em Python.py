# Excessões são erros que ocorrem no programa
try:
    print(a)  # isso gera um erro da classe TypeError
except:
    print(TypeError(NameError))


try:
    print(a)  # isso gera um erro da classe TypeError
except NameError as erro:
    print('Erro', erro)
    print('Erro do desenvolvedor fale com ele')


print('-'*56)


try:
    b = {}
    print(b[1])
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chaves')
except Exception as erro:  # Exception capta qualquer tipo de erro.
    print('Ocorreu um erro inesperado.')
else:  # será executado sempre que o bloco Try não encontrar nenhuma excessão
    print('Seu código foi executado com sucesso!')
finally:  # sempre será executada diferentemente do Else
    print('Finalmente.')

print('Bora continuar...')
