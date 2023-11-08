class Principal:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.memoria = []

    def adiciona_processo(self, processo):

        if (len(self.memoria) >= self.tamanho):     # Memória cheia
            print('Memória Principal cheia')
        else:
            self.memoria.append(processo)
            print('Processo adicionado à Memória Principal')    # Memória tem espaço: Processo é adicionado à memória



    def mostra_memoria_principal(self):
      # Só para Interface ou Debug
      print('\n SITUAÇÃO DA MEMÓRIA PRINCIPAL')
      print('--------------------------')
      print(f'Tamanho da MP: {self.tamanho}')
      print(f'Memória Alocada: {len(self.memoria)}')

    
    