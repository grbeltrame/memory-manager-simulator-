from processo import Processo
from imagem import Imagem
from registro_entrada import Registro

processos = {}
id = 0

# Não sei o que ta rolando, ele ta lendo o arquivo P7 duas vezes mas não ta lendo o P1
# Mas ta imprimindo os dados certos pelo menos
with open('entrada.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split()
        
        if len(partes) >= 3:
            nome = partes[0]

            if nome not in processos:
                img = Imagem(id, 0, 0, 'NOVO')
                processo = Processo(img)
                processos[nome] = processo.imagem.nome
                id += 1
            else:
                continue

            reg = Registro(partes[0], partes[1], partes[2])
            processo.imagem.adiciona_registro(reg)

for imagem in processos.items():
    print(processo.mostra_processo())
    
