

class JogoDuplicadoException(Exception):
    def __init__(self):
        super().__init__("jogo duplicado!")
