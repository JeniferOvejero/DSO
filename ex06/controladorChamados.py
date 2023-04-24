from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
          self.__chamados = []
          self.__tipochamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
            contador = 0
            for chamado in self.__chamados:
                  if chamado.tipo == tipo:
                        contador += 1
            return contador

    def inclui_chamado(self, data: Date, cliente: Cliente, tecnico: Tecnico, titulo: str, descricao: str, prioridade: int, tipo: TipoChamado) -> Chamado:
        existe = False
        for cha in self.__chamados:
            if data == cha.data and cliente == cha.cliente and tecnico == cha.tecnico and tipo == cha.tipo:
                existe = True
        if not existe:
            if isinstance(data, Date) and isinstance(cliente, Cliente) and isinstance(tecnico, Tecnico) and isinstance(tipo, TipoChamado):
                chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
                self.__chamados.append(chamado)
                return chamado
            else:
                 return TypeError
        else:
             return print("Chamado já existe.")

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        existe = False
        for tip in self.__tipochamados:
            if codigo == tip.codigo:
                existe = True
        if not existe:
            tipoChamado = TipoChamado(codigo, descricao, nome)
            self.__tipochamados.append(tipoChamado)
            return tipoChamado
        else:
            return "Tipo de Chamado já existe." 

    @property
    def tipos_chamados(self):
	    return self.__tipochamados