from tabela_paginas import TabelaPagina
from processo import Processo
from imagem import Imagem

class Principal:
    def __init__(self, tamanho, tamanho_pagina):
        self.tamanho = tamanho
        self.tamanho_pagina = tamanho_pagina
        self.memoria = []

    def adiciona_processo(self, processo):
        qtd_quadros_necessarios = (processo.imagem.tamanho + self.tamanho_pagina - 1) // self.tamanho_pagina

        if len(self.memoria) + qtd_quadros_necessarios <= self.tamanho:
            tabela_paginas = TabelaPagina(self.tamanho_pagina)
            tabela_paginas.inicializa_tabela(qtd_quadros_necessarios)

            processo.tabela_paginas = tabela_paginas
            self.memoria.extend([processo] * qtd_quadros_necessarios)
            
            print(f"Processo {processo.imagem.id_processo} adicionado à Memória Principal")
            return True
        else:
            print("Memória Insuficiente -- Memória Principal cheia")
            return False

    def remover_processo(self, processo):
        self.memoria = [quadro for quadro in self.memoria if quadro != processo]

    def mostra_memoria_principal(self):
        print('\nSITUAÇÃO DA MEMÓRIA PRINCIPAL')
        print('--------------------------')
        print(f'Tamanho da MP: {self.tamanho}')
        print(f'Tamanho da Página: {self.tamanho_pagina}')
        print(f'Memória Alocada: {len(self.memoria)} quadros ({len(self.memoria) * self.tamanho_pagina} bytes)')

    def liberar_quadros(self, processo):
        # Remove os quadros alocados para o processo especificado
        self.memoria = [quadro for quadro in self.memoria if quadro != processo]

# Teste básico
imagem1 = Imagem(1, 0, 0, 'NOVO')
imagem1.tamanho = 512

imagem2 = Imagem(2, 0, 0, 'NOVO')
imagem2.tamanho = 256

principal = Principal(tamanho=1024, tamanho_pagina=256)

processo1 = Processo(imagem1)
processo2 = Processo(imagem2)

principal.adiciona_processo(processo1)
principal.adiciona_processo(processo2)

principal.mostra_memoria_principal()
