import random
from roboColetor import roboColetorReativoSimples

class classeAmbiente:
  """
  Classe responsável por instanciar o ambiente em que atuará os agentes robô coletor e robô seletor
  """
  ambiente = None
  R1 = roboColetorReativoSimples("R")

  def geraAmbiente(self):
    """
    Método responsável por gerar o ambiente inserindo os robôs  e lixeiras em suas respectivas posições e
    lixo de forma randômica.
    Todas as posições serão aleatoriamente contempladas com um lixo orgânico ou reciclável ou nenhum deles, e
    após isso as posições padrões do robô e dos lixos será setada.
    0 - Posição livre
    1 - Lixo reciclável
    2 - Lixo orgânico

    O robô R1 inicia na posição 1x1, o robô R2 inicia na posição 1x20. As lixeiras estão em 12x1 e 12x20, o incinerador está em 20x1 e a recicladora em
    20x20.
    """
    
    ambiente = []
    qtdLixos = 0

    for i in range(20):
      linha = []
      for j in range(20):
        linha.append(0)
      ambiente.append(linha)

    ambiente[0][0] = "R1"
    ambiente[0][19] = "Q"
    ambiente[11][0] = "X"
    ambiente[11][19] = "Y"
    ambiente[19][0] = "I"
    ambiente[19][19] = "R"

    for i in range(20):
      for j in range(20):
        if ambiente[i][j] != 0:
          continue
        seed = random.randrange(0, 10)
        if seed > 3:
          ambiente[i][j] = " "
          continue
        lixo = random.randrange(0, 3)
        if (lixo > 0 and qtdLixos < 2):
          qtdLixos += 1
          ambiente[i][j] = lixo
        else:
          ambiente[i][j] = " "
      qtdLixos = 0

    ambiente[0][0] = " "
    self.ambiente = ambiente

  def __init__(self):
    self.geraAmbiente()

  def atualizaAmbiente (self):
    print("x = ", self.R1.localAtual['x'])
    print("y = ", self.R1.localAtual['y'])
    #xR1 = self.R1.localAtual['x']
    #yR1 = self.R1.localAtual['y']
    #self.ambiente[xR1][yR1] = "R1"
    self.ambiente = self.R1.checalixo(self.ambiente)

    #self.ambiente = self.R2.levaLixo(self.ambiente)
  
  def getAmbiente (self):
    """
    Essa função provavelmente vai se transformar em uma diferente na versão final.
    Por enquanto permanece para propósitos de debug
    Serve pra printar na tela o ambiente.
    """

    while(True):
      lixo = 0

      if self.ambiente != None:
        xR1 = self.R1.localAtual['x']
        yR1 = self.R1.localAtual['y']
        
        ambiente = self.ambiente
        for i in range(len(ambiente)):
          for j in range(len(ambiente[i])):
            if j == xR1 and i == yR1:
              print(self.R1.nome, end=" ")
              continue
            if ambiente[i][j] == 1 or ambiente[i][j] == 2:
              lixo += 1
            print(ambiente[i][j], end=" ")
          print(" ")

      self.atualizaAmbiente()
      print("Lixo ", lixo)
      print("Carregamento = ", self.R1.lixo_carregado)
      buffer = input("Pressione qualquer tecla para continuar")
      print("\n\n\n\n\n\n\n\n\n\n")