# https://docs.python.org/2/library/datetime.html
from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, '')
setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))  # pegando o nº do mês atual
print(mes_atual)
ultimo_dia_mes = mdays[mes_atual]
print(ultimo_dia_mes)

# sábado, 13 de julho de 2019
formatacao1 = dt.strftime('%A, %d de %B de %Y')
# 13/07/2019 11:21:20
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1, formatacao2)
print(mes_atual, mdays[mes_atual])