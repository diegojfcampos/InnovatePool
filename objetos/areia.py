from estruturas.produto import Produto

class Areia(Produto):

    def __init__(self):        
        super().__init__()
        self.peso = 00       
        self.filtro = None
       
    def toArray(self):
        dados_array = super().toArray()
        dados_array['peso'] = self.peso
        return dados_array
    
    def add_dados_db(self, dados_db):
        super().add_dados_db(dados_db)
        if 'peso' in dados_db:
            self.peso = dados_db['peso']
    
    def setPreco(self, preco):
        self.preco = preco

    def setFiltro(self, filtro):
        self.filtro = filtro

    def getPreco(self):
        return self.preco

    def getAreiaCalculado(self):
        return (self.getPreco() * self.filtro.capacidade_areia)

    def getAreia(self):
            print(f"======\n Areia \n======")
            print(f"Id: {self.id}")
            print(f"Marca: {self.marca}")
            print(f"Tipo: {self.modelo}")
            print(f"Preco Lata: {self.getPreco()}")
            print(f"Quantidade: {self.filtro.capacidade_areia} latas")
            print(f"Preco Calculado: {self.getAreiaCalculado()}\n")
