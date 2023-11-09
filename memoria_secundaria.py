from imagem import Imagem
from processo import Processo

class Secundaria:
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.memoria = []

    def adiciona_processo(self, processo):

        alocado = 0                         # Espaço alocado em memória
        for i in range(len(self.memoria)):
            alocado += self.memoria[i].imagem.tamanho          
        
        if alocado + processo.imagem.tamanho >= self.tamanho:             # Memória cheia
            print('Memória Insuficiente -- Memória Secundária cheia')
        else:
            self.memoria.append(processo)
            print('Processo adicionado à Memória Secundária')       # Memória tem espaço: Processo é adicionado à memória

    def mostra_memoria_secundaria(self):
      # Só para Interface ou Debug
      print('\n SITUAÇÃO DA MEMÓRIA SECUNDÁRIA')
      print('--------------------------')
      print(f'Tamanho da MS: {self.tamanho}')
      print(f'Memória Alocada: {len(self.memoria)}')


# Teste: Criando a memória secundaria, criando um processo, adicionando o processo na sec, adicionando 3 páginas novas na TP do processo e atualizando o 20

# Teoricamente, não se adiciona página se ele tá na MS, mas isso mostra que a TP tá funcionando e a arquitetura da MS é igual a da MP


sec = Secundaria(1000000)
img = Imagem(1, 0, 20, "Bloqueado")
img.tamanho = 200
proc = Processo(img)
sec.adiciona_processo(proc)
print(sec.memoria[0].imagem.tamanho)
sec.memoria[0].adiciona_pagina_TP(20)
sec.memoria[0].adiciona_pagina_TP(30)
sec.memoria[0].adiciona_pagina_TP(45)
sec.memoria[0].adiciona_pagina_TP(20)
print(sec.memoria[0].paginas.mostra_tabela_paginas())

    