from robo import robo

class roboColetor (robo):
  """
  Classe responsável por instanciar métodos específicos 
  efetuados por um robô do tipo coletor
  """
  localAtual = {
    'x': 0,
    'y': 0
  }
  
  def __init__(self, nome):
    robo.__init__(self, nome)

  def checalixo(self, espaco):
    raise NotImplementedError("Deve ser implementada na classe filha")