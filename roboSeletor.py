import robo

class roboSeletor (robo):
  """
  Classe responsável por instanciar métodos específicos 
  efetuados por um robô do tipo coletor
  """
  def checalixo(self, espaco):
    if espaco == 0:
      return
    elif espaco == 1:
      self.carregando_lixo = 'R'
    elif espaco == 2:
      self.carregando_lixo = 'N'