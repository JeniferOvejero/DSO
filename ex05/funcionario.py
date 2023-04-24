from abc import ABC, abstractmethod
from usuario_bu import UsuarioBU


class Funcionario(UsuarioBU, ABC):
    @abstractmethod
    def __init__(self, departamento: str, cpf: int, dias_de_emprestimo: int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento: str):
        self.__departamento = departamento

    @abstractmethod
    def emprestar(self, titulo_livro: str):
        return 'do departamento "{0}" pegou emprestado o livro: {1} com {2} dias de prazo'.format(self.departamento, titulo_livro, self.dias_de_emprestimo)

    @abstractmethod
    def devolver(self, titulo_livro: str):
        pass