from imagem import Imagem  # Substitua 'imagem' pelo nome real do arquivo
from tabela_paginas import TabelaPagina

class Processo:


    def __init__(self, imagem):
        self.imagem = imagem
        self.paginas = TabelaPagina()


# Função para adicionar referência da pagina no processo.
# Pode ser uma pagina ou varias dependendo do tamanho do processo
    def adiciona_pagina(self, pagina):
        self.paginas.append(pagina)

    def mostra_processo(self):
      print('\n SITUAÇÃO DO PROCESSO')
      print('--------------------------')
      print(f'Tamanho do processo: {self.imagem.tamanho}')
      print(f'{self.imagem.mostra_imagem()}')
      print(f'Quantidade de Páginas na TP: {len(self.paginas.entradas)} ')