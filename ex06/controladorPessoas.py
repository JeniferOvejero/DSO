from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
         return self.__tecnicos

    def inclui_cliente(self, codigo :int, nome :str) -> Cliente:
        existe = False
        for cli in self.clientes:
            if codigo == cli.codigo:
                existe = True
        if not existe:
            novoCliente = Cliente(nome, codigo)
            self.__clientes.append(novoCliente)
            return novoCliente
        else:
            return "Cliente já registrado."

    def inclui_tecnico(self, codigo :int, nome :str) -> Tecnico:
        existe = False
        for tec in self.tecnicos:
            if codigo == tec.codigo:
                existe = True
        if not existe:
            novoTecnico = Tecnico(nome, codigo)
            self.__tecnicos.append(novoTecnico)
            return novoTecnico
        else:
            return "tecnico já registrado."