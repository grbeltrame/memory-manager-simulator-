class Entrada_TP:

    def __init__(self, numquadro):
        self.p = 1
        self.m = 0
        self.numquadro = numquadro
        self.timer = 0

    # Funções auto-explicativas

    def adiciona_timer(self):
        self.timer += 1

    def quadro_modificado(self):
        self.m = 1

    def mostra_entrada_TP(self, num):
        print(f'Entrada {num} da TP')
        print(f'Numero do quadro: {self.numquadro}')
        print(f'Tempo na TP: {self.timer}')