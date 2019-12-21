from estruturas.produto import Produto


class Manta(Produto):
    
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

    def getMantaPreco(self):
        precoBaseManta = super().getPreco()                
        return precoBaseManta
    
    def getMantaCalculado(self):        
        return self.dimensoes.m2facial() * self.getMantaPreco()

    def setPreco(self, preco):
        self.preco = preco


    def getCheckManta(self):
        print(self.dimensoes.largura)
        print(self.dimensoes.comprimento)
        print(self.dimensoes.prof_inicial)
        print(self.dimensoes.prof_final)
        print(self.dimensoes.largura_da_calcada)
        print(self.id)
        print(self.fornecedor)
        print(self.marca)
        print(self.margem_de_lucro)
        print(self.custo)
        print(self.tamanho)
        print(self.preco)