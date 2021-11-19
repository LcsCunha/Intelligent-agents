from roboSeletor import roboSeletor
import random

class roboSeletorReativoSimples (roboSeletor):
  def __init__(self, nome):
    roboSeletor.__init__(self, nome)

  def monitoraLixos(self, ambiente):

    x = self.localAtual['y']
    y = self.localAtual['x']
    
    xLixo1 = self.localLixeira['X'][0]
    yLixo1 = self.localLixeira['X'][1]

    xLixo2 = self.localLixeira['Y'][0]
    yLixo2 = self.localLixeira['Y'][1]

    if x == xLixo1 and y == yLixo1:
      if len(ambiente.X) > 0:
        self.lixo_carregado = ambiente.X.pop()
        return ambiente
    elif x == xLixo2 and y == yLixo2:
      if len(ambiente.Y) > 0:
        self.lixo_carregado = ambiente.Y.pop()
        return ambiente
    
    lim_right = self.localAtual['x'] == 19
    lim_left = self.localAtual['x'] == 0
    lim_up = self.localAtual['y'] == 0
    lim_down = self.localAtual['y'] == 19

    yLixo1 = self.localLixeiraFinal['I'][0]
    xLixo1 = self.localLixeiraFinal['I'][1]

    xLixo2 = self.localLixeiraFinal['R'][0]
    yLixo2 = self.localLixeiraFinal['R'][1]

    if x == xLixo1 and y == yLixo1:
      ambiente.I.append(self.lixo_carregado)
      self.lixo_carregado = None
      self.direcao = None
      return ambiente.ambiente
    elif x == xLixo2 and y == yLixo2:
      ambiente.R.append(self.lixo_carregado)
      self.lixo_carregado = None
      self.direcao = None
      return ambiente.ambiente

    while (True):
      mov = random.randrange(1, 5)
      #print("mov = ", mov)
      if mov == 1 and not lim_right:
        self.localAtual['x'] += 1
        return ambiente
      if mov == 2 and lim_left:
        self.localAtual['x'] -= 1
        return ambiente
      if mov == 3 and lim_down:
        self.localAtual['y'] += 1
        return ambiente
      if mov == 4 and lim_up:
        self.localAtual['y'] -= 1
        return ambiente
    
    return ambiente.ambiente

  def despejarLixo (self, ambiente):
    y = self.localAtual['y']
    x = self.localAtual['x']

    yLixo1 = self.localLixeiraFinal['I'][0]
    xLixo1 = self.localLixeiraFinal['I'][1]

    xLixo2 = self.localLixeiraFinal['R'][0]
    yLixo2 = self.localLixeiraFinal['R'][1]

    if x == xLixo1 and y == yLixo1:
      ambiente.I.append(self.lixo_carregado)
      self.lixo_carregado = None
      self.direcao = None
      return True
    elif x == xLixo2 and y == yLixo2:
      ambiente.R.append(self.lixo_carregado)
      self.lixo_carregado = None
      self.direcao = None
      return True
    
    return False

  def moveRoboAteFim (self, ambiente):
    if self.despejarLixo (ambiente):
      return ambiente.ambiente

    if self.localAtual['x'] == 0:
      self.localAtual['x'] +=1
      return ambiente.ambiente
    elif self.localAtual['x'] == 19:
      self.localAtual['x'] -= 1
      return ambiente.ambiente

    if self.localAtual['y'] < self.localLixeiraFinal['I'][0]:
      self.localAtual['y'] += 1
      return ambiente.ambiente
    else:
      if self.lixo_carregado == 1: 
        self.localAtual['x'] -= 1 #Vai em direção ao incinerador
      elif self.lixo_carregado == 2:
        self.localAtual['x'] += 1 #Vai em direção ao reciclador

    return ambiente.ambiente
    #if x == 
    #if self.localAtual['x']