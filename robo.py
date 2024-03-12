class Robo:
  """
  Classe responsável por instanciar o agente robô 
  que irá interagir com o ambiente.
  Seus métodos são ações que o mesmo efetua no ambiente.
  """

  def __init__ (self, nome):
    self.nome = nome
    self.pos_xy = [0, 0],
      

  def checalixo(self, espaco):
    raise NotImplementedError("Deve ser implementada na classe robo coletor")

  def get_posicao_robo(self):
    return self.pos_xy
  
  #TODO verificar usabilidade de atualizar a posicao dessa forma
  # def atualiza_pos_robo(self, tipo):
  #   if tipo == 'x++':
  #     self.pos_xy[0] += 1
  #   elif tipo == 'x--':
  #     self.pos_xy[0] -= 1
  #   elif tipo == 'y++':
  #     self.pos_xy[1] += 1

  def incrementa_pos_x(self):
    self.pos_xy[0] += 1
  
  def incrementa_pos_y(self):
    self.pos_xy[1] += 1
  
  def decrementa_pos_x(self):
    self.pos_xy[0] -= 1

  def decrementa_pos_y(self):
    self.pos_xy[0] -= 1

  #Ações

  # def soltaLixo ():

  # def noOp ():



  #Alterações: ambiente

  #Percepções