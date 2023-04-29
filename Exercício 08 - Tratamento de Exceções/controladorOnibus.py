from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):

    def __init__(self):
        self.onibus = None
   
    def ligar(self) -> str:
        self.onibus.ligar()
        return "Onibus Ligado"

    def desligar(self) -> str:
        self.onibus.desligar()
        return "Onibus Desligado"

    '''
    Um passageiro entra no onibus. Se nao for possivel permitir o embarque, dispara a excecao
    @return Mensagem informando o que ocorreu com o onibus 
    @throws OnibusJahCheioException 
    '''
    def embarca_pessoa(self) -> str:
        self.onibus.embarca_pessoa()
        return "Pessoa embarcada"

    def desembarca_pessoa(self) -> str:
        self.onibus.desembarca_pessoa()
        return "Pessoa desembarcada"

    @property
    def onibus(self) -> Onibus:
        return self.onibus

    def inicializar_onibus(self, capacidade: int, total_passageiros: int, ligado: bool):
        self.onibus = Onibus(capacidade, total_passageiros, ligado)
