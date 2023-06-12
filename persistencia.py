import pickle

class Cliente():
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

# cliente1 = Cliente(123, 'Jean')
# cliente2 = Cliente(456, 'Jenny')
# cliente3 = Cliente(789, 'José')

# clientes = {}

# clientes[cliente1.codigo] = cliente1
# clientes[cliente2.codigo] = cliente2
# clientes[cliente3.codigo] = cliente3

# arq_clientes = open('clientes.pkl', 'wb') #wb se o arq nao existe ele cria o arquivo diefrente do rb

# pickle.dump(clientes, arq_clientes)
# print("a")

arq_clientes = open('clientes.pkl', 'rb')
clientes = pickle.load(arq_clientes)

for chave, cliente in clientes.items():
    print(chave, cliente.nome)