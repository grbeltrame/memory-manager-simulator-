from registro_entrada import Registro 
class Imagem:


# Construtor da classe imagem, recebe os atributos da imagem de cada processo
  def __init__(self,id_processo, PC, IR, estado,nome = None,tamanho = None):
    self.id_processo = id_processo
    self.PC = PC
    self.IR = IR
    self.estado = estado
    self.nome =''
    self.tamanho =''
    self.executavel = []

# Adiciona linhas de codigo do tipo Registro Entrada no arquivo de codigo executavel
# Usar essa função na hora de ler o arquivo de entrada, o parametro registro é uma linha do arquivo de entrada
  def adiciona_registro(self, registro):
    self.executavel.append(registro)
    self.nome = registro.numero_processo
    self.tamanho = registro.tamanho

# Função para atualizar a imagem
# Quando o processo muda de estado, a imagem pode ser atualizada. Usar quando necessario, isto é, quando vai da MP para MS e vice versa
# ou seja, quando vai e sai dos estados suspensos
  def atualiza_imagem(self, new_PC, new_IR, new_Estado):
    self.PC = new_PC
    self.IR = new_IR
    self.estado = new_Estado

# Função para atualizar apenas o estado do processo, quando ele esta indo de PRONTO para EXECUTANDO, de EXECUTANDO para BLOQUEADO, 
# de BLOQUEADO para PRONTO e quando ele é FINALIZADO
  def atualiza_estado(self, new_Estado):
    self.estado = new_Estado

#  Função para mostrar o estado da imagem
  def mostra_imagem(self):
    print('\nSITUAÇÃO DA IMAGEM:')
    print('----------------------')
    print(f'Id do processo: {self.id_processo}')
    print(f'Numero do processo: {self.nome}')
    print(f'Program counter: {self.PC}')
    print(f'Instruction registrer: {self.IR}')
    print(f'Estado do processo: {self.estado}')