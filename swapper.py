class Swapper:
    def move_processo(self, processo, principal, secundaria):
        # Variável "removido" indica qual será o processo que sairá da MP
        removido = principal.memoria[0]

        # Encontra o processo mais antigo na MP
        for i in range(len(principal.memoria)):
            if principal.memoria[i] and principal.memoria[i].imagem.id_processo < removido.imagem.id_processo:
                removido = principal.memoria[i].imagem

        # Removemos o processo antigo da MP, se existir
        if removido:
            principal.remover_processo(removido)
            secundaria.adiciona_processo(removido)  # Corrigido para adicionar o processo removido à memória secundária

        # Tentamos adicionar o processo novo na MP
        principal.adiciona_processo(processo)
