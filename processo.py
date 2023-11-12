from imagem import Imagem  # Substitua 'imagem' pelo nome real do arquivo
from tabela_paginas import TabelaPagina

# No arquivo processo.py

from tabela_paginas import TabelaPagina

class Processo:
    def __init__(self, imagem, tamanho_pagina, principal, secundaria):
        self.imagem = imagem
        self.paginas = TabelaPagina(tamanho_pagina, principal, secundaria)

    def adiciona_pagina_TP(self, numpagina):
        self.paginas.adiciona_entrada(numpagina)

    def mostra_processo(self):
        print('\n SITUAÇÃO DO PROCESSO')
        print('--------------------------')
        print(f'Tamanho do processo: {self.imagem.tamanho}')
        print(f'{self.imagem.mostra_imagem()}')
        print(f'Quantidade de Páginas na TP: {len(self.paginas.entradas)} ')
