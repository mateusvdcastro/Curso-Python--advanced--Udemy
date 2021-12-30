string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
l1 = [string[i: i + n] for i in range(0, len(string), n)]
print(l1)
form = '.'.join(l1)
print(form)
print('-'*40)
# uma explicação para entender melhor o exercício
lexp = [f'string[{i}: {i + n}]' for i in range(0, len(string), n)]
print(lexp)
