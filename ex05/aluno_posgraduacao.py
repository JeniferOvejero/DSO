from aluno import Aluno


class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese = False

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, x):
        print(x)
        self.__elaborando_tese = x

    def emprestar(self, titulo_livro: str):
        if self.elaborando_tese:
            dias_de_emprestimo = dias_de_emprestimo*2
        return "Aluno de matricula {0} pegou emprestado o livro: {1} com {2} dias de prazo".format(self.matricula, titulo_livro, self.dias_de_emprestimo)

    def devolver(self, titulo_livro: str):
        return "Aluno de matricula {0} devolveu o livro: {1}".format(self.matricula, titulo_livro)
