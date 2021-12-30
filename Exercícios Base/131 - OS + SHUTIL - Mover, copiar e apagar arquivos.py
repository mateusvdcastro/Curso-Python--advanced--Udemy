import os
import shutil  # vai mover e copiar os arquivos

caminho_original = input('Digite o caminho original:')
caminho_novo = input('Digite o caminho em que quer copiar/mover os arquivos:')

try:
    os.mkdir(caminho_novo)  # cria uma pasta nova
except FileExistsError as e:  # para caso o arquivo já tenho sido criado
    print(f'Pasta {caminho_novo} já existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        # if '.doc' in file:                                                       # como filtrar por tipo de arquivo
        # este shutil.move também renomeia arquivos
        shutil.move(old_file_path, new_file_path)                           # movendo um arquivo de um lugar para outro
        # shutil.copy(old_file_path, new_file_path)          # para copiar arquivos de uma pasta para a criada em mkdir
        print(f'Arquivo {file} movido com sucesso.')

        # os.remove(new_file_path)  #como remover um arquivo
