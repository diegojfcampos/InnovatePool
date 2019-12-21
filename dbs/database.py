import ast
import json


class Database:
    def __init__(self, tabela):
        self.file = open('./dbs/' + tabela + '.json', 'r')
        self.table = tabela
        self.db = json.dumps(ast.literal_eval(self.file.read()))

    def lista(self):
        #Teste
        #lista = json.loads(self.db)[self.table]
        #print(f'\nACESSANDO LISTA() CLASSE DB')
        #print(f'\nOUTPUT: {lista}\n')
        #Fim Teste
        return json.loads(self.db)[self.table]

    def listaItem(self, item):
        #Teste
        #listitem = json.loads(self.db)[item]
        #print(f'\nACESSANDO LISTAITEM() CLASSE DB')
        #print(f'\nOUTPUT: {listitem}\n')
        #Fim Teste
        return json.loads(self.db)[item]

    def find(self, id):
        for row in json.loads(self.db)[self.table]:
            if row['id'] == id:
                return row
        return None
