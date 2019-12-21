from dbs.database import Database

from objetos.motor import Motor
from objetos.filtro import Filtro
from objetos.led import Led
from objetos.vinil import Vinil
from objetos.manta import Manta
from objetos.perfil_rigido import Perfil
from objetos.areia import Areia
from objetos.tampa import Tampa
from objetos.maodeobra import MO
from objetos.modulo import Modulo
from objetos.transformador import Transformador

from estruturas.menu import Menu
from estruturas.dimensao import Dimensao

class WebApp:
    
    def __init__(self, config):
        self.config = config
        self.html = ''

    def main(self, server):        
        self.html += '<h>Digite as Dimensões da Piscina</h>' 
        self.html += '<form method=get action=adddimensao>'
        self.html += '<label>Largura:</label/>'
        self.html += '<input name="largura" placeholder="Digite a Largura"/>'
        self.html += '<label>Comprimento:</label/>'
        self.html += '<input name="comprimento" placeholder="Digite o Comprimento"/>'
        self.html += '<label>Profundidade Inicial:</label/>'
        self.html += '<input name="prof_inicial" placeholder="Digite a Profundidade"/>'
        self.html += '<label>Profundidade Final:</label/>'
        self.html += '<input name="prof_final" placeholder="Digite a Profundidade"/>'
        self.html += '<label>Largura da Calçada:</label/>'
        self.html += '<input name="largura_da_calcada" placeholder="0.6 metros"/>'

        self.html += '<b><a href="/configuracao">CONFIGURAÇÕES</a>'

        self.html += '<button type="submit">Confirmar Dimensões da Piscina</button>'


        self.getConfigAtual(server)
        self.getPrecoAtual(server)


    def adddimensao(self, server):
        params = server.getParams()
        try: 
            self.config['dimensao'] = Dimensao(0, 0, 0, 0)
            self.config['dimensao'].largura = float(params['largura'])
            self.config['dimensao'].comprimento = float(params['comprimento'])
            self.config['dimensao'].prof_inicial = float(params['prof_inicial'])
            self.config['dimensao'].prof_final = float(params['prof_final'])           
            self.config['dimensao'].setCalcada(float(params['largura_da_calcada']))
            self.main(server)

        except:
            self.html += '<b>Erro:</b> Valor inválido, tente usar números.'
            self.html += '<a class="button" href="/main">Voltar</a>'

    def vinils(self, server):        
        params = server.getParams()
        try:
            self.listarDBItens(server, 'vinils', 'VINIL', 'vinils')
            result_db = self.config['vinils'].find(int(params['id']))
            vinil = Vinil()
            vinil.setDimensoes(self.config['dimensao'])
            vinil.add_dados_db_vinil(result_db)
            self.config['vinil'] = vinil
            self.main(server)
        except:
            self.listarDBItens(server, 'vinils', 'VINIL', 'vinils')

    def manta(self, server):         
        manta = Manta()
        manta.setDimensoes(self.config['dimensao'])
        manta.add_dados_db(self.config['mantas'].lista())
        self.config['manta'] = manta
        self.main(server)

    def perfil(self, server):   
        perfil = Perfil()
        perfil.setDimensoes(self.config['dimensao']) 
        perfil.add_dados_db(self.config['perfis'].lista())
        self.config['perfil'] = perfil
        self.main(server)

    def filtros(self, server):
        """
        self.html += '<label>Escolha um Filtro:</label/>'
        self.html += '<input name="filtro" placeholder="Digite o Filtro"/>'
        self.html += '<h>Escolha um Filtro</h>'
        itens = self.config['filtros'].lista()
        self.html += '<table cellspacing=0 cellpadding=0>' 
        """
        params = server.getParams()
        filtro = Filtro()
        filtros_possiveis = []
        filtro.setDimensao(self.config['dimensao'])
        itens = self.config['filtros'].lista() 
         
        for iten in itens:
            if iten['capacidade_maxima']  > self.config['dimensao'].m3real():
                filtros_possiveis.append(iten)

        try:            
            result_db = self.config['filtros'].find(int(params['id']))         
            if filtro.verificaFiltro(result_db['capacidade_maxima']) == True:       
                filtro.add_dados_db(result_db)                
                self.config['filtro'] = filtro
                self.main(server)        
        except:
            print('\n ..:: Filtro não encontrado.\n\n')

    def areia(self, server):    
        areia = Areia()            
        areia.setFiltro(self.config['filtro'])
        areia.add_dados_db(self.config['areia'].lista())
        self.config['areia'] = areia
        self.main(server)
        
    def motores(self, server):          
        motor = Motor()
        motor.setFiltro(self.config['filtro'])  
        escolhido = motor.escolhaMotor()    
        result_db = self.config['motores'].find(escolhido)
        motor.add_dados_db(result_db)
        self.config['motor'] = motor
        self.main(server)

    def tampa(self, server):
        tampa = Tampa()
        tampa.setFiltro(self.config['filtro'])    
        escolhido = tampa.escolhaTampa()
        result_db = self.config['tampas'].find(escolhido)
        tampa.add_dados_db(result_db)
        self.config['tampa'] = tampa
        self.main(server)
            
    def leds(self, server):
        params = server.getParams()
        try:
            result_db = self.config['leds'].find(int(params['id']))
            led = Led()
            led.add_dados_db(result_db)
            self.config['led'] = led
            self.main(server)
        except:
            self.listarDBItens(server, 'leds', 'LED', 'leds')
 
    def transformador(self, server, led):
        transformador = Transformador()        
        transformador.setLed(self.config['led'])
        transformador.add_dados_db(self.config['transformador'].lista())
        self.config['transformador'] = transformador
        self.main(server)

    def listarDBItens(self, server, tabela, name, page):
        self.html += '<h3>Escolha um ' + name + ':</h3>'
        itens = self.config[tabela].lista()
        self.html += '<table cellspacing=0 cellpadding=0>' 
        
        # CAEBC
        self.html += '<tr>'
        for dado in itens[0]:
            self.html += '<th>' + dado + '</th>'
        self.html += '<th>Escolher</th>'
        self.html += '</tr>' 
        
        # ITEMS
        for item in itens:
            self.html += '<tr>'
            for dado in item:
                self.html += '<td>' + str(item[dado]) + '</td>'
            self.html += '<td><a href="/'+page+'?id=' + str(item['id']) + '">Escolher</a></td>'
            self.html += '</tr>' 

        self.html += '</table>' 
        self.html += '<hr/><a class="button" href="/">Voltar</a>'

    def getConfigAtual(self, server):  
            
        dim = self.config['dimensao']        
        self.html += '<HR/><h3>Dimensões Digitadas:</h3>'
        self.html += '<div><b>Largura: </b>' + str(dim.largura) + '</div>'
        self.html += '<div><b>Comprimento: </b>' + str(dim.comprimento) + '</div>'
        self.html += '<div><b>Profundidade Inicial: </b>' + str(dim.prof_inicial) + '</div>'
        self.html += '<div><b>Profundidade Final: </b>' + str(dim.prof_final) + '</div>'

        self.html += '<HR/><h3>Dimensões da Piscina:</h3>'
        self.html += '<div><b>- Largura da Calçada: </b>' + str(dim.largura_da_calcada) + '</div>'
        self.html += '<div><b>- Profundidade Média: </b>' + str(dim.profundidade_media()) + '</div>'
        self.html += '<div><b>- Área de Calçada: </b>' + str(dim.area_da_calcada()) + '</div>'
        self.html += '<div><b>- Perímetro: </b>' + str(dim.perimetro()) + '</div>'
        self.html += '<div><b>- M² Facial: </b>' + str(dim.m2facial()) + '</div>'
        self.html += '<div><b>- M² Parede: </b>' + str(dim.m2parede()) + '</div>'
        self.html += '<div><b>- M² Total: </b>' + str(dim.m2total()) + '</div>'
        self.html += '<div><b>- M³ Total: </b>' + str(dim.m3total()) + '</div>'
        self.html += '<div><b>- M³ Real: </b>' + str(dim.m3real()) + '</div>'
        self.escolhido('Motor', 'motor')
        self.escolhido('Filtro', 'filtro')
        self.escolhido('Led', 'led')
        
    def escolhido(self, name, dado):
        if self.config[dado] != None:
            self.html += '<HR/><h3>' + name + ':</h3>'
            try:
                self.html += '<div><b>id: </b>' + str(self.config[dado].id) + '</div>'
                self.html += '<div><b>Nome: </b>' + str(self.config[dado].nome) + '</div>'
                self.html += '<div><b>Preço: </b>R$ ' + str(self.config[dado].preco) + '</div>'
            except:
                self.html += '' + name + ' não escolhido'
                
    def getPrecoAtual(self, server):
        self.html += ''
        self.html += ''