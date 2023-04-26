from model.evento import Evento
from datetime import date as Date
from model.calendario import Calendario

class Social(Evento):
    def __init__(self, calendario: Calendario, data: Date, titulo: str, descricao: str, chave: str, local: str):
        super().__init__(calendario, data, titulo, descricao, chave)
        self.__local = local

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local: str):
        self.__local = local