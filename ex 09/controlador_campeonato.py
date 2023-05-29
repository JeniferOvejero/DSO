from jogo import Jogo
from jogo_duplicado_exception import JogoDuplicadoException


class ControladorCampeonato():
    def __init__(self):
        self.__jogos = []

    @property
    def jogos(self):
        return self.__jogos

    @jogos.setter
    def jogos(self, novo: Jogo):
        self.__jogos = novo

    def busca_jogo_por_numero(self, numero):
        if numero in self.jogos.numero:
            for jogo in self.jogos:
                if numero == jogo.numero:
                    return Jogo
        else:
            return None

    def add_jogo(self, jogo: Jogo):
        if jogo is None:
            return None
        if jogo.numero not in [j.numero for j in self.jogos]:
            try:
                self.__jogos.append(jogo)
            except Exception:
                print("error")
        else:
            raise JogoDuplicadoException()

    def remove_jogo(self, numero):
        if numero in [j.numero for j in self.jogos]:
            for jogo in self.jogos:
                if numero == jogo.numero:
                    self.jogos.remove(jogo)
                    return Jogo
        else:
            return None

    def classificacao_campeonato(self):
        equipes_pontuacao = set()
        for jogo in self.jogos:
            equipes_pontuacao.add(jogo.equipe1)
            equipes_pontuacao.add(jogo.equipe2)
        return sorted(equipes_pontuacao, key=lambda equipe: equipe.pontos,
                      reverse=True)
