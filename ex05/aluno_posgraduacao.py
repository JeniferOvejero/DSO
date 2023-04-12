from aluno import Aluno


class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(matricula, cpf, dias_de_emprestimo)
        self.__elaborando_tese = False

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese: bool):
        self.__elaborando_tese = elaborando_tese

    def emprestar(self, titulo_livro: str):
        return "Aluno de matricula {matricula} pegou emprestado o livro: {titulo_do_livro} com {dias_de_emprestimo} dias de prazo".format(self.__matricula, titulo_livro, self.__dias_de_emprestimo)

    def devolver(self, titulo_livro: str):
        return "Aluno de matricula {matricula} devolveu o livro: {titulo_do_livro}".format(self.__matricula, titulo_livro)