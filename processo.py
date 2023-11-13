# processo.py

from tp import TabelaPagina

class Processo:
    def __init__(self, imagem, tamanho, principal, secundaria):
        self.imagem = imagem
        self.tamanho = tamanho
        self.estado = "Novo"  # Estado inicialself.tabela_paginas = TabelaPagina(self, principal, secundaria, qtd_paginas_necessarias)

    def atualiza_estado(self, novo_estado):
        print(f"Processo {self.imagem.id_processo} está transitando do estado {self.estado} para {novo_estado}.")
        self.estado = novo_estado

