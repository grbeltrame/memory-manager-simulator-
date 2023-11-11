from imagem import Imagem
from memoria_principal import Principal
from memoria_secundaria import Secundaria
from processo import Processo
from tabela_paginas import TabelaPagina

class Swapper:
    #Em move processo, o swapper recebe o processo que está entrando na MP e envia o processo que está a mais tempo (LRU), para a MS.
    def move_processo(processo, principal, secundaria):
        #Variável "removido" indica qual será o processo que sairá da MP
        removido = principal.memoria[0]
        #Loop para percorrer a memória principal
        for i in range(len(principal.memoria)):
            #aqui, encontramos qual processo está a mais tempo na MP
            if principal.memoria[i].imagem.id_processo < removido.imagem.id_processo:
                removido = principal.memoria[i].imagem
        #removemos o processo antigo da MP
        secundaria.adiciona_processo(secundaria,removido)
        #tentamos adicionar o processo novo na MP
        principal.adiciona_processo(principal,processo)