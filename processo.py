# processo.py

from tq import TabelaQuadro

class Processo:
    def __init__(self, imagem, tamanho, principal, secundaria):
        self.imagem = imagem
        self.tamanho = tamanho
        self.estado = "Novo" 
        self.timer = 0

    def atualiza_estado(self, novo_estado):
        print(f"Processo {self.imagem.id_processo} está transitando do estado {self.estado} para {novo_estado}.")
        self.estado = novo_estado
        self.imagem.estado = novo_estado

