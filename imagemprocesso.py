class Imagem:
    def __init__(self, id_processo, PC, IR, estado):
        self.id_processo = id_processo
        self.PC = PC
        self.IR = IR
        self.estado = estado
        self.tamanho = 0  # Será atualizado quando o processo for criado

    def __str__(self):
        return f"ID: {self.id_processo}, PC: {self.PC}, IR: {self.IR}, Estado: {self.estado}, Tamanho: {self.tamanho} bytes"
