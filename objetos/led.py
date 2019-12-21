# -*- coding: utf-8 -*-

from estruturas.produto import Produto


class Led(Produto):
    def __init__(self):
        super().__init__()
        self.cor_da_luz = ''
        self.potencia = 0.0
        self.area_iluminacao = 12.0
        self.dimensoes = None    

    def toArray(self):
       dados_array = super().toArray()
       dados_array['cor_da_luz'] = self.cor_da_luz
       dados_array['potencia'] = self.potencia
       dados_array['area_de_iluminacao'] = self.area_iluminacao
       return dados_array

    def add_dados_db(self, dados_db):# O atributo dados_db recebe dado da Classe Produto.add_dados_db
        super().add_dados_db(dados_db)
        if 'cor_da_luz' in dados_db:
            self.cor_da_luz = dados_db['cor_da_luz']
        if 'potencia' in dados_db:
            self.potencia = dados_db['potencia']
        if 'area_de_iluminacao' in dados_db:
            self.area_iluminacao = dados_db['area_de_iluminacao']
    
    def setDimensoes(self, dimensoes):
        self.dimensoes = dimensoes

    def getPreco(self):
        preco = super().getPreco()
        return preco

    def escolhaCor(self, dados_db, escolha):

        led_possiveis = []
        if escolha == 1:
            for cor in dados_db:
                if cor['cor_da_luz'] == 'branco':
                    led_possiveis.append(cor)
        
        elif escolha == 2:
            for cor in dados_db:
                if cor['cor_da_luz'] == 'azul':
                    led_possiveis.append(cor)         
            
        elif escolha == 3:
            for cor in dados_db:
                if cor['cor_da_luz'] == 'colorido':
                    led_possiveis.append(cor)        
                
        return led_possiveis
    
    def verificaEscolha(self, escolha, led_possiveis):
        for led in led_possiveis:
            if led['id'] == escolha:
                return True        
          
    def quantidadeLeds(self):
        #Necessario truncar para mais math.ceil
        return (self.dimensoes.m2facial() / self.area_iluminacao)

    