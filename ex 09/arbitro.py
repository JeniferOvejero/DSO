from pessoa import Pessoa


class Arbitro(Pessoa):
    def __init__(self, nome: str, telefone: str, nacionalidade: str,
                 numero_jogos: int):
        super().__init__(nome, telefone)
        self.__nacionalidade = nacionalidade
        self.__numero_jogos = numero_jogos

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @property
    def numero_jogos(self):
        return self.__numero_jogos

    @nacionalidade.setter
    def nacionalidade(self, novo):
        self.__nacionalidade = novo

    @numero_jogos.setter
    def numero_jogos(self, novo):
        self.__numero_jogos = novo
