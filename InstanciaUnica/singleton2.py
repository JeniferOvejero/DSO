

class Controlador():
    __instacia = None #atributo de classe

    def __init__(self, qualquer):
        self.atributo_qualquer = qualquer

    @classmethod
    def __new__(cls, *args, **kwargs): #passo antes do init
        if not Controlador.__instacia:
            Controlador.__instacia = object.__new__(cls)
        return Controlador.__instacia

    @classmethod  
    def metodo_classe(cls): #metodo de classe recebe cls de parametro ao inves de self
       print("este é um metodo zumbi!")

inst_controlador1 = Controlador("Atributo1")
print(inst_controlador1, inst_controlador1.atributo_qualquer)

inst_controlador2 = Controlador("Atributo2")
print(inst_controlador2, inst_controlador1.atributo_qualquer)