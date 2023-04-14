from funcionario import Funcionario


class Professor(Funcionario):
    def __init__(self, departamento: str, cpf: int):
        super().__init__(departamento, cpf, dias_de_emprestimo = 20)
    
    def emprestar(self, titulo_livro: str):
        return "Professor do departamento {departamento} pegou emprestado o livro: {titulo_do_livro} com {dias_de_emprestimo} dias de prazo".format(self.__departamento, titulo_livro, self.__dias_de_emprestimo)

    def devolver(self, titulo_livro: str):
        return "Professor do departamento {departamento} devolveu o livro: {titulo_do_livro}".format(self.__departamento, titulo_livro)
