# memoria_principal.py
import math
from tp import TabelaPagina

class MemoriaPrincipal:
    def __init__(self, tamanho, tamanho_pagina):
        self.tamanho = tamanho
        self.tamanho_pagina = tamanho_pagina
        self.qtd_quadros = tamanho // tamanho_pagina  # Calcula a quantidade total de quadros
        self.memoria = [None] * self.qtd_quadros  # Inicializa a memória como uma lista de quadros vazios
        self.tabelas_paginas = {}  # Dicionário para armazenar as tabelas de páginas de cada processo



    # Dentro da classe MemoriaPrincipal
    def tem_espaco_suficiente(self, processo):
        qtd_quadros_necessarios = processo.tamanho // self.tamanho_pagina
        qtd_paginas_necessarias = math.ceil(qtd_quadros_necessarios / (self.qtd_quadros * 1.0))

        # Verifica se há páginas suficientes na tabela de páginas
        tabela_paginas = self.tabelas_paginas.get(processo.imagem.id_processo)
        if tabela_paginas is not None:
            paginas_alocadas = sum(1 for entrada in tabela_paginas.entradas if entrada.p == 1)
        else:
            paginas_alocadas = 0

        print(f"Páginas alocadas: {paginas_alocadas}, Páginas necessárias: {qtd_paginas_necessarias}")

        return paginas_alocadas + qtd_paginas_necessarias <= self.qtd_quadros


    def adiciona_processo(self, processo, memoria_secundaria):
        qtd_quadros_necessarios = processo.tamanho // self.tamanho_pagina
        qtd_paginas_necessarias = (qtd_quadros_necessarios + self.qtd_quadros - 1) // self.qtd_quadros

        print(f"Antes da adição - Processo: {processo}, Páginas Necessárias: {qtd_paginas_necessarias}")

        if self.tem_espaco_suficiente(processo):
            # Aloca páginas do processo na memória principal
            tabela_paginas = TabelaPagina(self.tamanho_pagina, self, memoria_secundaria)
                        # Inicializa a tabela de páginas
            tabela_paginas.inicializa_tabela(qtd_paginas_necessarias)

            print(f"Tabela de Páginas criada: {tabela_paginas}")
            self.tabelas_paginas[processo.imagem.id_processo] = tabela_paginas
            
            for i in range(qtd_paginas_necessarias):
                num_quadro_livre = tabela_paginas.encontra_quadro_livre()
                if num_quadro_livre is not None:
                    entrada = tabela_paginas.entradas[num_quadro_livre]
                    entrada.p = 1
                    entrada.m = 0
                    entrada.numquadro = num_quadro_livre
                    entrada.timer = 0
                    print(f"Página {i} do processo {processo.imagem.id_processo} alocada no Quadro {num_quadro_livre}")
                else:
                    print("Não há quadros livres na tabela de páginas.")
            
            self.tabelas_paginas[processo.imagem.id_processo] = tabela_paginas
        else:
            print(f"Memória Insuficiente -- Memória Principal cheia para o processo {processo.imagem.id_processo}.")




    def remover_processo(self, processo):
        for i in range(len(self.memoria)):
            if self.memoria[i] == processo:
                self.memoria[i] = None
    
# Dentro da classe GerenciadorMemoriaPrincipal
    def encontra_processo(self, numero_processo, processos_verificados=set()):
        for quadro in self.memoria:
            if quadro and quadro.imagem and quadro.imagem.id_processo == numero_processo:
                return quadro.imagem
            elif quadro and quadro.tabela_paginas and quadro.tabela_paginas.entradas:
                for entrada in quadro.tabela_paginas.entradas:
                    if entrada.p == 1 and entrada.numquadro not in processos_verificados:
                        processos_verificados.add(entrada.numquadro)
                        processo = self.encontra_processo(numero_processo, processos_verificados)
                        if processo:
                            return processo
        return None



    




    def mostra_memoria_principal(self):
        print('\nSITUAÇÃO DA MEMÓRIA PRINCIPAL')
        print('--------------------------')
        print(f'Tamanho da MP: {self.tamanho}')
        print(f'Tamanho da Página: {self.tamanho_pagina}')
        print(f'Quantidade de Quadros na MP: {self.qtd_quadros}')
        print(f'Memória Alocada: {len(self.memoria)} quadros ({len(self.memoria) * self.tamanho_pagina} bytes)')
