from pessoa import Pessoa
from jogador import Jogador


class Equipe():
    def __init__(self, pais: str, tecnico: Pessoa):
        self.__pais = pais
        self.__tecnico = tecnico
        self.__jogadores = []
        self.__pontos = 0

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, novo: str):
        self.__pais = novo

    @property
    def tecnico(self):
        return self.__tecnico

    @tecnico.setter
    def tecnico(self, novo: Pessoa):
        self.__tecnico = novo

    @property
    def jogadores(self):
        return self.__jogadores

    @jogadores.setter
    def jogadores(self, novo: Jogador):
        self.__jogadores = novo

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, novo: int):
        self.__pontos = novo

    def add_jogador(self, jogador: Jogador):
        if jogador is None:
            return None
        if jogador.nome not in [j.nome for j in self.jogadores]:
            try:
                self.__jogadores.append(jogador)
                print("jogador adicionado: ", jogador)
            except Exception:
                print("error")
        else:
            return None

    def remove_jogador(self, jogador: Jogador):
        if jogador in self.__jogadores:
            self.__jogadores.remove(jogador)
        else:
            return None

    def total_cartoes_time(self):
        total = 0
        for jogador in self.__jogadores:
            total += jogador.numero_cartoes_amarelos
        return total
