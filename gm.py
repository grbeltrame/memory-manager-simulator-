from memoria_principal import Principal
from memoria_secundaria import Secundaria
from processo import Processo
from imagem import Imagem
from swapper import Swapper
# Código principal


class GerenciadorMemoria:
    def __init__(self, tamanho_mp, tamanho_ms, tamanho_pagina, tamanho_endereco):
        self.tamanho_mp = tamanho_mp
        self.tamanho_ms = tamanho_ms
        self.tamanho_pagina = tamanho_pagina
        self.tamanho_endereco = tamanho_endereco
        self.principal = Principal(tamanho_mp, tamanho_pagina)  # Passa o tamanho da página
        self.secundaria = Secundaria(tamanho_ms)

    def executa_comandos(self, arquivo):
        with open(arquivo, 'r') as f:
            for linha in f:
                partes = linha.split()
                numero_processo = partes[0]

                if partes[1] == 'C':
                    tamanho_processo = int(partes[2].rstrip('MB'))
                    self.cria_processo(numero_processo, tamanho_processo)
                elif partes[1] == 'T':
                    self.termina_processo(numero_processo)
                elif partes[1] == 'P':
                    endereco_logico = int(partes[2].lstrip('(').rstrip(')2'))
                    self.executa_instrucao(numero_processo, endereco_logico)
                elif partes[1] == 'I':
                    dispositivo = partes[2]
                    self.executa_io(numero_processo, dispositivo)
                elif partes[1] == 'R':
                    endereco_logico = int(partes[2])
                    self.realiza_leitura(numero_processo, endereco_logico)
                elif partes[1] == 'W':
                    endereco_logico = int(partes[2])
                    valor = int(partes[3])
                    self.realiza_escrita(numero_processo, endereco_logico, valor)

    def cria_processo(self, numero_processo, tamanho_processo, principal, secundaria):
        imagem = Imagem(numero_processo, 0, 0, 'NOVO')
        imagem.tamanho = tamanho_processo
        processo = Processo(imagem, imagem.tamanho ,principal, secundaria)
        self.principal.adiciona_processo(processo)


        # Verifica se a memória principal está cheia
        if len(self.principal.memoria) + self.principal.qtdtabelas * 256 >= self.principal.tamanho:
            print("Antes do Swapper - Memória Principal:")
            print(f"Tamanho da Memória Principal: {self.principal.tamanho}")
            print(f"Espaço Alocado: {len(self.principal.memoria) + self.principal.qtdtabelas * 256}")

            # Chama o Swapper para liberar espaço na memória principal
            swapper = Swapper()  # ou crie uma instância do Swapper de acordo com sua implementação
            swapper.move_processo(processo, self.principal, self.secundaria)


        # Agora, tenta adicionar o processo à memória principal novamente
        if len(self.principal.memoria) + self.principal.qtdtabelas * 256 < self.principal.tamanho:
            self.principal.adiciona_processo(processo)
        else:
            print("Memória Insuficiente -- Memória Principal cheia")

        # Agora, verifica se a memória principal está vazia antes de tentar acessar o primeiro elemento
        if len(self.principal.memoria) > 0:
            print(self.principal.memoria[0].imagem.tamanho)
        else:
            print("Memória principal vazia")

    def swapper(self, novo_processo):
        # Adicione aqui a lógica do Swapper para liberar espaço na memória principal
        # Você precisa chamar move_processo do Swapper e passar os parâmetros necessários
        Swapper.move_processo(novo_processo, self.principal, self.secundaria)

    def termina_processo(self, numero_processo):
        processo = self.principal.encontra_processo(numero_processo)
        if processo:
            self.principal.remove_processo(processo)
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
            processo.paginas.realiza_leitura(endereco_logico)
            print(f"Realizando leitura para o processo {numero_processo} no endereço {endereco_logico}.")
        else:
            print(f"Processo {numero_processo} não encontrado.")

    def realiza_escrita(self, numero_processo, endereco_logico, valor):
        processo = self.principal.encontra_processo(numero_processo)
        if processo:
            processo.paginas.realiza_escrita(endereco_logico, valor)
            print(f"Realizando escrita para o processo {numero_processo} no endereço {endereco_logico} com valor {valor}.")
        else:
            print(f"Processo {numero_processo} não encontrado.")

# Exemplo de uso
gerenciador = GerenciadorMemoria(tamanho_mp=1024, tamanho_ms=4096, tamanho_pagina=256, tamanho_endereco=12)
gerenciador.executa_comandos('entrada.txt')
