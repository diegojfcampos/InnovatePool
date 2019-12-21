
from estruturas.produto import Produto
from estruturas.dimensao import Dimensao
"""
from objetos.manta import Manta
from objetos.perfil_rigido import Perfil
from estruturas.dimensao import Dimensao
"""

class Vinil(Produto):
    
    def __init__(self):
        super().__init__()
        self.espessura = ''
        self.dimensoes = None
        self.manta = None
        self.perfil = None
        self.preco = 114.50
         
    
    def toArray(self):
        dados_array = super().toArray()
        dados_array['espessura'] = self.espessura
        return dados_array

    def add_dados_db(self, dados_db):
        super().add_dados_db(dados_db)
        if 'espessura' in dados_db:
            self.espessura = dados_db['espessura']

    def setDimensoes(self, dimensoes):
        self.dimensoes = dimensoes
        
    def setManta(self, manta):
        self.manta = manta         
    
    def setPerfil(self, perfil):
        self.perfil = perfil       

    def getVinilPreco(self):
        preco = super().getPreco()                
        return preco
    
    def getVinilCalculado(self):            
        return self.dimensoes.m2total() * self.preco
 
    def getPrecoManta(self):        
        return self.dimensoes.m2facial() * self.manta.getMantaPreco()

    def getPrecoPerfil(self):  
        return self.dimensoes.m2facial() * self.perfil.getPerfilPreco()

    def getPrecoTotal(self):
        return self.getVinilCalculado() + self.getPrecoManta() + self.getPrecoPerfil()


    #apagar daqui pra baixo, apenas testes
    def printManta(self):
        print(f"\nTodos atributos e métodos manta\n")
        print('Atributos Dimensao')
        print(f'Id: {self.manta.id}')
        print(f'Fornecedor: {self.manta.fornecedor}')
        print(f'Marca: {self.manta.marca}')
        print(f'Modelo: {self.manta.modelo}')
        print(f'Custo: {self.manta.custo}')
        print(f'Ml: {self.manta.margem_de_lucro}')
        print(f'Preco: {self.manta.preco}')
        print(f'Tamanho: {self.manta.tamanho}\n')
        print(f'Metodo pegar preco Manta: {self.manta.getMantaPreco()}')

    def printPerfil(self):
        print(f"\nTodos atributos e métodos perfil\n")
        print('Atributos Perfil')
        print(f'Id: {self.perfil.id}')
        print(f'Fornecedor: {self.perfil.fornecedor}')
        print(f'Marca: {self.perfil.marca}')
        print(f'Modelo: {self.perfil.modelo}')
        print(f'Custo: {self.perfil.custo}')
        print(f'Ml: {self.perfil.margem_de_lucro}')
        print(f'Preco: {self.perfil.preco}')
        print(f'Tamanho: {self.perfil.tamanho}')
        print(f'Metodo pegar preco Manta: {self.perfil.getPerfilPreco()}')

    def printDimensoes(self):
        print("\nTodos atributos e métodos Dimensoes\n")
        print('Atributos Dimensoes')
        print(f'Largura: {self.dimensoes.largura}')
        print(f'Comprimento: {self.dimensoes.comprimento}')
        print(f'Profundidade Inicial: {self.dimensoes.prof_inicial}')
        print(f'Profundidade Final:{self.dimensoes.prof_final}')
        print(f'Largura da Calcada: {self.dimensoes.largura_da_calcada}\n')
        print('Métodos de Dimensões')
        print(f'p_m: {self.dimensoes.profundidade_media()}')
        print(f'perimetro: {self.dimensoes.perimetro()}')
        print(f'm2facil: {self.dimensoes.m2facial()}')
        print(f'm2parede: {self.dimensoes.m2parede()}')
        print(f'm2total: {self.dimensoes.m2total()}')
        print(f'm3total: {self.dimensoes.m3total()}')
        print(f'm3real: {self.dimensoes.m3real()}')
        print(f'area calcada: {self.dimensoes.area_calcada()}\n')

"""
#TESTES DE CLASSE

#Instancias
teste_vinil = Vinil()
teste_dimensoes = Dimensao(2,2,2,2,2)
perfil = Perfil()
manta = Manta()

print(f'Classe Vinil: {teste_vinil}') #testando classe
print(f'Classe Dimensoes: {teste_dimensoes}\n')  #testando classe

#Metodos Sets - Setando objetos
print(f'Metodos Sets - Setando objetos\n')
print(f'Tipo de dado Dimensoes: {teste_vinil.dimensoes}')
teste_vinil.setDimensoes(teste_dimensoes)
print(f'Tipo de dado Dimensoes: {teste_vinil.dimensoes}\n')

print(f'Tipo de dado Dimensoes: {teste_vinil.manta}')
teste_vinil.setManta(manta)

print(f'Tipo de dado Dimensoes: {teste_vinil.manta}\n')

print(f'Tipo de dado Dimensoes: {teste_vinil.perfil}')
teste_vinil.setPerfil(perfil)

print(f'Tipo de dado Dimensoes: {teste_vinil.perfil}\n')

#Métodos Gets - Pegando dados
print(f'Outputs Metodos')
print(f'Metodo Preco Vinil: {teste_vinil.getVinilPreco()}')
print(f'Metodo Preco Vinil Calculado: {teste_vinil.getVinilCalculado()}')
print(f'Metodo Preco Manta: {teste_vinil.getPrecoManta()}')
print(f'Metodo Preco Perfil: {teste_vinil.getPrecoPerfil()}')
print(f'Metodo Preco TOTAL: {teste_vinil.getPrecoTotal()}')


#Testando metodos prints
teste_vinil.printDimensoes()
teste_vinil.printManta()
teste_vinil.printPerfil()
"""

    






  
