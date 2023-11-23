# gerenciador_memoria.py
import math
from mp import MemoriaPrincipal
from ms import MemoriaSecundaria
from processo import Processo
from imagem import Imagem
from swapper import Swapper
from entrada import *

class GerenciadorMemoria:
    def __init__(self, tamanho_mp, tamanho_ms, tamanho_pagina):
        self.tamanho_mp = tamanho_mp
        self.tamanho_ms = tamanho_ms
        self.tamanho_pagina = tamanho_pagina
        self.fila_prontos_suspenso = []
        self.fila_executando = []
        self.fila_bloqueados_suspenso = []
        self.fila_terminados = []
        self.principal = MemoriaPrincipal(tamanho_mp, tamanho_pagina)
        self.secundaria = MemoriaSecundaria(tamanho_ms)

    def mostra_situacao_memoria(self):
        print('\nSITUAÇÃO DA MEMÓRIA PRINCIPAL')
        print('-----------------------------')
        print(f'Tamanho da MP: {self.principal.tamanho}')
        print(f'Espaço Total: {self.principal.qtd_quadros} quadros')
        print(f'Espaço Alocável: {self.principal.quadros_disponiveis} quadros  /  {self.principal.quadros_disponiveis * 256} bytes')
        print("\n        Quadros dos Processos        ")
        sem_processo = 1
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
                sem_processo = 0
        if sem_processo == 1:
           print("\n    Não há nenhum Processo na MP        ")

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
                        self.cria_processo(numero_processo, tamanho_processo_str)
                        self.executa_instrucao(numero_processo, endereco_logico)
                    else:
                        print(f"Formato de comando inválido na linha: {linha}")
                elif partes[1] == 'I':
                    dispositivo = partes[2]
                    self.cria_processo(numero_processo, tamanho_processo_str)
                    self.executa_io(numero_processo, dispositivo)
                elif partes[1] == 'R':
                    endereco_logico = int(partes[2])
                    self.cria_processo(numero_processo, tamanho_processo_str)
                    self.realiza_leitura(numero_processo, endereco_logico)
                    
                elif partes[1] == 'W':
                    # Verifica se há informações suficientes para comandos de escrita (com 4 partes)
                    if len(partes) < 4:
                        print("Formato de comando inválido na linha:", linha)
                        continue  # Pular para a próxima iteração do loop

                    endereco_logico = int(partes[2])
                    valor = int(partes[3])
                    self.cria_processo(numero_processo, tamanho_processo_str)
                    self.realiza_escrita(numero_processo, endereco_logico, valor)

                processo = self.principal.encontra_processo(numero_processo, set())
                for i in self.principal.memoria:
                    if i != None:
                        if processo == i:
                            i.timer = 0
                        else:
                            i.timer += 1


            # Mostra a situação da memória após a execução dos comandos
     #       self.mostra_situacao_memoria()

    def cria_processo(self, numero_processo, tamanho_processo_str):
        print('\n')
       # self.mostra_situacao_memoria()

        # Converte o valor do tamanho do processo para inteiro
        tamanho_processo = int(tamanho_processo_str)

        imagem = Imagem(numero_processo, 0, 0, 'NOVO')
        imagem.tamanho = tamanho_processo
        processo = Processo(imagem, tamanho_processo, self.principal, self.secundaria)  # Ajuste nesta linha

        # Adiciona o processo à Memória Secundária
        if self.secundaria.adiciona_processo(processo):
            processo.atualiza_estado("Pronto/Suspenso")
            # Adiciona o processo à fila de processos prontos/suspenso
            self.fila_prontos_suspenso.append(processo)

        # Verifica se há espaço disponível na memória principal antes de adicionar o processo

        if self.principal.adiciona_processo(processo, self.secundaria):
            processo.atualiza_estado("Pronto")
            print(f"Processo {numero_processo} criado com sucesso.")
            self.mostra_situacao_memoria()

            # Exibe o estado da memória principal após a tentativa de criação do processo
#            self.mostra_situacao_memoria()

        # Exibe o estado da memória principal após a tentativa de adição do processo

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
            processo.atualiza_estado("Finalizado")
            print(f"Processo {numero_processo} terminado.")
        else:
            print(f"Processo {numero_processo} não encontrado.")

    def executa_instrucao(self, numero_processo, endereco_logico):
        processo = self.principal.encontra_processo(numero_processo, set())
     #   if processo == None:
        processo.atualiza_estado("Executando")

        if processo:
            processo.imagem.PC = endereco_logico
            processo.imagem.IR = endereco_logico
            quadro_dentro = 0
            
            print(f"Executando instrução do endereço lógico {endereco_logico} para o processo {numero_processo}.")

            if self.principal.tabelas_paginas[processo.imagem.id_processo] == []:
                entrada = Entrada_TP(math.floor(endereco_logico/255), 256)
                entrada.p = 1
                self.principal.tabelas_paginas[processo.imagem.id_processo].append(entrada)
                print(f"Página {math.floor(endereco_logico/255)} entrou na TP de {numero_processo}")
            else:

                for entrada in self.principal.tabelas_paginas[processo.imagem.id_processo]:
                    if math.floor(endereco_logico/255) == entrada.numquadro:
                        quadro_dentro = 1

                if quadro_dentro == 0 and len(self.principal.tabelas_paginas[processo.imagem.id_processo]) < self.principal.tamanho_tabela_paginas:
                    entrada = Entrada_TP(math.floor(endereco_logico/255), 256)
                    entrada.p = 1
                    self.principal.tabelas_paginas[processo.imagem.id_processo].append(entrada)
                    print(f"Página {math.floor(endereco_logico/255)} entrou na TP de {numero_processo}")
                elif quadro_dentro == 1:
                    print(f"Página {math.floor(endereco_logico/255)} já está dentro da TP")
                else:
                    print("Tabela de Páginas Cheia")

     #       gerenciador.principal.mostra_tabelas_paginas()
        else:
            print(f"Processo {numero_processo} não encontrado.")

    def executa_io(self, numero_processo, dispositivo):
        processo = self.principal.encontra_processo(numero_processo, set())
        processo.atualiza_estado("Bloqueado")
        print(f"Processo {numero_processo} executando operação de I/O no dispositivo {dispositivo}.")
        print(f"Processo {numero_processo} bloqueado por operação de I/O no dispositivo {dispositivo}.")

    def realiza_leitura(self, numero_processo, endereco_logico):
        processo = self.principal.encontra_processo(numero_processo, set())
        if processo:
            processo.imagem.PC = endereco_logico
            processo.imagem.IR = endereco_logico
       #     self.realiza_leitura(numero_processo, endereco_logico)
            processo.atualiza_estado("Executando")
            print(f"Realizando leitura para o processo {numero_processo} no endereço lógico {endereco_logico}.")
            quadro_dentro = 0

            if self.principal.tabelas_paginas[processo.imagem.id_processo] == []:
                entrada = Entrada_TP(math.floor(endereco_logico/255), 256)
                entrada.p = 1
                self.principal.tabelas_paginas[processo.imagem.id_processo].append(entrada)
                print(f"Página {math.floor(endereco_logico/255)} entrou na TP de {numero_processo}")
            else:
                
                for entrada in self.principal.tabelas_paginas[processo.imagem.id_processo]:
                    if math.floor(endereco_logico/255) == entrada.numquadro:
                        quadro_dentro = 1

                if quadro_dentro == 0 and len(self.principal.tabelas_paginas[processo.imagem.id_processo]) < self.principal.tamanho_tabela_paginas:
                    entrada = Entrada_TP(math.floor(endereco_logico/255), 256)
                    entrada.p = 1
                    self.principal.tabelas_paginas[processo.imagem.id_processo].append(entrada)
                    print(f"Página {math.floor(endereco_logico/255)} entrou na TP de {numero_processo}")
                elif quadro_dentro == 1:
                    print(f"Página {math.floor(endereco_logico/255)} já está dentro da TP")
                else:
                    print("Tabela de Páginas Cheia")
        else:
            print(f"Processo {numero_processo} não encontrado.")

    def realiza_escrita(self, numero_processo, endereco_logico, valor):
        processo = self.principal.encontra_processo(numero_processo, set())

        if processo:
            processo.imagem.PC = endereco_logico
            processo.imagem.IR = endereco_logico
            processo.atualiza_estado("Executando")
            print(f"Realizando escrita para o processo {numero_processo} no endereço lógico {endereco_logico} com valor {valor}.")
            quadro_dentro = 0

            if self.principal.tabelas_paginas[processo.imagem.id_processo] == []:
                entrada = Entrada_TP(math.floor(endereco_logico/255), 256)
                entrada.p = 1
                entrada.m = 1
                self.principal.tabelas_paginas[processo.imagem.id_processo].append(entrada)
                print(f"Página {math.floor(endereco_logico/255)} entrou na TP de {numero_processo}")
            else:
                for entrada in self.principal.tabelas_paginas[processo.imagem.id_processo]:
                    if math.floor(endereco_logico/255) == entrada.numquadro:
                        quadro_dentro = 1

                if quadro_dentro == 0 and len(self.principal.tabelas_paginas[processo.imagem.id_processo]) < self.principal.tamanho_tabela_paginas:
                    entrada = Entrada_TP(math.floor(endereco_logico/255), 256)
                    entrada.p = 1
                    entrada.m = 1
                    self.principal.tabelas_paginas[processo.imagem.id_processo].append(entrada)
                    print(f"Página {math.floor(endereco_logico/255)} entrou na TP de {numero_processo}")
                elif quadro_dentro == 1:
                    print(f"Página {math.floor(endereco_logico/255)} já está dentro da TP")
                else:
                    print("Tabela de Páginas Cheia")

        else:
            print(f"Processo {numero_processo} não encontrado.")



# Exemplo de uso
# MP de 16 KB, MS de 1 MB, tamanho da página 256 e 12 do endereço
gerenciador = GerenciadorMemoria(tamanho_mp= 16384 , tamanho_ms= 1048576 , tamanho_pagina=256)

gerenciador.mostra_situacao_memoria()

gerenciador.executa_comandos('entrada.txt')

gerenciador.principal.mostra_tabelas_paginas()

# Mostra o estado da memória principal ao final da simulação
#gerenciador.principal.mostra_memoria_principal()

# Mostra o estado da memória secundária ao final da simulação
gerenciador.secundaria.mostra_memoria_secundaria()