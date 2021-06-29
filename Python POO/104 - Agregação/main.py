from classes import CarrinhoDeCompras, Produtos

carrinho = CarrinhoDeCompras()
p1 = Produtos('Camiseta', 50)
p2 = Produtos('Iphone', 10000)
p3 = Produtos('Caneca', 45)
p4 = Produtos('Playstation', 3589)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p4)

carrinho.lista_produto()
print(carrinho.soma_total())

