from arbitro import Arbitro
from equipe import Equipe


class Jogo():
    def __init__(self, numero: int, local: str, arbitro: Arbitro,
                 equipe_1: Equipe, equipe_2: Equipe):
        self.__numero = numero
        self.__local = local
        self.__arbitro = arbitro
        self.__equipe_1 = equipe_1
        self.__equipe_2 = equipe_2
        self.__gols_equipe_1 = 0
        self.__gols_equipe_2 = 0
        self.__finalizado = False

    @property
    def numero(self):
        return self.__numero

    @property
    def local(self):
        return self.__local

    @property
    def arbitro(self):
        return self.__arbitro

    @property
    def equipe_1(self):
        return self.__equipe_1

    @property
    def equipe_2(self):
        return self.__equipe_2

    @property
    def gols_equipe_1(self):
        return self.gols___equipe_1

    @property
    def gols_equipe_2(self):
        return self.gols___equipe_2

    @property
    def finalizado(self):
        return self.__finalizado

    @numero.setter
    def numero(self, novo: int):
        self.__numero = novo

    @local.setter
    def local(self, novo: str):
        self.__local = novo

    @arbitro.setter
    def arbitro(self, novo: Arbitro):
        self.__arbitro = novo

    @equipe_1.setter
    def equipe_1(self, novo: Equipe):
        self.__equipe_1 = novo

    @equipe_2.setter
    def equipe_2(self, novo: Equipe):
        self.__equipe_2 = novo

    @gols_equipe_1.setter
    def gols_equipe_1(self, novo: int):
        self.__gols_equipe_1 = novo

    @gols_equipe_2.setter
    def gols_equipe_2(self, novo: int):
        self.__gols_equipe_2 = novo

    @finalizado.setter
    def finalizado(self, novo: bool):
        self.__finalizado = novo

    def finaliza_jogo(self):
        self.__finalizado = True
        v = self.vencedor()
        if v is None:
            self.__equipe_1.pontos += 1
            self.__equipe_2.pontos += 1
        else:
            v.pontos += 3

    def vencedor(self):
        if self.__gols_equipe_1 > self.__gols_equipe_2:
            return self.__equipe_1
        if self.__gols_equipe_2 > self.__gols_equipe_1:
            return self.__equipe_2
        else:
            return None

    def pontos_vencedor(self):
        v = self.vencedor()
        return v.pontos
