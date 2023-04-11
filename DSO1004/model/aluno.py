

class Aluno:
    def __init__(self, matricula: str):
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: str):
        self.__matricula = matricula
