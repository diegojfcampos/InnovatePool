# -*- coding: utf-8 -*-

from estruturas.produto import Produto

class Filtro(Produto):
    def __init__(self):        
        super().__init__()
        self.capacidade_maxima = 00
        self.capacidade_areia = None
        self.dimensao = None
        self.areia = None
        self.tampa = None       

       
    def toArray(self):
        dados_array = super().toArray()
        dados_array['capacidade_maxima'] = self.capacidade_maxima
        dados_array['capacidade_de_areia'] = self.capacidade_areia
        return dados_array

    def add_dados_db(self, dados_db):# O atributo dados_db recebe dado da Classe Produto.add_dados_db
        super().add_dados_db(dados_db)
        if 'capacidade_maxima' in dados_db:
            self.capacidade_maxima = dados_db['capacidade_maxima']
        if 'capacidade_de_areia' in dados_db:
            self.capacidade_areia = dados_db['capacidade_de_areia']

    def setDimensao(self, dimensao):
        self.dimensao = dimensao

    def setMotor(self, motor):
        self.motor = motor

    def setAreia(self, areia):
        self.areia = areia
    
    def setTampa(self, tampa):
        self.tampa = tampa

    def getPreco(self):
        preco = super().getPreco()
        return preco

    def verificaFiltro(self, filtro_verificacao):
        if self.dimensao.m3real() < filtro_verificacao:            
            return True

        if self.dimensao.m3real() > filtro_verificacao:
            print("Este Filtro é muito pequeno para o tamanho da psicina")
            return False  
