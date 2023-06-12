import pickle
from clienteDAO import ClienteDAO
from cliente import Cliente

# cliente1 = Cliente(123, 'Jean')
# cliente2 = Cliente(456, 'Jenny')
# cliente3 = Cliente(789, 'José')

# clientes_dao = ClienteDAO()

# clientes_dao.add(cliente1)
# clientes_dao.add(cliente2)
# clientes_dao.add(cliente3)

for cliente in clientes_dao.get__all():
    print(cliente.codigo, cliente.nome)