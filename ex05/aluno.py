from abc import abstractmethod
from usuario_bu import UsuarioBU


class Aluno(UsuarioBU):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: str):
        self.__matricula = matricula

    @abstractmethod
    def emprestar(self, titulo_livro: str):
        pass

    @abstractmethod
    def devolver(self, titulo_livro: str):
        pass