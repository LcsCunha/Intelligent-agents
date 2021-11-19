from roboColetor import roboColetor
import random

class roboColetorUtilidade (roboColetor):
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
    #print("dir = ", right, "esq = ", left, "up = ", up, "down = ", down)
    if espaco == 1 or espaco == 2: #Se o espaço estiver sujo
      self.lixo_carregado = espaco
      ambiente[y][x] = " "
      return ambiente
    elif right == 2 and not lim_right:
      self.localAtual['x'] += 1
      return ambiente
    elif left == 2 and not lim_left:
      self.localAtual['x'] -= 1
      return ambiente
    elif down == 2 and not lim_down:
      self.localAtual['y'] += 1
      return ambiente
    elif up == 2 and not lim_up:
      self.localAtual['y'] -= 1
      return ambiente
    elif right == 1 and not lim_right:
      self.localAtual['x'] += 1
      return ambiente
    elif left == 1 and not lim_left:
      self.localAtual['x'] -= 1
      return ambiente
    elif down == 1 and not lim_down:
      self.localAtual['y'] += 1
      return ambiente
    elif up == 1 and not lim_up:
      self.localAtual['y'] -= 1
      return ambiente

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

  def soltarLixos(self, ambiente):
    
    y = self.localAtual['y']
    x = self.localAtual['x']

    yLixo1 = self.localLixeira['X'][0]
    xLixo1 = self.localLixeira['X'][1]

    xLixo2 = self.localLixeira['Y'][0]
    yLixo2 = self.localLixeira['Y'][1]

    if x == xLixo1 and y == yLixo1:
      ambiente.X.append(self.lixo_carregado)
      self.lixo_carregado = None
      return True
    elif x == xLixo2 and y == yLixo2:
      ambiente.Y.append(self.lixo_carregado)
      self.lixo_carregado = None
      return True
    
    return False

  def moveRoboAteLixeira(self, ambiente):
    if self.soltarLixos(ambiente): #Caso o robo esteja na posição da lixeira
      return ambiente.ambiente

    if self.localAtual['x'] == 0:
      self.localAtual['x'] +=1
      return ambiente.ambiente
    elif self.localAtual['x'] == 19:
      self.localAtual['x'] -= 1
      return ambiente.ambiente

    if self.localAtual['y'] < self.localLixeira['X'][0]:
      self.localAtual['y'] += 1
      return ambiente.ambiente
    elif self.localAtual['y'] > self.localLixeira['X'][0]:
      self.localAtual['y'] -= 1
      return ambiente.ambiente

    distancia1 = abs(self.localAtual['x'] - self.localLixeira['X'][1])
    distancia2 = abs(self.localAtual['x'] - self.localLixeira['Y'][1])

    if distancia1 <= distancia2:
      lixo_mais_proximo = self.localLixeira['X'][1]
    if distancia1 > distancia2:
      lixo_mais_proximo = self.localLixeira['Y'][1]

    if self.localAtual['x'] < lixo_mais_proximo:
      self.localAtual['x'] += 1
      return ambiente.ambiente
    elif self.localAtual['x'] > lixo_mais_proximo:
      self.localAtual['x'] -= 1
      return ambiente.ambiente

    return ambiente.ambiente

    #if x == 
    #if self.localAtual['x']