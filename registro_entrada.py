class Registro:

    def __init__(self, numero_processo, comando, tamanho=None, dispositivo=None, endereco=None, valor=None):
        self.numero_processo = numero_processo
        self.comando = comando

        if comando == 'C':
            self.tamanho = tamanho
        elif comando == 'I':
            self.dispositivo = dispositivo
        elif comando == 'P':
            self.endereco = endereco
        elif comando == 'R':
            self.endereco_r = endereco
        elif comando == 'W':
            self.endereco_w = endereco
            self.valor = valor