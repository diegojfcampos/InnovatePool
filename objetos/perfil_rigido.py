from estruturas.produto import Produto


class Perfil(Produto):
    
    def __init__(self):
        super().__init__()
        self.tamanho = ''     
        self.dimensoes = None       
    
    def toArray(self):
        dados_array = super().toArray()
        dados_array['tamanho'] = self.tamanho
        return dados_array

    def add_dados_db(self, dados_db):
        super().add_dados_db(dados_db)
        if 'tamanho' in dados_db:
            self.tamanho = dados_db['tamanho']

    def setDimensoes(self, dimensoes):
        self.dimensoes = dimensoes

    def getPerfilPreco(self):
        precoBasePerfil = super().getPreco()                
        return precoBasePerfil
    
    def getPerfilCalculado(self):        
        return self.dimensoes.m2facial() * self.getPerfilPreco()

    def setPreco(self, preco):
        self.preco = preco