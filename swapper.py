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
        principal.remover_processo(processo)
        print(f"Processo {processo.imagem.id_processo} foi Suspenso (Swapper)")