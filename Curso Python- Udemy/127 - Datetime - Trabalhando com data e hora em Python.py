# https://docs.python.org/2/library/datetime.html
from datetime import datetime, timedelta

data = datetime(2021, 5, 8, 23, 29, 10)  # --> ano, mês, dia, hora, minuto, segundo
print(data)
print(data.strftime('%d/%m/%Y %H:%M:%S'))  # to see Directive in documentation

data1 = datetime.strptime('08/05/2021', '%d/%m/%Y')
print(data1)  # os zeros são devidos a eu não ter informado hora minuto e segundo

times = datetime.strptime('08/05/2021', '%d/%m/%Y')
print(times.timestamp())

convert = datetime.fromtimestamp(1620442800.0)
print(f'Valor converido do timestamp {convert}')

data2 = datetime.strptime('25/12/2005 18:30:00', '%d/%m/%Y %H:%M:%S')
data2 = data2 + timedelta(days=5, seconds=59)  # time delta é uma variação/periodo do tempo
print(data2.strftime('%d/%m/%Y %H:%M:%S'))

d1 = datetime.strptime('20/12/2005 18:30:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/12/2005 19:30:00', '%d/%m/%Y %H:%M:%S')
timedelta = d2 - d1
print(f'A diferença entre duas datas --> {timedelta}')
print(timedelta.seconds)
print(timedelta.days)
print(d1.time())
