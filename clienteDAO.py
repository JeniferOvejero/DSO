from DAO_abstract import DAO
from cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if (isinstance(cliente.codigo, int)) and (cliente is not None) \
                and isinstance(cliente, Cliente):
            super().add(cliente.codigo, cliente)

    def det(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)