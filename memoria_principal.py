from tabela_paginas import TabelaPagina
from processo import Processo
from imagem import Imagem

class Principal:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.memoria = []
        self.qtdtabelas = 0     # Qtd de tabelas de páginas na MP (1 para cada processo)

    def adiciona_processo(self, processo):
        
        alocado = 0                         # Espaço Alocado em memória

        for i in range(len(self.memoria)):
            alocado += self.memoria[i].imagem.tamanho          # self.memoria[i] é um Processo.
        
        if alocado + processo.imagem.tamanho + (self.qtdtabelas+1)*256 >= self.tamanho:             # Memória cheia
            print('Memória Insuficiente -- Memória Principal cheia')
        else:
            self.memoria.append(processo)
            self.qtdtabelas += 1
            print('Processo adicionado à Memória Principal')       # Memória tem espaço: Processo é adicionado à memória





    def mostra_memoria_principal(self):
      # Só para Interface ou Debug
      print('\n SITUAÇÃO DA MEMÓRIA PRINCIPAL')
      print('--------------------------')
      print(f'Tamanho da MP: {self.tamanho}')
      print(f'Memória Alocada: {len(self.memoria) + self.qtdtabelas*256}')

# Teste: Criando um processo e adicionando na MP, printando tamanho do processo e quantidade de TP's

pin = Principal(100)
img = Imagem(1, 0, 20, "Bloqueado")
img.tamanho = 200
proc = Processo(img)
pin.adiciona_processo(proc)
print(pin.memoria[0].imagem.tamanho)
print(pin.qtdtabelas)
    
    