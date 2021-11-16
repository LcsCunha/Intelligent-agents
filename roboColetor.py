from robo import robo
import random

class roboColetor (robo):
  """
  Classe responsável por instanciar métodos específicos 
  efetuados por um robô do tipo coletor
  """
  
  def __init__(self, nome):
    robo.__init__(self, nome)

  def checalixo(self, espaco):
    raise NotImplementedError("Deve ser implementada na classe filha")

class roboColetorReativoSimples (roboColetor):
  def __init__(self, nome):
    roboColetor.__init__(self, nome)

  def checalixo(self, ambiente):
    x = self.localAtual['x']
    y = self.localAtual['y']
    espaco = ambiente[x][y]
    print("espaco = ", espaco)

    right = ambiente[x + 1][y]
    left = ambiente[x - 1][y]
    up = ambiente[x][y - 1]
    down = ambiente[x][y + 1]
    print("dir = ", right, "esq = ", left, "up = ", up, "down = ", down)
    
    if espaco != " ": #Se o espaço estiver sujo
      self.lixo_carregado = espaco
      ambiente[x][y] = " "
      return ambiente
    elif right == 1 or right == 2:
      self.localAtual['x'] += 1
      return ambiente
    elif left == 1 or left == 2:
      self.localAtual['x'] -= 1
      return ambiente
    elif down == 1 or down == 2:
      self.localAtual['y'] += 1
      return ambiente
    elif up == 1 or up == 2:
      self.localAtual['y'] -= 1
      return ambiente

    #Caso não haja lixo nas 4 posições ao redor do robô
    lim_right = self.localAtual['x'] == 19
    lim_left = self.localAtual['x'] == 0
    lim_up = self.localAtual['y'] == 0
    lim_down = self.localAtual['y'] == 19

    while (True):
      mov = random.randrange(1, 5)

      print("mov = ", mov)
      if mov == 1 and right == " " and not lim_right:
        self.localAtual['x'] += 1
        return ambiente
      if mov == 2 and left == " " and not lim_left:
        self.localAtual['x'] -= 1
        return ambiente
      if mov == 3 and down == " " and not lim_down:
        self.localAtual['y'] += 1
        return ambiente
      if mov == 4 and up == " " and not lim_up:
        self.localAtual['y'] -= 1
        return ambiente

class baseadaEmModelos (roboColetor):
  def __init__(self, nome):
    roboColetor.__init__(self, nome)

  def checalixo(self, ambiente):
    x = self.localAtual['x']
    y = self.localAtual['y']
    espaco = ambiente[x][y]
    print("espaco = ", espaco)

    right = ambiente[x + 1][y]
    left = ambiente[x - 1][y]
    up = ambiente[x][y - 1]
    down = ambiente[x][y + 1]
    print("dir = ", right, "esq = ", left, "up = ", up, "down = ", down)
    
    if espaco != " ": #Se o espaço estiver sujo
      self.lixo_carregado = espaco
      ambiente[x][y] = " "
      return ambiente
    elif right == 1 or right == 2:
      self.localAtual['x'] += 1
      return ambiente
    elif left == 1 or left == 2:
      self.localAtual['x'] -= 1
      return ambiente
    elif down == 1 or down == 2:
      self.localAtual['y'] += 1
      return ambiente
    elif up == 1 or up == 2:
      self.localAtual['y'] -= 1
      return ambiente
      
    #Caso não haja lixo nas 4 posições ao redor do robô
    lim_right = self.localAtual['x'] == 19
    lim_left = self.localAtual['x'] == 0
    lim_up = self.localAtual['y'] == 0
    lim_down = self.localAtual['y'] == 19

    while (True):
      mov = random.randrange(1, 5)

      print("mov = ", mov)
      if mov == 1 and right == " " and not lim_right:
        self.localAtual['x'] += 1
        return ambiente
      if mov == 2 and left == " " and not lim_left:
        self.localAtual['x'] -= 1
        return ambiente
      if mov == 3 and down == " " and not lim_down:
        self.localAtual['y'] += 1
        return ambiente
      if mov == 4 and up == " " and not lim_up:
        self.localAtual['y'] -= 1
        return ambiente