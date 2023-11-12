from entrada_tabela_paginas import Entrada_TP

class TabelaPagina:

    def __init__(self, tamanho_pagina, principal, secundaria):
        self.tamanho_pagina = tamanho_pagina
        self.entradas = []
        self.numeroPaginas = []
        self.principal = principal
        self.secundaria = secundaria

    def adiciona_entrada(self, numquadro):
        # Adiciona uma entrada à tabela de páginas
        entrada = Entrada_TP(numquadro)

        if len(self.entradas) >= self.tamanho_pagina:  # Tabela de páginas cheia
            print('Tabela de Páginas cheia')
        else:  # Tabela tem espaço: Adiciona entrada e aumenta o timer de todas as páginas em 1 (para o LRU)
            if numquadro not in self.numeroPaginas:
                print(numquadro)
                self.entradas.append(entrada)
                self.numeroPaginas.append(numquadro)
                print('Entrada adicionada na Tabela de Páginas')
            else:
                print(numquadro)
                print('Entrada atualizada')
                for i in range(len(self.entradas)):
                    if self.entradas[i].numquadro == numquadro:
                        self.entradas[i].timer = 0
            for i in range(len(self.entradas)):
                self.entradas[i].adiciona_timer()

    def mostra_tabela_paginas(self):
        # Só para Interface ou Debug
        print('\n SITUAÇÃO DA TABELA DE PÁGINAS DO PROCESSO')
        print('--------------------------')
        print(f'Tamanho da TP: {self.tamanho_pagina}')
        print(f'Entradas na TP: {len(self.entradas)}')
        for i in range(len(self.entradas)):
            self.entradas[i].mostra_entrada_TP(i)

    def realiza_leitura(self, endereco_logico):
        num_pagina, offset = self.calcula_pagina_e_offset(endereco_logico)
        entrada = self.entradas[num_pagina]

        if entrada is not None:
            quadro = entrada.num_quadro
            if quadro not in self.principal:
                self.move_pagina_para_mp(quadro)
            endereco_fisico = (quadro * self.tamanho_pagina) + offset
            print(f"Leitura: Endereço lógico {endereco_logico} mapeado para endereço físico {endereco_fisico}.")
        else:
            print(f"Erro de leitura: Página {num_pagina} não está na memória.")

    def realiza_escrita(self, endereco_logico, valor):
        num_pagina, offset = self.calcula_pagina_e_offset(endereco_logico)
        entrada = self.entradas[num_pagina]

        if entrada is not None:
            quadro = entrada.num_quadro
            if quadro not in self.principal:
                self.move_pagina_para_mp(quadro)
            endereco_fisico = (quadro * self.tamanho_pagina) + offset
            print(f"Escrita: Valor {valor} escrito no endereço lógico {endereco_logico}, mapeado para endereço físico {endereco_fisico}.")
        else:
            print(f"Erro de escrita: Página {num_pagina} não está na memória.")

    def calcula_pagina_e_offset(self, endereco_logico):
        num_pagina = endereco_logico // self.tamanho_pagina
        offset = endereco_logico % self.tamanho_pagina
        return num_pagina, offset

    def move_pagina_para_mp(self, num_quadro):
        # Implemente a lógica para mover a página da MS para a MP
        # usando o swapper ou a lógica desejada na sua implementação.
        # Você pode chamar o swapper aqui ou implementar a lógica diretamente.
        pass
