# gerenciador_memoria.py
import math
from mp import MemoriaPrincipal
from ms import MemoriaSecundaria
from processo import Processo
from imagem import Imagem
from swapper import Swapper

class GerenciadorMemoria:
    def __init__(self, tamanho_mp, tamanho_ms, tamanho_pagina, tamanho_endereco):
        self.tamanho_mp = tamanho_mp
        self.tamanho_ms = tamanho_ms
        self.tamanho_pagina = tamanho_pagina
        self.fila_prontos_suspenso = []
        self.fila_executando = []
        self.fila_bloqueados_suspenso = []
        self.fila_terminados = []
        self.tamanho_endereco = tamanho_endereco
        self.principal = MemoriaPrincipal(tamanho_mp, tamanho_pagina)
        self.secundaria = MemoriaSecundaria(tamanho_ms)

    def mostra_situacao_memoria(self):
        print('\nSITUAÇÃO DA MEMÓRIA PRINCIPAL')
        print('-----------------------------')
        print(f'Tamanho da MP: {self.principal.tamanho}')
        print(f'Espaço Total: {self.principal.qtd_quadros} quadros')
        print(f'Espaço Alocável: {self.principal.quadros_disponiveis} quadros  /  {self.principal.quadros_disponiveis * 256} bytes')

        for processo in self.principal.memoria:
            if processo:
                print(f'\nQuadros na MP do Processo {processo.imagem.id_processo}:')
                print('-----------------------------')
                print('Página  |    Quadro')
                
                # Itera sobre as entradas da tabela de páginas
                pagina = 0
                for entrada in self.principal.quadros[processo.imagem.id_processo].entradas:
                    print(f'  {pagina}\t|\t{entrada.numquadro}')
                    pagina += 1
                print("\n")


    def executa_comandos(self, arquivo):
        with open(arquivo, 'r') as f:
            for linha in f:
                partes = linha.split()

                # Verificar se há informações suficientes na linha
                if len(partes) < 2:
                    print("Formato de comando inválido na linha:", linha)
                    continue  # Pular para a próxima iteração do loop

                numero_processo = partes[0]

                if partes[1] == 'C':
                    # Verifica se há informações suficientes para processos de criação (com 4 partes)
                    if len(partes) < 3:
                        print("Formato de comando inválido na linha:", linha)
                        continue  # Pular para a próxima iteração do loop

                    tamanho_processo_str = partes[2]
                    self.cria_processo(numero_processo, tamanho_processo_str)
                elif partes[1] == 'T':
                    self.termina_processo(numero_processo)
                elif partes[1] == 'P':
                    end = partes[2].lstrip('(')
                    end = list(end)
                    end.pop()
                    end.pop()
                    endereco_binario = ""
                    for i in end:
                        endereco_binario += i


                    # Verifica se o endereço_binario não está vazio
                    if endereco_binario:
                        endereco_logico = int(endereco_binario, 2)
                        self.executa_instrucao(numero_processo, endereco_logico)
                    else:
                        print(f"Formato de comando inválido na linha: {linha}")
                elif partes[1] == 'I':
                    dispositivo = partes[2]
                    self.executa_io(numero_processo, dispositivo)
                elif partes[1] == 'R':
                    endereco_logico = int(partes[2])
                    self.realiza_leitura(numero_processo, endereco_logico)
                elif partes[1] == 'W':
                    # Verifica se há informações suficientes para comandos de escrita (com 4 partes)
                    if len(partes) < 4:
                        print("Formato de comando inválido na linha:", linha)
                        continue  # Pular para a próxima iteração do loop

                    endereco_logico = int(partes[2])
                    valor = int(partes[3])
                    self.realiza_escrita(numero_processo, endereco_logico, valor)

            # Mostra a situação da memória após a execução dos comandos
            self.mostra_situacao_memoria()

    def cria_processo(self, numero_processo, tamanho_processo_str):
        self.mostra_situacao_memoria()

        # Converte o valor do tamanho do processo para inteiro
        tamanho_processo = int(tamanho_processo_str)

        imagem = Imagem(numero_processo, 0, 0, 'NOVO')
        imagem.tamanho = tamanho_processo
        processo = Processo(imagem, tamanho_processo, self.principal, self.secundaria)  # Ajuste nesta linha

        # Adiciona o processo à Memória Secundária
        self.secundaria.adiciona_processo(processo)
        processo.atualiza_estado("Pronto/Suspenso")
        # Adiciona o processo à fila de processos prontos/suspenso
        self.fila_prontos_suspenso.append(processo)

        # Verifica se há espaço disponível na memória principal antes de adicionar o processo
        if self.principal.tem_espaco_suficiente(processo):
            self.principal.adiciona_processo(processo, self.secundaria)
            processo.atualiza_estado("Pronto")
            print(f"Processo {numero_processo} criado com sucesso.")
        else:
            print(f"Memória Insuficiente -- Memória Principal cheia para o processo {numero_processo}.")

            # Exibe o estado da memória principal após a tentativa de criação do processo
            self.mostra_situacao_memoria()

            print("Antes do Swapper - Memória Principal:")
            print(f"Tamanho da Memória Principal: {self.principal.tamanho}")
            print(f"Espaço Alocado: {len(self.principal.memoria) + self.principal.qtd_quadros * 256}")

            # Chama o Swapper para liberar espaço na memória principal
            # Após adicionar o processo à memória principal
            swapper = Swapper()
            swapper.move_processo(processo, self.principal, self.secundaria)

            # Atualiza o estado do processo após o Swapper
            if processo.estado == "Pronto":
                processo.atualiza_estado("Pronto/Suspenso")
            elif processo.estado == "Bloqueado":
                processo.atualiza_estado("Bloqueado/Suspenso")

            # Tenta adicionar o processo à memória principal novamente
            if self.principal.tem_espaco_suficiente(processo):
                self.principal.adiciona_processo(processo , self.secundaria)
                processo.atualiza_estado("Pronto")
                print(f"Processo {numero_processo} criado com sucesso após Swapper.")
            else:
                print("Memória Insuficiente -- Memória Principal cheia mesmo após Swapper.")

        # Exibe o estado da memória principal após a tentativa de adição do processo
        self.mostra_situacao_memoria()

    # Dentro da classe GerenciadorMemoria, método que conclui um processo
    def conclui_processo(self, processo):
        # Remove o processo da fila de executando
        self.fila_executando.remove(processo)

        # Adiciona o processo à fila de terminados
        self.fila_terminados.append(processo)


        # Dentro da classe GerenciadorMemoria, método que bloqueia ou suspende um processo
    def bloqueia_ou_suspende_processo(self, processo):
        # Remove o processo da fila de executando
        self.fila_executando.remove(processo)

        # Adiciona o processo à fila de bloqueados/suspenso
        self.fila_bloqueados_suspenso.append(processo)


    def move_para_executando(self, processo):
        # Remove o processo da fila de prontos/suspenso
        self.fila_prontos_suspenso.remove(processo)

        # Adiciona o processo à fila de executando
        self.fila_executando.append(processo)

    def termina_processo(self, numero_processo):
        processo = self.principal.encontra_processo(numero_processo, set())

        if processo:
            self.principal.remover_processo(processo)
            self.secundaria.remove_processo(processo)
            print(f"Processo {numero_processo} terminado.")
        else:
            print(f"Processo {numero_processo} não encontrado.")

    def executa_instrucao(self, numero_processo, endereco_logico):
        processo = self.principal.encontra_processo(numero_processo, set())

        if processo:
            processo.imagem.PC = endereco_logico
            processo.imagem.IR = endereco_logico
            if math.floor(endereco_logico/255) not in self.principal.tabelas_paginas[processo.imagem.id_processo]:
                self.principal.tabelas_paginas[processo.imagem.id_processo].append(math.floor(endereco_logico/255))
            print(f"Executando instrução do endereço lógico {endereco_logico} para o processo {numero_processo}.")
            gerenciador.principal.mostra_tabelas_paginas()
        else:
            print(f"Processo {numero_processo} não encontrado.")

    def executa_io(self, numero_processo, dispositivo):
        print(f"Processo {numero_processo} executando operação de I/O no dispositivo {dispositivo}.")

    def realiza_leitura(self, numero_processo, endereco_logico):
        processo = self.principal.encontra_processo(numero_processo, set())
        if processo:
       #     self.realiza_leitura(numero_processo, endereco_logico)
            print(f"Realizando leitura para o processo {numero_processo} no endereço lógico {endereco_logico}.")
            if math.floor(endereco_logico/255) not in self.principal.tabelas_paginas[processo.imagem.id_processo]:
                self.principal.tabelas_paginas[processo.imagem.id_processo].append(math.floor(endereco_logico/255))
        else:
            print(f"Processo {numero_processo} não encontrado.")

    def realiza_escrita(self, numero_processo, endereco_logico, valor):
        processo = self.principal.encontra_processo(numero_processo, set())

        if processo:
            print(f"Realizando escrita para o processo {numero_processo} no endereço lógico {endereco_logico} com valor {valor}.")
            if math.floor(endereco_logico/255) not in self.principal.tabelas_paginas[processo.imagem.id_processo]:
                self.principal.tabelas_paginas[processo.imagem.id_processo].append(math.floor(endereco_logico/255))
        else:
            print(f"Processo {numero_processo} não encontrado.")



# Exemplo de uso
gerenciador = GerenciadorMemoria(tamanho_mp=4194304, tamanho_ms=33554432, tamanho_pagina=256, tamanho_endereco=12)
gerenciador.executa_comandos('entrada.txt')

gerenciador.principal.mostra_tabelas_paginas()

# Mostra o estado da memória principal ao final da simulação
#gerenciador.principal.mostra_memoria_principal()

# Mostra o estado da memória secundária ao final da simulação
gerenciador.secundaria.mostra_memoria_secundaria()