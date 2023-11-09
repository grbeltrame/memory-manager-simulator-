from entrada_tabela_paginas import Entrada_TP

class TabelaPagina:

    def __init__(self):
        tamanho = 256                  # Quantidade de entradas possíveis    ====    Tamanho da Tabela de Páginas; Pode ser modificado 
        self.tamanho = tamanho
        self.entradas = []
        self.numeroPaginas = []

    def adiciona_entrada(self, numquadro):
        # Adiciona uma entrada à tabela de paginas
        entrada = Entrada_TP(numquadro)

        if (len(self.entradas) >= self.tamanho):  # Tabela de páginas cheia
            print('Tabela de Páginas cheia')

        else:                                       # Tabela tem espaço: Adiciona entrada e aumenta o timer de todas as páginas em 1 (para o LRU)
            if(numquadro not in self.numeroPaginas):
                print(numquadro)
                self.entradas.append(entrada)
                self.numeroPaginas.append(numquadro)
                print('Entrada adicionada na Tabela de Páginas')
            else:
                print(numquadro)
                print('Entrada atualizada')
                for i in range(len(self.entradas)):
                    if self.entradas[i].numquadro == numquadro:
                        self.entradas[i].timer = 0
            for i in range(len(self.entradas)):
                self.entradas[i].adiciona_timer()
        

    def mostra_tabela_paginas(self):
      # Só para Interface ou Debug
      print('\n SITUAÇÃO DA TABELA DE PÁGINAS DO PROCESSO')
      print('--------------------------')
      print(f'Tamanho da TP: {self.tamanho}')
      print(f'Entradas na TP: {len(self.entradas)}')
      for i in range(len(self.entradas)):
          self.entradas[i].mostra_entrada_TP(i)

# Testes feitos na MS e MP