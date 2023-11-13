    def termina_processo(self, numero_processo):
        processo = self.principal.encontra_processo(numero_processo)
        if processo:
            self.principal.remover_processo(processo)
            self.secundaria.remove_processo(processo)
            print(f"Processo {numero_processo} terminado.")
        else:
            print(f"Processo {numero_processo} não encontrado.")

    def executa_instrucao(self, numero_processo, endereco_logico):
        processo = self.principal.encontra_processo(numero_processo)
        if processo:
            processo.imagem.PC = endereco_logico
            processo.imagem.IR = endereco_logico
            print(f"Executando instrução para o processo {numero_processo}.")
        else:
            print(f"Processo {numero_processo} não encontrado.")

    def executa_io(self, numero_processo, dispositivo):
        print(f"Processo {numero_processo} executando operação de I/O no dispositivo {dispositivo}.")

    def realiza_leitura(self, numero_processo, endereco_logico):
        processo = self.principal.encontra_processo(numero_processo)
        if processo:
            processo.tabela_paginas.realiza_leitura(endereco_logico)
            print(f"Realizando leitura para o processo {numero_processo} no endereço {endereco_logico}.")
        else:
            print(f"Processo {numero_processo} não encontrado.")

    def realiza_escrita(self, numero_processo, endereco_logico, valor):
        processo = self.principal.encontra_processo(numero_processo)
        if processo:
            processo.tabela_paginas.realiza_escrita(endereco_logico, valor)
            print(f"Realizando escrita para o processo {numero_processo} no endereço {endereco_logico} com valor {valor}.")
        else:
            print(f"Processo {numero_processo} não encontrado.")