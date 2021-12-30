#!/usr/bin/env python3
# *** veja a aula, pois este programa deve ser rodado no terminal ****
import sys
import os

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Faltando argumentos:')
    print('-a', 'Para listar todos os arquivos neste pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios neste pasta', sep='\t')
    sys.exit()


so_arquivos = False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)