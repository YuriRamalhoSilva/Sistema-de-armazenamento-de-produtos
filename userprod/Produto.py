import Sistema


class Produto:
    def __init__(self, nome, quant, preco):
        self.__nome: str = nome
        self.__quant: int = quant
        self.__preco: float = preco
       
    def set_nome (self,nome):
        self.__nome = nome
    
    def set_quant (self,quant):
        self.__quant = quant
    
    def set_preco (self,preco):
        self.__preco = preco

    def get_nome (self):
        return self.__nome
    
    def get_quant(self):
        return self.__quant
    
    def get_preco(self):
        return self.__preco
    

