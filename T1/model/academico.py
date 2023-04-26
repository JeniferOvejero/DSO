from model.evento import Evento
from datetime import date as Date
from model.calendario import Calendario

class Academico(Evento):
    def __init__(self, calendario: Calendario, data: Date, titulo: str, descricao: str, chave: str, materia: str, professor: str):
        super().__init__(calendario, data, titulo, descricao, chave)
        self.__materia = materia
        self.__professor = professor

    @property
    def materia(self):
        return self.__materia

    @materia.setter
    def materia(self, materia: str):
        self.__materia = materia

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor: str):
        self.__professor = professor