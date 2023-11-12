from tabela_paginas import TabelaPagina
from processo import Processo
from imagem import Imagem

from collections import deque

class Principal:
    def __init__(self, tamanho, tamanho_pagina):
        self.tamanho = tamanho
        self.tamanho_pagina = tamanho_pagina
        self.memoria = []

    def adiciona_processo(self, processo):
        qtd_quadros_necessarios = (processo.imagem.tamanho + self.tamanho_pagina - 1) // self.tamanho_pagina
        if len(self.memoria) + qtd_quadros_necessarios <= self.tamanho // self.tamanho_pagina:
            processo.tabela_paginas.inicializa_tabela(qtd_quadros_necessarios)
            self.memoria.append(processo)
            print('Processo adicionado à Memória Principal')
        else:
            print('Memória Insuficiente -- Memória Principal cheia')

    def mostra_memoria_principal(self):
        print('\n SITUAÇÃO DA MEMÓRIA PRINCIPAL')
        print('--------------------------')
        print(f'Tamanho da MP: {self.tamanho}')
        print(f'Memória Alocada: {len(self.memoria) * self.tamanho_pagina} ({len(self.memoria)} páginas)')

    def liberar_quadros(self, processo):
        # Remove os quadros alocados para o processo especificado
        self.memoria = [quadro for quadro in self.memoria if quadro != processo]

    def mostra_memoria_principal(self):
        print('\nSITUAÇÃO DA MEMÓRIA PRINCIPAL')
        print('--------------------------')
        print(f'Tamanho da MP: {self.tamanho}')
        print(f'Tamanho da Página: {self.tamanho_pagina}')
        print(f'Memória Alocada: {len(self.memoria)} quadros ({len(self.memoria) * self.tamanho_pagina} bytes)')
        print(f'Quantidade de Tabelas na MP: {self.qtdtabelas}')

    
    