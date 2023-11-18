# entrada_tp.py

class Entrada_TP:
    def __init__(self, numquadro, tamanho_pagina):
        self.p = 0
        self.m = 0
        self.numquadro = numquadro
        self.timer = 0
        self.tamanho_pagina = tamanho_pagina

    def adiciona_timer(self):
        self.timer += 1

    def quadro_modificado(self):
        self.m = 1

    def mostra_entrada_TP(self, num):
        print(f'Entrada {num} da TP')
        print(f'Número do quadro: {self.numquadro}')
        print(f'Tempo na TP: {self.timer}')
