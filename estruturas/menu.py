class Menu:

    # def __init__(self):
    #     self.menus

    def menu_inicial(self):
        print('**************************************')
        print(f'1 - Digitar Dimensão\n2 - Escolher Vinil\n3 - Escolher Filtro')
        print(f'4 - Escolher Led\n5 - Ver Configuracoes Escolhidas\n6 - Calcular Preço')
        print(f'7 - Testando Objetos e Métodos\n0 - Sair do Sistema')
        print('**************************************')
        escolha = None
        while escolha == None:
            try:
                escolha = int(input('Digite uma opção: '))
                if escolha >= 0 and escolha < 12:
                    return escolha
            except:
                escolha = None

    def digita_dimensao(self):
        dim = [0, 0, 0, 0, 0]
        while dim[0] == 0 or dim[1] == 0 or dim[2] == 0 or dim[3] == 0 or dim[4] == 0:
            try:
                if dim[0] == 0:
                    escolha = float(input('\nDigite a largura: '))
                    dim[0] = escolha
                elif dim[1] == 0:
                    escolha = float(input('\nDigite o comprimento: '))
                    dim[1] = escolha
                elif dim[2] == 0:
                    escolha = float(input('\nDigite a profundidade inicial: '))
                    dim[2] = escolha
                elif dim[3] == 0:
                    escolha = float(input('\nDigite a profundidade final: '))
                    dim[3] = escolha
                elif dim[4] == 0:
                    escolha = float(0.6) # largura da calcada é um valor fixo, mas poderá ser alterado nas configurações.
                    dim[4] = escolha
            except:
                escolha = None
        return dim