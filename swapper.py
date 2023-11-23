class Swapper:
    @staticmethod
    def move_processo(principal):
        # Variável processo indica qual sairá da MP
        processo = None
        maiorTimer = 0
        for i in principal.memoria:
            if i != None:
                if maiorTimer <= i.timer:
                    maiorTimer = i.timer
                    processo = i
        processo.estado = "Suspenso"
        processo.imagem.estado = "Suspenso"
        principal.mostra_tabelas_paginas()
        principal.remover_processo(processo)
        print(f"\nProcesso {processo.imagem.id_processo} foi Suspenso (Swapper [LRU]) por falta de espaço\n")