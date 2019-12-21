# -*- coding: utf-8 -*-

from estruturas.produto import Produto


class Motor(Produto):
    def __init__(self,):
        super().__init__()
        self.capacidade_maxima = 0.0
        self.filtro = None

    def toArray(self):
        dados_array = super().toArray()
        dados_array['capacidade_maxima'] = self.capacidade_maxima
        return dados_array

    def add_dados_db(self, dados_db): # O atributo dados_db recebe da Classe Produto.add_dados_db
        super().add_dados_db(dados_db)
        if 'capacidade_maxima' in dados_db:
            self.capacidade_maxima = dados_db['capacidade_maxima']

    def setFiltro(self, filtro):
        self.filtro = filtro

    def getPreco(self):
        calculado = super().getPreco()
        return calculado + (self.capacidade_maxima / 3)

    def escolhaMotor(self):
        if self.filtro.capacidade_maxima <= 28:
            return 1                 
        
        if self.filtro.capacidade_maxima > 28 and self.filtro.capacidade_maxima <= 40:
            return 2           
                
        if self.filtro.capacidade_maxima > 40 and self.filtro.capacidade_maxima <= 52:
            return 3            

        if self.filtro.capacidade_maxima > 52 and self.filtro.capacidade_maxima <= 78:
            return 4
            

        if self.filtro.capacidade_maxima > 78 and self.filtro.capacidade_maxima <= 113:
            return 5   

        if self.filtro.capacidade_maxima > 113 and self.filtro.capacidade_maxima <= 176:
            return 6

        if self.filtro.capacidade_maxima > 176 and self.filtro.capacidade_maxima <= 312:
            return 7
