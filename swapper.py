class Swapper:
    def move_processo(self, processo, principal, secundaria):
        # Variável "removido" indica qual será o processo que sairá da MP
        removido = principal.memoria[0]
        
        # Loop para percorrer a memória principal
        for i in range(len(principal.memoria)):
            # Aqui, encontramos qual processo está a mais tempo na MP
            if principal.memoria[i].imagem.id_processo < removido.imagem.id_processo:
                removido = principal.memoria[i].imagem
        
        # Removemos o processo antigo da MP
        principal.memoria.remove(removido)
        secundaria.adiciona_processo(removido, secundaria)  # Corrigido para adicionar o processo removido à memória secundária
        # Tentamos adicionar o processo novo na MP
        principal.adiciona_processo(processo)
