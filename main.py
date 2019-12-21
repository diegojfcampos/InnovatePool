# -*- coding: utf-8 -*-

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

from math import ceil

databases = {}
config = {}

def initDatabases():
    databases['motores'] = Database('motores')
    databases['filtros'] = Database('filtros')
    databases['leds'] = Database('leds')
    databases['vinils'] = Database('vinils')
    databases['areia'] = Database('areia')
    databases['modulo'] = Database('modulo')
    databases['perfil_rigido'] = Database('perfil_rigido')
    databases['tampa'] = Database('tampa')
    databases['transformador'] = Database('transformador')
    databases['manta'] = Database('manta')
    databases['caixa_passagem'] = Database('caixa_passagem')
    databases['maodeobra'] = Database('maodeobra')

    #MAODEOBRA
    #config['moescavacao'] = databases['maodeobra']['escavacao']
    #config['moremocao'] = databases['maodeobra']['remocao']
    #config['moconstrucao'] = Database('moconstrucao')
    #config['mofiltro'] = databases['maodeobra']['instalacao_filtro']
    #config['momotor'] = databases['maodeobra']['instalacao_motobomba']
    #config['movinil'] = databases['maodeobra']['instalacao_vinil']
    
    #CONFIG GERAl
    #databases['config'] = Database('config')

def initConfig():
    config['dimensao'] = None
    config['motor'] = None
    config['filtro'] = None
    config['led'] = None
    config['vinil'] = None
    config['areia'] = None
    config['modulo'] = None
    config['perfil_rigido'] = None
    config['tampa'] = None
    config['transformador'] = None
    config['manta'] = None
    config['caixa_passagem'] = None
    config['maodeobra'] = None
    
    #MAODEOBRA
    #config['moescavacao'] = None
    #config['moremocao'] = None
    #config['moconstrucao'] = None
    #config['mofiltro'] = None
    #config['momotor'] = None
    #config['movinil'] = None
    

def initVinil(dimensao, vinil_escolhido):    
    vinil_escolhido.setDimensoes(dimensao)
    return vinil_escolhido

def initManta(dimensao, dados_db):   
    manta = Manta()
    manta.setDimensoes(dimensao)
    manta.add_dados_db(dados_db)
    return manta

def initPerfil(dimensao, dados_db):   
    perfil = Perfil()
    perfil.setDimensoes(dimensao) 
    perfil.add_dados_db(dados_db)
    return perfil

def initFiltro(tabela, dimensao):
    filtro = Filtro()
    filtros_possiveis = []
    filtro.setDimensao(dimensao)
    itens = tabela.lista() 
  
    for iten in itens:
        if iten['capacidade_maxima']  > dimensao.m3real():
            filtros_possiveis.append(iten)
    
    for iten in filtros_possiveis:        
        print(iten)

    try:
        id_item = int(input('\n Digite o Id do Filtro: '))
        result_db = tabela.find(id_item)
        
        if filtro.verificaFiltro(result_db['capacidade_maxima']) == True:       
            filtro.add_dados_db(result_db)
            return filtro
        else:
            filtro.verificaFiltro(result_db['capacidade_maxima'])
            config['filtro'] = initFiltro(databases['filtros'], config['dimensao'])  
        
    except:
        print('\n ..:: Filtro não encontrado.\n\n')

    return filtro

def initMotor(tabela, filtro):    
    motor = Motor()
    motor.setFiltro(filtro)  
    escolhido = motor.escolhaMotor()    
    result_db = tabela.find(escolhido) 
    motor.add_dados_db(result_db)
    return motor

def initTampa(tabela, filtro):
    tampa = Tampa()
    tampa.setFiltro(filtro)    
    escolhido = tampa.escolhaTampa()
    result_db = tabela.find(escolhido)
    tampa.add_dados_db(result_db)
    return tampa  


def initAreia(filtro, dados_db):    
    areia = Areia()    
    areia.add_dados_db(dados_db)
    areia.setFiltro(filtro)
    return areia

def initLed(dimensao, tabela):
    led = Led()
    led.setDimensoes(dimensao)    
    dados_db = tabela.lista()  
    escolha = int(input('1 - Led Branco\n2 - Azul\n3 - Colorido\nDigite o id da cor desejada: '))
    led_possiveis = led.escolhaCor(dados_db, escolha)     
    
    #Imprime opcoes apenas da cor ecolhida  
    for cor in led_possiveis:
        print(cor)

    id_item = int(input('\n Digite o Id do Led: '))
    result_db = tabela.find(id_item)
         
    if led.verificaEscolha(id_item, led_possiveis) == True:       
        led.add_dados_db(result_db)
    else:
        config['led'] = initLed(config['dimensao'], databases['leds'])

    return led

def initModulo(led, tabela):
    modulo = Modulo()
    modulo.setLed(led)
    dados_db = tabela.lista()

    for item in dados_db:
        print(item)

    try:
        id_item = int(input('\n Digite o Id do Modulo: '))
        result_db = tabela.find(id_item)
        modulo.add_dados_db(result_db)
    except ValueError:
        print('Modulo nao encontrado, digite o Id do modulo.')

    return modulo

def initTransformador(led, dados_db):
    transformador = Transformador()
    transformador.setLed(led)
    transformador.add_dados_db(dados_db)
    return transformador

def initMO(dimensao, dados_db):  
    mo = MO()
    mo.setDimensoes(dimensao)
    mo.add_dados_db(dados_db)
    
    """
    escavacao = dados_db.listaItem('escavacao')
    construcao = dados_db.listaItem('construcao')
    remocao = dados_db.listaItem('remocao_de_terra')
    intal_filtro = dados_db.listaItem('instalacao_filtro')
    intal_motobomba = dados_db.listaItem('instalacao_motobomba')
    intal_vinil = dados_db.listaItem('instalacao_vinil')

    for item in escavacao:
        mo.setEscavacao(item['preco'])
    
    for item in construcao:
        mo.setConstrucao(item['preco'])
    
    for item in remocao:
        mo.setRemocaoTerra(item['preco'])
    
    for item in intal_filtro:
        mo.setInstalacaoFiltro(item['preco'])
    
    for item in intal_motobomba:
        mo.setInstalacaoMotor(item['preco'])

    for item in intal_vinil:
        mo.setInstalacaoVinil(item['preco'])
    """
    return mo

def verConfig():
    print('\n . : Dimensao : .\n')
    if config['dimensao'] != None:
        print(config['dimensao'].toArray())

    print('\n . : Motor : .\n')
    if config['motor'] != None:
        print(config['motor'].toArray())

    print('\n . : Filtro : .\n')
    if config['filtro'] != None:
        print(config['filtro'].toArray())

    print('\n . : Led : .\n')
    if config['led'] != None:
        print(config['led'].toArray())

    print('\n . : Vinil : .\n')
    if config['vinil'] != None:
        print(config['vinil'].toArray())

    print('\n . : Manta : .\n')
    if config['manta'] != None:
        print(config['manta'].toArray())

    print('\n . : Perfil Rígido : .\n')
    if config['perfil_rigido'] != None:
        print(config['perfil_rigido'].toArray())

    print('\n . : Areia: .\n')
    if config['areia'] != None:
        print(config['areia'].toArray())

    print('\n . : Tampa da casa de máquinas : .\n')
    if config['tampa'] != None:
        print(config['tampa'].toArray())

    print('\n . : Transformador : .\n')
    if config['transformador'] != None:
        print(config['transformador'].toArray())
        
    print('\n . : Módulo: .\n')
    if config['modulo'] != None:
        print(config['modulo'].toArray())

    print('\n . : Mão de Obra .\n')
    if config['maodeobra'] != None:
        print(config['maodeobra'].toArray())    


def calcularPreco():
    preco = 0.0    
    if config['filtro'] != None:
        aux = config['filtro'].getPreco()
        preco += aux
        print('\n..:: Filtro => R$ ' + str(aux) + '\n')
    
    if config['led'] != None:
        aux = config['led'].getPreco()
        preco += aux
        print('\n..:: Led => R$ ' + str(aux) + '\n')

    if config['transformador'] != None:
        aux = config['transformador'].getPreco()
        preco += aux
        print('\n..:: Tranformador => R$ ' + str(aux) + '\n')

    if config['modulo'] != None:
        aux = config['modulo'].getPreco()
        preco += aux
        print('\n..:: Modulo => R$ ' + str(aux) + '\n')

    if config['vinil'] != None:
        aux = config['vinil'].getVinilCalculado()
        preco += aux
        print('\n..:: Vinil => R$ ' + str(aux) + '\n')

    if config['manta'] != None:
        aux = config['manta'].getMantaCalculado()
        preco += aux
        print('\n..:: Manta de Revestimento => R$ ' + str(aux) + '\n')

    if config['perfil_rigido'] != None:
        aux = config['perfil_rigido'].getPerfilCalculado()
        preco += aux
        print('\n..:: Perfil Rigido => R$ ' + str(aux) + '\n')

    if config['motor'] != None:
        aux = config['motor'].getPreco()
        preco += aux
        print('\n..:: Motor => R$ ' + str(aux) + '\n')

    if config['areia'] != None:
        aux = config['areia'].getAreiaCalculado()
        preco += aux
        print('\n..:: Areia => R$ ' + str(aux) + '\n')
    
    if config['tampa'] != None:
        aux = config['tampa'].getPreco()
        preco += aux
        print('\n..:: Tampa da casa de máquinas => R$ ' + str(aux) + '\n')    
    
    if config['maodeobra'] != None:
        aux = config['maodeobra'].getMOTotal()
        preco += aux
        print('\n..:: Mão de Obra Total => R$ ' + str(aux) + '\n')

    """
    config['escavacao'] = databases['mao_de_obra']['escavacao']
    config['remocao'] = databases['mao_de_obra']['remocao_de_terra']
    config['construcao'] = databases['mao_de_obra']['construcao']
    config['instalacao_filtro'] = databases['mao_de_obra']['instalacao_filtro']
    config['instalacao_motobomba'] = databases['mao_de_obra']['instalacao_motobomba']
    config['instalacao_vinil'] = databases['mao_de_obra']['instalacao_vinil']
    """
    print('\n..:: Total => R$ ' + str(preco) + '\n')
  

#--------------------------------------------------------------------------------------------------
####--   busca o termo gravado no atributo tabela em database.lista e printa a chave   --####

#             ('motores', 'Lista de Motores')
def listarDBItens(tabela, name):
    print('\n . : ' + name + ' : .\n')
    itens = databases[tabela].lista()
    for item in itens:        
        print(item)
#--------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
####--   Seleciona o item pelo ID e retorna no atributo OBJETO   --####

#                  ("motores",'Motor',Motor())
def escolherProduto(tabela, texto, objeto):
    try:
        id_item = int(input('\n Digite o Id do ' + texto + ': '))
        result_db = databases[tabela].find(id_item)
        objeto.add_dados_db(result_db)
        
        return objeto
        
    except:
        print('\n ..:: Motor não encontrado.\n\n')
#--------------------------------------------------------------------------------------------------


def main():
    initDatabases()
    initConfig()    
    menu = Menu()

    opcao = -1
    while opcao != 0:
        opcao = menu.menu_inicial()
        if opcao == 1:
            dim = menu.digita_dimensao()
            config['dimensao'] = Dimensao(dim[0], dim[1], dim[2], dim[3])      
            config['maodeobra'] = initMO(config['dimensao'], databases['maodeobra'])            
                      
        elif opcao == 2:
            listarDBItens('vinils', 'Lista de Vinils')
            config['vinil'] = escolherProduto('vinils', 'vinils', Vinil())
            initVinil(config['dimensao'], config['vinil'])
            config['manta'] = initManta(config['dimensao'], databases['manta'].lista())
            config['perfil_rigido'] = initPerfil(config['dimensao'], databases['perfil_rigido'].lista()) 
                    
        elif opcao == 3:
            config['filtro'] = initFiltro(databases['filtros'], config['dimensao'])            
            config['areia'] = initAreia(config['filtro'], databases['areia'].lista())            
            config['motor'] = initMotor(databases['motores'], config['filtro'])
            config['tampa'] = initTampa(databases['tampa'], config['filtro'] )           

        elif opcao == 4:
            config['led'] = initLed(config['dimensao'], databases['leds'])

            if config['led'].cor_da_luz == 'branco':
                config['transformador'] = initTransformador(config['led'], databases['transformador'].lista())
            elif config['led'].cor_da_luz == 'azul':
                config['transformador'] = initTransformador(config['led'], databases['transformador'].lista())
            elif config['led'].cor_da_luz == 'colorido':
                config['modulo'] = initModulo(config['led'], databases['modulo'])        

        elif opcao == 5:
            verConfig()

        elif opcao == 6:
            calcularPreco()

        elif opcao == 7:
            print(f'\nTestando Objetos e Métodos\n')
            #Testanto
            #Vinil
            print(f"Tipo de Arquivo Vinil: {config['vinil']}")
            print(f"Preco do Vinil: {config['vinil'].getVinilPreco()}")
            print(f"Preco Calculado do Vinil: {config['vinil'].getVinilCalculado()}\n")

            #Filtro
            print(f"Tipo de Arquivo Filtro: {config['filtro']}")
            print(f"Preco do Filtro: {config['filtro'].getPreco()}\n")
            
            #Motor
            print(f"Tipo de Arquivo Motor: {config['motor']}")
            print(f"Preco do Motor: {config['motor'].getPreco()}\n")

            #Led
            print(f"Tipo de Arquivo Led: {config['led']}")
            print(f"Preco do Led: {config['led'].getPreco()}\n")

            #Manta
            print(f"Tipo de Arquivo Manta: {config['manta']}")
            print("ATRIBUTOS")          
            print(f"Id: {config['manta'].id}")
            print(f"Fornecedor: {config['manta'].fornecedor}")
            print(f"Marca: {config['manta'].marca}")
            print(f"Margem de Lucro: {config['manta'].margem_de_lucro}")
            print(f"Custo: {config['manta'].custo}")
            print(f"Tamanho:{config['manta'].tamanho}")

            print("METODOS")  
            print(f"Preco da Manta: {config['manta'].getMantaPreco()}")
            print(f"Preco Calculado da Manta: {config['manta'].getMantaCalculado()}\n")      

            #Perfil
            print(f"Tipo de Arquivo Perfil: {config['perfil_rigido']}")
            print(f"Preco do Perfil: {config['perfil_rigido'].getPerfilPreco()}")
            print(f"Preco Calculado do Perfil: {config['perfil_rigido'].getPerfilCalculado()}\n")

            #Areia
            print(f"Tipo de Arquivo Areia: {config['areia']}")
            print(f"Preco da Areia: {config['areia'].getPreco()}")            
            print(f"Preco Calculado do Areia: {config['areia'].getAreiaCalculado()}\n")
            
            #Tampa
            print(f"Tipo de Arquivo Tampa: {config['tampa']}")
            print(f"Preco do Tampa: {config['tampa'].getPreco()}\n")

            #Modulo
            if config['modulo'] != None:
                print(f"Tipo de Arquivo Modulo: {config['modulo']}")
                print(f"Preco do Modulo: {config['modulo'].getPreco()}\n")

            #Transformador
            if config['transformador'] != None:
                print(f"Tipo de Arquivo Transformador: {config['transformador']}")
                print(f"Id: {config['transformador'].id}")
                print(f"Fornecedor: {config['transformador'].fornecedor}")
                print(f"Marca: {config['transformador'].marca}")
                print(f"Margem de Lucro: {config['transformador'].margem_de_lucro}")
                print(f"Custo: {config['transformador'].custo}")
                print(f"Potencia:{config['transformador'].potencia}")

                print("METODOS")   
                print(f"Preco do Transformador: {config['transformador'].getPreco()}\n")

            #Mao de Obra
            print(f"Tipo de Arquivo Mao de Obra: {config['maodeobra']}")
            print(f"Preco Escavavao: {config['maodeobra'].getEscavacao()}")
            print(f"Preco Remocao de Terra: {config['maodeobra'].getRemocao()}")
            print(f"Preco Construcao: {config['maodeobra'].getConstrucao()}")
            print(f"Preco Instalacao do Filtro: {config['maodeobra'].getInstalacaoFiltro()}")
            print(f"Preco Instalacao do Vinil: {config['maodeobra'].getInstalacaoVinil()}")
            print(f"Preco Instalacao do Motor: {config['maodeobra'].getInstalacaoMotor()}")
            print(f"TOTAL MAO DE OBRA: {config['maodeobra'].getMOTotal()}\n")
            
main()


