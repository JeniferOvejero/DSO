from funcionario import Funcionario


class Professor(Funcionario):
    def __init__(self, departamento: str, cpf: int):
        super().__init__(departamento, cpf, dias_de_emprestimo = 20)
    
    def emprestar(self, titulo_livro: str):
        return 'Professor '

    def devolver(self, titulo_livro: str):
        return 'Professor do departamento "{0}" devolveu o livro: {1}'.format(self.departamento, titulo_livro)
