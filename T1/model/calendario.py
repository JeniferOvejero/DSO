

class Calendario():
    def __init__(self, chave: str):
        self.__chave = chave
        self.__eventos = []
        self.__modificacoes = []

    @property
    def chave(self):
        return self.__chave

    @chave.setter
    def chave(self, chave = str):
        self.chave = chave

    @property
    def eventos(self):
        return self.__eventos

    @property
    def modificacoes(self):
        return self.__modificacoes