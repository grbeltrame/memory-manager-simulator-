# memoria_secundaria.py

class MemoriaSecundaria:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.processos = []

    def adiciona_processo(self, processo):
        existe = 0
        for i in self.processos:
            if i.imagem.id_processo == processo.imagem.id_processo:
                existe = 1
        if existe == 0:
            self.processos.append(processo)
            print(f"Processo {processo.imagem.id_processo} adicionado à Memória Secundária")
            return True
        elif existe == 1:
            return False

    def remove_processo(self, processo):
        self.processos.remove(processo)
        print(f"Processo {processo.imagem.id_processo} removido da Memória Secundária")

    def mostra_memoria_secundaria(self):
        print('\nSITUAÇÃO DA MEMÓRIA SECUNDÁRIA')
        print('--------------------------')
        print(f'Tamanho da MS: {self.tamanho}')
        print(f'Processos na MS: {len(self.processos)}')
        for processo in self.processos:
            print(processo.imagem)
