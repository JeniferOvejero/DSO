from controller.controlador_alunos import ControladorAlunos
from view.tela_principal import TelaPrincipal


class ControladorPrincipal: #instancia os outros controladores
    def __init__(self):
        self.__controlador_aluno = ControladorAlunos(self)
        self.__tela_principal = TelaPrincipal(self)

    def inicia_sistema(self):
        while True:
            opcao = self.__tela_principal.menu_principal()

            if opcao == 1:
                self.__controlador_aluno.mostra_menu_alunos()
            elif opcao == 0:
                break