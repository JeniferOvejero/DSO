from abc import ABC, abstractclassmethod
from datetime import date as Date
from model.calendario import Calendario


class Evento(ABC):
    @abstractclassmethod
    def __init__(self, calendario: Calendario, data: Date, titulo: str, descricao: str, chave: str):
        self.__calendario = calendario
        self.__data = data
        self.__titulo = titulo
        self.__descricao = descricao
        self.__chave = chave
        self.__modificacoes = []

    @property
    def calendario(self):
        return self.__calendario

    @calendario.setter
    def calendario(self, calendario = Calendario):
        self.__calendario = calendario

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data = Date):
        self.__data = data

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo = str):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao = str):
        self.descricao = descricao

    @property
    def chave(self):
        return self.__chave

    @chave.setter
    def chave(self, chave = str):
        self.chave = chave

    @property
    def modificacoes(self):
        return self.__modificacoes