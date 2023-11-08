class Secundaria:
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.memoria = []

    def adiciona_processo(self, processo):

        if (len(self.memoria) >= self.tamanho):          # Memória cheia
            print('Memória Secundária cheia')
        else:
            self.memoria.append(processo)
            print('Processo adicionado à Memória Secundária')       # Memória tem espaço: Processo é adicionado à memória

    def mostra_memoria_secundaria(self):
      # Só para Interface ou Debug
      print('\n SITUAÇÃO DA MEMÓRIA SECUNDÁRIA')
      print('--------------------------')
      print(f'Tamanho da MS: {self.tamanho}')
      print(f'Memória Alocada: {len(self.memoria)}')

    