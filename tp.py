# tp.py

from entrada import Entrada_TP

class TabelaPagina:
    def __init__(self, tamanho_pagina, memoria_principal, memoria_secundaria):
        self.tamanho_pagina = tamanho_pagina
        self.memoria_principal = memoria_principal
        self.memoria_secundaria = memoria_secundaria
        self.entradas = []

        

    def inicializa_tabela(self, qtd_quadros_necessarios):
        for i in range(qtd_quadros_necessarios):
            self.entradas.append(Entrada_TP(i, self.tamanho_pagina))

    def encontra_quadro_livre(self):
        for i, entrada in enumerate(self.entradas):
            if entrada.p == 0:
                return i
        return None


    def substitui_pagina(self, processo, endereco_logico):
        quadro_livre = self.encontra_quadro_livre()
        if quadro_livre is not None:
            entrada_substituida = self.entradas[quadro_livre]
            processo.paginas.quadro_modificado(entrada_substituida.numquadro)
            entrada_substituida.p = 1
            entrada_substituida.m = 0
            entrada_substituida.numquadro = quadro_livre
            entrada_substituida.timer = 0
            print(f'Página {endereco_logico // self.tamanho_pagina} substituída na MP')
        else:
            print('Não há quadros livres para substituição')
