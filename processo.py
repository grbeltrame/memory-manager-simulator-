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
      # print(f'{self.imagem.mostra_imagem()}')
      print('PAGINAS DO PROCESSO')
      # for(i in self.paginas):
      #   print(f"Página: {i}")

teste_imagem = Imagem(1,0,0, "novo")
processo_teste = Processo(teste_imagem)
processo_teste.adiciona_pagina(1)
processo_teste.adiciona_pagina(2)
processo_teste.mostra_processo()