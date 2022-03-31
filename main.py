# Simular um dados de 6 lados

import random

class Main:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'


    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValordoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta!')


    def GerarValordoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = Main()
simulador.Iniciar()