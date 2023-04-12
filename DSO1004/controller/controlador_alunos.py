from model.aluno import Aluno
from view.tela_aluno import TelaAluno


class ControladorAlunos:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__alunos = []
        self.__tela_aluno = TelaAluno(self)

    def inclui_aluno(self):
        matricula = self.__tela_aluno.pega_dados_aluno()
        aluno = Aluno(matricula)
        self.__alunos.append(aluno)

    def altera_aluno(self, aluno):
        pass

    def exclui_aluno(self, aluno):
        pass

    def lista_aluno(self):
        for aluno in self.__alunos:
            self.__tela_aluno.mostra_aluno(aluno.matricula)

    def mostra_menu_alunos(self):
        while True:
            opcao = self.__tela_aluno.mostra_opcoes_aluno()

            if opcao == 1:
                self.inclui_aluno()

            elif opcao == 3:
                self.lista_aluno()
            
            elif opcao == 0:
                break