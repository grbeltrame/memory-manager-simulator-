from entrada_tabela_paginas import Entrada_TP

class TabelaPagina:

    def __init__(self):
        tamanho = 1024                  # Tamanho aleatório pra inicializar a Tabela de Páginas; Pode ser modificado 
        self.tamanho = tamanho
        self.entradas = []

    def adiciona_entrada(self, numquadro):
        # Adiciona uma entrada à tabela de paginas

        if (len(self.entradas) >= self.tamanho):  # Tabela de páginas cheia
            print('Tabela de Páginas cheia')

        else:                                       # Tabela tem espaço: Adiciona entrada e aumenta o timer de todas as páginas em 1 (para o LRU)
            entrada = Entrada_TP(numquadro)
            self.entradas.append(entrada)

            for i in range(self.entradas.length):
                self.entradas[i].adiciona_timer()

            print('Entrada adicionada na Tabela de Páginas')

    def mostra_tabela_paginas(self):
      # Só para Interface ou Debug
      print('\n SITUAÇÃO DA TABELA DE PÁGINAS DO PROCESSO')
      print('--------------------------')
      print(f'Tamanho da TP: {self.tamanho}')
      print(f'Entradas na TP: {len(self.entradas)}')
      for i in range(len(self.entradas)):
          self.entradas[i].mostra_entrada_TP(i)

        