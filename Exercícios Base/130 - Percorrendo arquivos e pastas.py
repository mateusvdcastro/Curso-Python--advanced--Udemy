import os

path_research = input('Digite um caminho dos arquivos do seu PC: ')
find_by = input('Encontrar arquivos com quais nomes/caracteres?: ')


def format_lenght(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        text = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        text = 'K'
    elif tamanho < giga:
        tamanho /= mega
        text = 'M'
    elif tamanho < tera:
        tamanho /= giga
        text = 'G'
    elif tamanho < peta:
        tamanho /= tera
        text = 'T'
    else:
        tamanho /= peta
        text = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{text}'.replace('.', ',')


count = 0
for root, directorys, files in os.walk(path_research):
    for file in files:
        if find_by in file:
            try:
                count += 1
                full_path = os.path.join(root, file)
                name_file, extent_file = os.path.splitext(file)
                lenght = os.path.getsize(full_path)
                print()
                print('Encontrei o arquivo', file)
                print('Caminho do arquivo', full_path)
                print('Nome do Arquivo:', name_file)
                print('Extensão:', extent_file)
                print('Tamanho:', lenght)
                print('Tamanho formatado:', format_lenght(lenght))
            except PermissionError as e:
                print("Sem permissão neste arquivo.")
            except FileNotFoundError as e:
                print("Arquivo não encontrado")
            except Exception as e:
                print("Erro desconhecido")

print()
print(f'{count} arquivo(s) encontrado(s).')
