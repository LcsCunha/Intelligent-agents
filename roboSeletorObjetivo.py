from roboSeletor import roboSeletor

class roboSeletorObjetivo (roboSeletor):
  def __init__(self, nome):
    roboSeletor.__init__(self, nome)

  def monitoraLixos(self, ambiente):
    #print("direcao:", self.direcao)
    if self.direcao == None:
      ambiente.ambiente = self.moveRoboAteLixeira(ambiente)
    elif self.pegarLixos(ambiente):
      return ambiente.ambiente
    elif self.direcao == 'Left':
      self.localAtual['x'] -= 1
    elif self.direcao == 'Right':
      self.localAtual['x'] += 1
    
    return ambiente.ambiente

  def pegarLixos(self, ambiente):
    
    if self.lixo_carregado != None:
      return False

    x = self.localAtual['y']
    y = self.localAtual['x']
    
    xLixo1 = self.localLixeira['X'][0]
    yLixo1 = self.localLixeira['X'][1]

    #print("xLixo = ", xLixo1)
    #print("yLixo = ", yLixo1)
    #print("xRobo = ", x)
    #print("yRobo = ", y)
    #print("Lixo do robo = ", self.lixo_carregado)

    xLixo2 = self.localLixeira['Y'][0]
    yLixo2 = self.localLixeira['Y'][1]

    if x == xLixo1 and y == yLixo1:
      if len(ambiente.X) > 0:
        #print("entrou")
        self.lixo_carregado = ambiente.X.pop()
        self.direcao = self.definirDirecao()
        return True
      else:
        self.direcao = 'Right'
        return False
      return True
    elif x == xLixo2 and y == yLixo2:
      if len(ambiente.Y) > 0:
        self.lixo_carregado = ambiente.Y.pop()
        self.direcao = self.definirDirecao()
        return True
      else:
        self.direcao = 'Left'
        return False
    
    return False

  def definirDirecao(self):
    if self.lixo_carregado == 1:
      self.direcao = 'I'
    elif self.lixo_carregado == 2:
      self.direcao = 'R'

  def moveRoboAteLixeira(self, ambiente):
    if self.pegarLixos(ambiente): #Caso o robo esteja na posição da lixeira
      return ambiente.ambiente

    if self.localAtual['x'] == 0:
      self.localAtual['x'] +=1
      return ambiente.ambiente
    elif self.localAtual['x'] == 19:
      self.localAtual['x'] -= 1
      #print("ENTROOOOU")
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