

class Product():
    def __init__(self, __segredo__: False):
        if not __segredo__:
            raise Exception()
        self.atributo = None


class Creator():
    def __init__(self):
        self.__product_instance = None

    def factory_method(self):
        if self.__product_instance is None:
            self.__product_instance = Product(__segredo__=True)
        return self.__product_instance