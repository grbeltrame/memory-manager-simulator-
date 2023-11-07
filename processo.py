from imagem import Imagem  # Substitua 'imagem' pelo nome real do arquivo


class Processo:

    def __init__(self, imagem):
        self.imagem = imagem
        self.paginas = []


# Função para adicionar referência da pagina no processo.
# Pode ser uma pagina ou varias dependendo do tamanho do processo
    def adiciona_pagina(self, pagina):
        self.paginas.append(pagina)

    def mostra_processo(self):
      print('\n SITUAÇÃO DO PROCESSO')
      print('--------------------------')
      print(f'Tamanho do processo: {self.imagem.tamanho}')
      print(f'{self.imagem.mostra_imagem()}')
      print('PAGINAS DO PROCESSO')
      for i in self.paginas:
          if i == None:
              print('Nenhuma pagina alocada')
          else:
              print(f"{i}\n")
          