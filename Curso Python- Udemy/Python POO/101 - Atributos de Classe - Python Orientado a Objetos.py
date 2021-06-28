class A:
    vc = 123  # vc é um atributo/variável de classe

    def __init__(self):
        # self.vc = 321  # este vc é uma variável de instância
        pass


a1 = A()
a2 = A()
print(a1.vc)
print(a2.vc)
print(A.vc)
A.vc = 321  # assim eu mudo a classe, uma vez q utilizei dela mesma e seu atributo
print(a1.vc)
print(a2.vc)
print(A.vc)
