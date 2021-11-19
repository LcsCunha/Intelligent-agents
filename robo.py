class robo:
  """
  Classe responsável por instanciar o agente robô que irá interagir com o ambiente.
  Seus métodos são ações que o mesmo efetua no ambiente.
  """
  nome = ""
  #Percepções

  localLixeira = {
    'X': (11, 0,),
    'Y': (11, 19,)
  }
  #localLixeiras = None #Ajeitar isso depois
  #historicoPercepcoes = []
  #ambiente = []
  lixo_carregado = None

  def __init__ (self, nome):
    self.nome = nome

  def checalixo(self, espaco):
    raise NotImplementedError("Deve ser implementada na classe robo coletor")
  
  #Ações
  
  # def soltaLixo ():

  # def noOp ():



  #Alterações: ambiente

  #Percepções