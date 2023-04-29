from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahVazioException import OnibusJahVazioException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahDesligadoException import OnibusJahDesligadoException


class Onibus(AbstractOnibus):
    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        super().__init__( capacidade, total_passageiros, ligado)

    # OnibusJahLigadoException
    def ligar(self) -> str:
        if self.ligado:
            raise OnibusJahLigadoException()
        else:
            self.ligado = True

    # OnibusJahDesligadoException
    def desligar(self) -> str:
        if not self.ligado(self):
            raise OnibusJahDesligadoException
        else:
            self.ligado = False

    # OnibusJahCheioException
    def embarca_pessoa(self) -> str:
        if self.total_passageiros >= self.capacidade:
            raise OnibusJahCheioException
        else:
            self.__total_passageiros += 1

    # OnibusJahVazioException
    def desembarca_pessoa(self) -> str:
        if self.total_passageiros == 0:
            raise OnibusJahVazioException
        else:
            self.__total_passageiros -= 1

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    def total_passageiros(self) -> int:
        return self.__total_passageiros

    @property
    def ligado(self) -> bool:
        return self.__ligado

    @capacidade.setter
    def capacidade(self, capacidade: int):
        self.__capacidade = capacidade


