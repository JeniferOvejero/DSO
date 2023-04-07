from Locatario import Locatario
from Locador import Locador
from Mobilia import Mobilia

class Imovel:
    def __init__(self, codigo: int, descricao: str, valor: float, locador: Locador):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        self.__locador = Locador
        self.__mobilia = []

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def locador(self):
        return self.__locador
    @locador.setter
    def locador(self, locador: Locador):
        self.__locador = locador
    
    @property
    def locatarios(self):
        return self.__locatarios

    def incluir_locatario(self, locatario: Locatario):
        if isinstance(locatario, Locatario) and locatario not in self.__locatarios:
            self.__locatarios.append(locatario)

    def excluir_locatario(self, locatario: Locatario):
        if isinstance(locatario, Locatario) and locatario in self.__locatarios:
            self.__locatarios.remove(locatario)

#    def incluir_mobilia(self, codigo_mobilia: int, descricao_mobilia: str):
#        if isinstance(codigo_mobilia, int) and codigo_mobilia not in self.__mobilias and isinstance(descricao_mobilia, str):
            
            

#    def excluir_mobilia(self, codigo_mobilia: int):
        

    def find_locatario_by_codigo(codigo_locatario: int):
        for loc in Locatario.codigo:
            if Locatario.codigo == codigo_locatario:
                return Locatario.nome
                break
            else:
                print("Não existe locatario com esse codigo")
