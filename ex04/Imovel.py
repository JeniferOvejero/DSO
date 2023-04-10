from Locatario import Locatario
from Locador import Locador
from Mobilia import Mobilia


class Imovel:
    def __init__(self, codigo: int, descricao: str, valor: float, locador:
                 Locador):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        self.__locador = locador
        self.__mobilias = []
        self.__locatarios = []

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

    @property
    def mobilias(self):
        return self.__mobilias

    def incluir_locatario(self, locatario: Locatario):
        loc_ex = False
        if isinstance(locatario, Locatario):
            for loc in self.locatarios:
                if loc.codigo == locatario.codigo:
                    loc_ex = True
                    print('locatario já incluso')
            if not loc_ex:
                self.__locatarios.append(locatario)
                print('incluiu o locatario!')
        else:
            print('error')

    def excluir_locatario(self, codigo_locatario):
        loc_ex = False
        if isinstance(codigo_locatario, int):
            for loc in self.locatarios:
                if loc.codigo == codigo_locatario:
                    loc_ex = True
                    self.__locatarios.remove(loc)
                    print('locatario removido!')
            if not loc_ex:
                print('Locatario não existe')
        else:
            print("error")

    def incluir_mobilia(self, codigo_mobilia: int, descricao_mobilia: str):
        mob_dup = False
        for mob in self.__mobilias:
            if mob.codigo == codigo_mobilia:
                mob_dup = True
                print("Mobilia já atribuida")
                break
        if not mob_dup:
            self.__mobilias.append(Mobilia(codigo_mobilia, descricao_mobilia))
            print('incluído!')

    def excluir_mobilia(self, codigo_mobilia: int):
        mob_ex = False
        for mob in self.__mobilias:
            if mob.codigo == codigo_mobilia:
                mob_ex = True
                self.__mobilias.remove(mob)
                print('Excluído!')
        if not mob_ex:
            print('Mobilia não existe!')

    def find_locatario_by_codigo(self, codigo_locatario: int):
        loc_ex = False
        for loc in self.locatarios:
            if loc.codigo == codigo_locatario:
                loc_ex = True
                return Locatario.nome
                break
        if not loc_ex:
                print("Não existe locatario com esse codigo")
