# https://ffmpeg.org/download.html
# FFMPEG é um conversor de vídeo

"""
ffmpeg -i "ENTRADA" -i "LEGANDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 -ss 00:00:10 "SAIDA"
"""

import os
import fnmatch  # para descobrir a extensão dos arquivos
import sys

if sys.platform == '':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
present = '-present ultrafast'  # pode escrever "fast" tbm
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'  # vai converter apensas 10 segundos

caminho_origem = r"C:\Users\Asus\Documents\PycharmProjects\Curso Python- Udemy\ffmpeg\Video_normal"
caminho_destino = r"C:\Users\Asus\Documents\PycharmProjects\Curso Python- Udemy\ffmpeg\Video_convertido"

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue

        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        arquivo_saida = f'{caminho_destino}/{nome_arquivo}_NOVO{extensao_arquivo}'

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
            f'{codec_video} {crf} {present} {codec_audio} {bitrate_audio} ' \
            f'{debug} {map_legenda} "{arquivo_saida}"'

        print(comando)
        print()
        print(arquivo)
        print(caminho_completo)
        print(nome_arquivo)
        print(caminho_legenda)

        os.system(comando)
