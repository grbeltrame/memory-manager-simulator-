# memoria_principal.py
import math
from tp import TabelaPagina

class MemoriaPrincipal:
    def __init__(self, tamanho, tamanho_pagina):
        self.tamanho = tamanho
        self.tamanho_pagina = tamanho_pagina
        self.qtd_quadros = tamanho // tamanho_pagina  # Calcula a quantidade total de quadros
        self.memoria = [None] * self.qtd_quadros  # Inicializa a memória como uma lista de quadros vazios
        self.quadros = {}  # Dicionário para armazenar os quadros de cada processo
        self.tabelas_paginas = {} # Dicionário para armazenar as tabelas de páginas de cada processo
        self.quadros_disponiveis = self.qtd_quadros
        self.quadro_atual = 0


    # Dentro da classe MemoriaPrincipal
    def tem_espaco_suficiente(self, processo):
        qtd_quadros_necessarios = round(processo.tamanho / self.tamanho_pagina)
        qtd_paginas_necessarias = qtd_quadros_necessarios

        # Verifica se há páginas suficientes na tabela de páginas
        tabela_paginas = self.quadros.get(processo.imagem.id_processo)
        if tabela_paginas is not None:
            paginas_alocadas = sum(1 for entrada in tabela_paginas.entradas if entrada.p == 1)
        else:
            paginas_alocadas = 0

        return paginas_alocadas + qtd_paginas_necessarias <= self.qtd_quadros


    def adiciona_processo(self, processo, memoria_secundaria):
        qtd_quadros_necessarios = round(processo.tamanho / self.tamanho_pagina)
        qtd_paginas_necessarias = qtd_quadros_necessarios

        print(f"Páginas Necessárias: {qtd_paginas_necessarias}")

        if self.tem_espaco_suficiente(processo):
           # self.memoria[processo.imagem.id_processo] = processo
            self.memoria.append(processo)
            self.quadros_disponiveis -= qtd_quadros_necessarios
            # Aloca páginas do processo na memória principal
            tabela_paginas = TabelaPagina(self.tamanho_pagina, self, memoria_secundaria)
                        # Inicializa a tabela de páginas
            tabela_paginas.inicializa_tabela(qtd_paginas_necessarias)

            self.quadros[processo.imagem.id_processo] = tabela_paginas
            
            for i in range(qtd_paginas_necessarias):
                num_quadro_livre = tabela_paginas.encontra_quadro_livre()
                if num_quadro_livre is not None:
                    entrada = tabela_paginas.entradas[num_quadro_livre]
                    entrada.numquadro = self.quadro_atual
                    self.quadro_atual += 1
                    print(f"Página {i} do processo {processo.imagem.id_processo} alocada no Quadro {self.quadro_atual}")
                else:
                    print("Não há quadros livres na MP.")
            
            self.quadros[processo.imagem.id_processo] = tabela_paginas

            self.tabelas_paginas[processo.imagem.id_processo] = []
        else:
            print(f"Memória Insuficiente -- Memória Principal cheia para o processo {processo.imagem.id_processo}.")




    def remover_processo(self, processo):
        for i in range(len(self.memoria)):
            if self.memoria[i] == processo:
                self.memoria[i] = None
    
# Dentro da classe GerenciadorMemoriaPrincipal
    def encontra_processo(self, numero_processo, processos_verificados=set()):
        for processo in self.memoria:
            if processo and processo.imagem and processo.imagem.id_processo == numero_processo:
                return processo
        return None


    def mostra_tabelas_paginas(self):
        for processo in self.memoria:
            if processo:
                print(f'\nTabela de Páginas dos Processo {processo.imagem.id_processo}')
                print('-----------------------------')
                print('Índice | Quadro')
                indice = 0
                for i in range(len(self.tabelas_paginas[processo.imagem.id_processo])):
                    print(f'{indice} |\t {self.tabelas_paginas[processo.imagem.id_processo][i]}')
                    indice += 1
                print('\n')




    def mostra_memoria_principal(self):
        print('\nSITUAÇÃO DA MEMÓRIA PRINCIPAL')
        print('--------------------------')
        print(f'Tamanho da MP: {self.tamanho}')
        print(f'Tamanho da Página: {self.tamanho_pagina}')
        print(f'Quantidade de Quadros na MP: {self.qtd_quadros}')
        print(f'Memória Alocável: {self.quadros_disponiveis} quadros ({self.quadros_disponiveis * self.tamanho_pagina} bytes)')
