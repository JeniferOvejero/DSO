from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):

    def __init__(self):
        self.__onibus = None

    def ligar(self) -> str:
        self.__onibus.ligar()
        return "Onibus Ligado"

    def desligar(self) -> str:
        self.__onibus.desligar()
        return "Onibus Desligado"

    def embarca_pessoa(self) -> str:
        self.__onibus.embarca_pessoa()
        return "Pessoa embarcada"

    def desembarca_pessoa(self) -> str:
        self.__onibus.desembarca_pessoa()
        return "Pessoa desembarcada"

    @property
    def onibus(self) -> Onibus:
        return self.__onibus

    def inicializar_onibus(self, capacidade: int, total_passageiros: int,
                           ligado: bool):
        if Onibus.ligado:
            if (isinstance(capacidade, int)
                    and isinstance(total_passageiros, int)
                    and isinstance(ligado, bool) and capacidade >= 0
                    and total_passageiros >= 0
                    and total_passageiros <= capacidade):
                self.__onibus = Onibus(capacidade, total_passageiros, ligado)
            else:
                raise ComandoInvalidoException
