# -*- coding: utf-8 -*-

# Estrutura de Dados de Dimensão
class Dimensao:

    # Coloquei o rec_ antes do atributo recebido apenas para diferenciar do atributo da classe, mas não é necessário
    def __init__(self, rec_largura, rec_comprimento, rec_prof_inicial, rec_prof_final):
        self.largura = rec_largura
        self.comprimento = rec_comprimento
        self.prof_inicial = rec_prof_inicial
        self.prof_final = rec_prof_final
        self.largura_da_calcada = 0.6

    def toArray(self):
        dados_array = {}
        dados_array['largura'] = self.largura
        dados_array['comprimento'] = self.comprimento
        dados_array['profundidade inical'] = self.prof_inicial
        dados_array['profundidade final'] = self.prof_final
        dados_array['largura da calcada'] = self.largura_da_calcada
        return dados_array

    def setCalcada(self, calcada):
        self.largura_da_calcada = calcada

    #******** FUNÇÕES DAS DIMENSÕES DA PISCINA ********#

    def profundidade_media(self):
        return ((self.prof_inicial + self.prof_final) / 2)

    def perimetro(self):
        return (self.comprimento + self.comprimento) + (self.largura + self.largura)

    def m2facial(self):
        return (self.comprimento) * (self.largura)

    def m2parede(self):
        return (self.profundidade_media()) * (self.perimetro())

    def m2total(self):
        return (self.m2facial() + self.m2parede())

    def m3total(self):
        return (self.profundidade_media() * self.m2facial())

    def m3real(self):
        return ((self.profundidade_media()-.1) * self.m2facial())

    def area_calcada(self):
        return ((self.perimetro() * self.largura_da_calcada) + ((self.largura_da_calcada * self.largura_da_calcada) * 4))
