from model.evento import Evento
from datetime import date as Date
from model.calendario import Calendario

class Aniversario(Evento):
    def __init__(self, calendario: Calendario, data: Date, titulo: str, descricao: str, chave: str, aniversariante: str):
        super().__init__(calendario, data, titulo, descricao, chave)
        self.__aniversariante = aniversariante

    @property
    def aniversariante(self):
        return self.__aniversariante

    @aniversariante.setter
    def aniversariante(self, aniversariante: str):
        self.__aniversariante = aniversariante