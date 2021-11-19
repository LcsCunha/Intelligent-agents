from robo import robo

class roboSeletor (robo):
  """
  Classe responsável por instanciar métodos específicos 
  efetuados por um robô do tipo coletor
  """
  direcao = None
  localAtual = {
    'x': 19,
    'y': 0
  }

  localLixeiraFinal = {
    'I': (19, 0,),
    'R': (19, 19,)
  }
  
  def __init__(self, nome):
    robo.__init__(self, nome)