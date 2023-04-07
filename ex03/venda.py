from pacote_viagem import PacoteViagem
from cliente import Cliente

class Venda:

    def __init__(self, codigo: int, cliente: Cliente, descricao: str, pacote: PacoteViagem, quantidade: int):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__descricao = descricao
        self.__pacote = pacote
        self.__quantidade = quantidade

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def nome(self, codigo: int):
        self.__codigo = codigo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def pacote(self):
        return self.__pacote

    @pacote.setter
    def pacote(self, pacote: PacoteViagem):
        self.__pacote = pacote

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    #@property
    #def preco_total(self):
    #    self.preco_total = preco_total
