

class TelaPrincipal:
    def __init__(self, controlador_principal): #não coloca o tipo para evitar problema de importação circular
        self.__controlador_principal = controlador_principal
    
    def menu_principal(self):
        print("*"*30)
        print("*** Sistema Alunos ***")
        print("*"*30)
        print("1 - Alunos")
        print("2 - Professores")
        print("3 - Boletins")
        print("0 - Sair do Sistema")
        opcao = int(input("Opção:"))
        return opcao