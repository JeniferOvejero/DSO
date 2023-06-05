

class Controlador():
    __instaciado = False #atributo de classe

    def __init__(self, qualquer):
        self.atributo_qualquer = qualquer
        if not Controlador.__instaciado:
            Controlador.__instaciado = True
        else:
            raise Exception("ja instanciado") #começa, mas não termina a criação de instancia

    @classmethod  
    def metodo_classe(cls): #metodo de classe recebe cls de parametro ao inves de self
       print("este é um metodo zumbi!")

inst_controlador1 = Controlador("Atributo1")
print(inst_controlador1, inst_controlador1.atributo_qualquer)

inst_controlador2 = Controlador("Atributo2")
print(inst_controlador2, inst_controlador1.atributo_qualquer)