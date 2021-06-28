from vendas.calc_preços import aumento, desconto
from vendas.Formato.preço import real

preco = 49.90
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = desconto(preco, 50, formata=True)
print(preco_com_reducao)

print(real(50))
