from estruturas.produto import Produto


class Transformador(Produto):
    def __init__(self,):
        super().__init__()
        self.potencia = 0
        self.led = None
     

    def toArray(self):
        dados_array = super().toArray()
        dados_array['potencia'] = self.potencia
        return dados_array

    def add_dados_db(self, dados_db): # O atributo dados_db recebe da Classe Produto.add_dados_db
        super().add_dados_db(dados_db)
        if 'potencia' in dados_db:
            self.capacidade_maxima = dados_db['potencia']

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco
    
    def setLed(self, led):
        self.led = led