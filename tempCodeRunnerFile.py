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
                processos[nome] = processo
                id += 1
            else:
                processo = processos[nome]

            reg = Registro(partes[0], partes[1], partes[2])
            processo.imagem.adiciona_registro(reg)


# main.py
for nome, processo in processos.items():
    print(f'\nSITUAÇÃO DO PROCESSO {nome}:\n--------------------------\nTamanho do processo: {processo.imagem.tamanho}\nId do processo: {processo.imagem.id_processo}\nNumero do processo: {processo.imagem.nome}\nProgram counter: {processo.imagem.PC}\nInstruction registrer: {processo.imagem.IR}\nEstado do processo: {processo.imagem.estado}\nQuantidade de Páginas na TP: {len(processo.paginas.entradas)} ')



