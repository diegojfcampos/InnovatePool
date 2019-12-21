class MO:

    def __init__(self):
        
        self.escavacao = 0.0
        self.remocao_terra = 0.0
        self.construcao = 0.0
        self.instalacao_filtro = 0.0
        self.instalacao_moto_bomba = 0.0
        self.instalacao_vinil = 0.0
        self.dimensoes = None

    def toArray(self):
        dados_array = {}
        dados_array['escavacao'] = self.escavacao
        dados_array['remocao_terra'] = self.remocao_terra
        dados_array['construcao'] = self.construcao
        dados_array['instalacao_filtro'] = self.instalacao_filtro
        dados_array['instalacao_moto_bomba'] = self.instalacao_moto_bomba
        dados_array['instalacao_vinil'] = self.instalacao_vinil            

        return dados_array

    def add_dados_db(self, dados_db): # O atributo dados_db recebe dado da Classe Webapp.motores

        escavacao = dados_db.listaItem('escavacao')
        construcao = dados_db.listaItem('construcao')
        remocao = dados_db.listaItem('remocao_de_terra')
        intal_filtro = dados_db.listaItem('instalacao_filtro')
        intal_motobomba = dados_db.listaItem('instalacao_motobomba')
        intal_vinil = dados_db.listaItem('instalacao_vinil')

        if dados_db == None:
            return
        for item in escavacao:
            self.setEscavacao(item['preco'])

        for item in construcao:
            self.setConstrucao(item['preco'])
        
        for item in remocao:
            self.setRemocaoTerra(item['preco'])
        
        for item in intal_filtro:
            self.setInstalacaoFiltro(item['preco'])
        
        for item in intal_motobomba:
            self.setInstalacaoMotor(item['preco'])

        for item in intal_vinil:
            self.setInstalacaoVinil(item['preco'])        


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
