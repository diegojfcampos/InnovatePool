
from estruturas.dimensao import Dimensao


class MO:

    def __init__(self):
        
        self.escavacao = 0.0
        self.remocao_terra = 0.0
        self.construcao = 0.0
        self.instalacao_filtro = 0.0
        self.instalacao_moto_bomba = 0.0
        self.instalacao_vinil = 0.0
        self.vinil = 0.0
        self.motor = 0.0
        self.filtro = 0.0
        self.dimensoes = None

    def setDimensoes(self, dimensoes):
        self.dimensoes = dimensoes

    def setVinil(self, vinil):
        self.vinil = vinil
    
    def setMotor(self, motor):
        self.motor = motor
    
    def setFiltro(self, filtro):
        self.filtro = filtro
        
    def setEscavacao(self, preco_escavacao):
        self.escavacao = preco_escavacao

    def setRemocaoTerra(self, preco_remocao):
        self.remocao_terra = preco_remocao

    def setConstrucao(self, construcao):
        self.construcao = construcao
    
    def setInstalacaoFiltro(self, preco_instalacao_filtro):
        self.instalacao_filtro = preco_instalacao_filtro

    def setInstalacaoVinil(self, preco_instalacao_vinil):
        self.instalacao_vinil = preco_instalacao_vinil
    
    def setInstalacaoMotor(self, preco_instalacao_motor):
        self.instalacao_moto_bomba = preco_instalacao_motor

    def getEscavacao(self):   
        return self.dimensoes.m3total() * self.escavacao

    def getConstrucao(self):    
        return self.dimensoes.m2total() * self.construcao

    def getRemocao(self):
        return self.dimensoes.m3total() * self.remocao_terra

    def getInstalacaoVinil(self):
        return self.instalacao_vinil

    def getInstalacaoFiltro(self):
        return self.instalacao_filtro

    def getInstalacaoMotor(self):
        return self.instalacao_moto_bomba

    def getMOTotal(self):
        return self.getEscavacao() + self.getRemocao() + self.getConstrucao() + self.getInstalacaoVinil() + self.getInstalacaoMotor()+ self.getInstalacaoFiltro()


#TESTES DE CLASSE

#Instancias
print(f'Instanciando objetos e verificando\n')
mo = MO()
dimensoes = Dimensao(2,2,2,2,2)
print(f'Classe MO: {mo}') #testando classe
print(f'Classe Dimensoes: {dimensoes}\n')  #testando classe
print(f'Tipo de dado Dimensoes: {mo.dimensoes}')
mo.setDimensoes(dimensoes)
print(f'Tipo de dado Dimensoes: {mo.dimensoes}\n')

#Verificando objeto dimensoes
print(f'Verificando objeto dimensões')
print("\nTodos atributos e métodos Dimensoes\n")
print('Atributos Dimensoes')
print(f'Largura: {dimensoes.largura}')
print(f'Comprimento: {dimensoes.comprimento}')
print(f'Profundidade Inicial: {dimensoes.prof_inicial}')
print(f'Profundidade Final:{dimensoes.prof_final}')
print(f'Largura da Calcada: {dimensoes.largura_da_calcada}\n')
print('Métodos de Dimensões')
print(f'p_m: {dimensoes.profundidade_media()}')
print(f'perimetro: {dimensoes.perimetro()}')
print(f'm2facil: {dimensoes.m2facial()}')
print(f'm2parede: {dimensoes.m2parede()}')
print(f'm2total: {dimensoes.m2total()}')
print(f'm3total: {dimensoes.m3total()}')
print(f'm3real: {dimensoes.m3real()}')
print(f'area calcada: {dimensoes.area_calcada()}\n')

#Verificando atributos vazios
print(f'Verificando atributos vazios.\n')
print(f'Preco Escavacao: {mo.escavacao}')
print(f'Preco Remocao da Terra: {mo.remocao_terra}')
print(f'Preco Construcao {mo.construcao}')
print(f'Preco Instalacao Filtro {mo.instalacao_filtro}')
print(f'Preco Instalacao Vinil {mo.instalacao_vinil}')
print(f'Preco Instalacao Moto Bomba {mo.instalacao_moto_bomba}\n')

#Setando valores fixos
print(f'Testando metodos sets = Setando valores fixos.')
mo.setDimensoes(dimensoes)
mo.setEscavacao(21)
mo.setRemocaoTerra(24)
mo.setConstrucao(57)
mo.setInstalacaoFiltro(255)
mo.setInstalacaoVinil(525)
mo.setInstalacaoMotor(150)
print(f'Valores setados.')

#Verificando atributos setados
print(f'\nVerificando atributos setados.\n')
print(f'Preco Escavacao: {mo.escavacao}')
print(f'Preco Remocao da Terra: {mo.remocao_terra}')
print(f'Preco Construcao {mo.construcao}')
print(f'Preco Instalacao Filtro {mo.instalacao_filtro}')
print(f'Preco Instalacao Vinil {mo.instalacao_vinil}')
print(f'Preco Instalacao Moto Bomba {mo.instalacao_moto_bomba}\n')

#Verificando métodos
print(f'Verificando Métodos da Classe MO.\n')
print(f'Método getEscavacao: {mo.getEscavacao()}')
print(f'Método getRemocao: {mo.getRemocao()}')
print(f'Método getConstrucap: {mo.getConstrucao()}')
print(f'Método getInstalcaoFiltro: {mo.getInstalacaoFiltro()}')
print(f'Método getInstalcaoVinil: {mo.getInstalacaoVinil()}')
print(f'Método getInstalcaoFiltro: {mo.getInstalacaoMotor()}')
print(f'Método getMOTotal: {mo.getMOTotal()}')