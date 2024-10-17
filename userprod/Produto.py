import Sistema


class Produto:
    def __init__(self, id, nome, quant, preco):

        self.__id: int = id
        self.__nome: str = nome
        self.__quant: int = quant
        self.__preco: float = preco
        Sistema.Sistema.Cad_Prod(self.__id, self.__nome, self.__preco, self.__quant)
