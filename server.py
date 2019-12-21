# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
from webapp import WebApp

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

from estruturas.dimensao import Dimensao

config = {}
    
config['motores'] = Database('motores')
config['filtros'] = Database('filtros')
config['leds'] = Database('leds')
config['vinis'] = Database('vinils')
config['areias'] = Database('areia')
config['modulos'] = Database('modulo')
config['perfis_rigido'] = Database('perfil_rigido')
config['tampas'] = Database('tampa')
config['transformadores'] = Database('transformador')
config['mantas'] = Database('manta')
config['caixas_passagem'] = Database('caixa_passagem')
config['maodeobras'] = Database('maodeobra')

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

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
        
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.app = WebApp(config)
        
        if self.path != '/' and self.path != '':
            func_name = self.path.split('?')[0].replace('/', '')
            func = getattr(self.app, func_name)
            func(self)
        else:
            func = getattr(self.app, 'main')
            func(self)
        
        self.template()
    
    def getParams(self):
        try:
            params_str = self.path.split('?')[1]
            params_array = params_str.split('&')
            params = {}
            for i in params_array:
                p = i.split('=')
                params[p[0]] = p[1]
            return params
        except:
            return {}
    
    def template(self):
        text=open("htdocs/template.html", "r")
        contents = text.read()
        contents = contents.replace('#CONTENT#', self.app.html)
        css=open("htdocs/main.css", "r")
        contents = contents.replace('</title>', '</title><style>'+css.read()+'</style>')
        self.wfile.write(contents.encode("utf-8"))


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()