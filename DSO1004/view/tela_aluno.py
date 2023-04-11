

class TelaAluno:
    def __init__(self, controlador):
        self.__controlador = controlador
    
    def mostra_opcoes_aluno(self):
        print("*"*30)
        print("*** Cadastro Alunos ***")
        print("*"*30)
        print("1 - Incluir Aluno")
        print("2 - Alterar Aluno")
        print("3 - Listar Alunos")
        print("4 - Excluir Aluno")
        print("0 - Sair do Sistema")
        opcao = int(input("Opção:"))
        return opcao
        #if é decisão de fluxo

    def pega_dados_aluno(self):
        matricula = input("Digite a matrícula do aluno: ")
        return matricula

    def lista_alunos(self):
        pass

    def mostra_aluno(self, matricula: str):
        print("Aluno: ", matricula)
