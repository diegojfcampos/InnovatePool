
from estruturas.produto import Produto

class Tampa(Produto):
    def __init__(self):        
        super().__init__()
        self.material = ' '
        self.filtro = None     
       
    def toArray(self):
        dados_array = super().toArray()
        dados_array['material'] = self.material
        return dados_array

    def add_dados_db_filtro(self, dados_db):# O atributo dados_db recebe dado da Classe Produto.add_dados_db
        super().add_dados_db(dados_db)
        if 'material' in dados_db:
            self.material = dados_db['material']

    def getPreco(self):
        preco = super().getPreco()
        return preco

    def setPreco(self, preco):
        self.preco = preco

    def setFiltro(self, filtro):
        self.filtro = filtro

    def escolhaTampa(self):
        if self.filtro.capacidade_maxima <= 78:
            return 1            
        
        if self.filtro.capacidade_maxima > 78 :
            return 2 