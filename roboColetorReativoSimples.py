from roboColetor import roboColetor
import random

class roboColetorReativoSimples (roboColetor):
  def __init__(self, nome):
    roboColetor.__init__(self, nome)

  def checalixo(self, ambiente):
    x = self.localAtual['x']
    y = self.localAtual['y']
    espaco = ambiente[y][x]

    lim_right = self.localAtual['x'] == 19
    lim_left = self.localAtual['x'] == 0
    lim_up = self.localAtual['y'] == 0
    lim_down = self.localAtual['y'] == 19
    #print("espaco = ", espaco)
    #print("dir = ", right, "esq = ", left, "up = ", up, "down = ", down)
    if self.lixo_carregado == None:
      if espaco == 1 or espaco == 2: #Se o espaço estiver sujo
        self.lixo_carregado = espaco
        ambiente[y][x] = " "
        return ambiente

    try:
      right = ambiente[y][x + 1]
    except:
      right = None

    try:
      left = ambiente[y][x - 1]
    except:
      left = None
    
    try:
      up = ambiente[y - 1][x]
    except:
      up = None
    
    try:
      down = ambiente[y + 1][x]
    except:
      down = None
    #Caso não haja lixo nas 4 posições ao redor do robô
    while (True):
      mov = random.randrange(1, 5)
      #print("mov = ", mov)
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

  def moveRoboAteLixeira(self, ambiente):
    #if self.soltarLixos(ambiente): #Caso o robo esteja na posição da lixeira
      #return ambiente.ambiente
    
    lim_right = self.localAtual['x'] == 19
    lim_left = self.localAtual['x'] == 0
    lim_up = self.localAtual['y'] == 0
    lim_down = self.localAtual['y'] == 19
    
    x = self.localAtual['x']
    y = self.localAtual['y']

    yLixo1 = self.localLixeira['X'][0]
    xLixo1 = self.localLixeira['X'][1]
    xLixo2 = self.localLixeira['Y'][0]
    yLixo2 = self.localLixeira['Y'][1]

    if x == xLixo1 and y == yLixo1:
      ambiente.X.append(self.lixo_carregado)
      self.lixo_carregado = None
      return ambiente
    elif x == xLixo2 and y == yLixo2:
      ambiente.Y.append(self.lixo_carregado)
      self.lixo_carregado = None
      return ambiente

    #Caso não haja lixo nas 4 posições ao redor do robô
    while (True):
      mov = random.randrange(1, 5)
      #print("mov = ", mov)
      if mov == 1 and not lim_right:
        self.localAtual['x'] += 1
        return ambiente
      if mov == 2 and not lim_left:
        self.localAtual['x'] -= 1
        return ambiente
      if mov == 3 and not lim_down:
        self.localAtual['y'] += 1
        return ambiente
      if mov == 4 and not lim_up:
        self.localAtual['y'] -= 1
        return ambiente

      return ambiente.ambiente

    #if x == 
    #if self.localAtual['x']