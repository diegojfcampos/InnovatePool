# -*- coding: utf-8 -*-


class Produto:
    def __init__(self):
        self.id = 0
        self.fornecedor = ''        
        self.marca = ''
        self.modelo = ''
        self.custo = 0.0   
        self.margem_de_lucro = 0.0
        self.preco = 0.0
        

    def toArray(self):
        dados_array = {}
        dados_array['id'] = self.id
        dados_array['fonecedor'] = self.fornecedor
        dados_array['marca'] = self.marca
        dados_array['modelo'] = self.modelo
        dados_array['custo'] = self.custo
        dados_array['marge_de_lucro'] = self.margem_de_lucro            
        dados_array['preco'] = self.preco

        return dados_array

# --------------------------------------------------------------------------------------------------
####--   Se o termo 'id' estiver em dados_db, guarda em self.id   --####

    def add_dados_db(self, dados_db): # O atributo dados_db recebe dado da Classe Webapp.motores
        if dados_db == None:
            return
        if 'id' in dados_db:
            self.id = dados_db['id']
        if 'fornecedor' in dados_db:
            self.fornecedor = dados_db['fornecedor']
        if 'marca' in dados_db:
            self.marca = dados_db['marca']      
        if 'modelo' in dados_db:
            self.modelo = dados_db['modelo']
        if 'custo' in dados_db:
            self.custo = dados_db['custo']
        if 'margem_de_lucro' in dados_db:
            self.margem_de_lucro = dados_db['margem_de_lucro']        
        if 'preco' in dados_db:
            self.preco = dados_db['preco']

    def getPreco(self):
        return self.preco