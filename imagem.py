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
    # Adicione apenas os valores necessários
      if registro.tamanho is not None:
            self.tamanho = registro.tamanho

      if registro.dispositivo is not None:
          self.dispositivo = registro.dispositivo

      if registro.endereco is not None:
          self.endereco = registro.endereco

      if registro.endereco_r is not None:
          self.endereco_r = registro.endereco_r

      if registro.endereco_w is not None:
          self.endereco_w = registro.endereco_w

      if registro.valor is not None:
          self.valor = registro.valor

      self.nome = registro.numero_processo

      # Adicione a instrução diretamente, não a instância de Registro
      self.executavel.append(registro)


      


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

  def mostra_executavel(self):
    print("Executavel:")
    for instrucao in self.executavel:
        if hasattr(instrucao, 'tamanho'):
            print(f"{instrucao.numero_processo} {instrucao.comando} {instrucao.tamanho}")
        elif hasattr(instrucao, 'dispositivo'):
            print(f"{instrucao.numero_processo} {instrucao.comando} {instrucao.dispositivo}")
        elif hasattr(instrucao, 'endereco'):
            print(f"{instrucao.numero_processo} {instrucao.comando} {instrucao.endereco}")
        elif hasattr(instrucao, 'endereco_r'):
            print(f"{instrucao.numero_processo} {instrucao.comando} {instrucao.endereco_r}")
        elif hasattr(instrucao, 'endereco_w'):
            print(f"{instrucao.numero_processo} {instrucao.comando} {instrucao.endereco_w}")
        elif hasattr(instrucao, 'valor'):
            print(f"{instrucao.numero_processo} {instrucao.comando} {instrucao.valor}")
        else:
            # Caso genérico, imprimir apenas os atributos conhecidos
            print(f"{instrucao.numero_processo} {instrucao.comando}")

     

#  Função para mostrar o estado da imagem
# Função para mostrar o estado da imagem
def mostra_imagem(self):
    executavel_str = ", ".join(map(str, self.executavel)) if self.executavel else "Nenhuma instrução"
    return f'\nSITUAÇÃO DA IMAGEM:\n----------------------\nId do processo: {self.id_processo}\nNumero do processo: {self.nome}\nProgram counter: {self.PC}\nInstruction registrer: {self.IR}\nEstado do processo: {self.estado}\nExecutavel: {executavel_str}\n'
