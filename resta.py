import os
class Resta(object):
  base = 7
  campos = 32
  matriz = 0

  def __init__(self):
    self.setup()

  #Inicializa matriz:
  def setup(self):
    self.matriz = [[ (-1 if ((i<2 or i>4) and (j<2 or j>4))
                        else 1 if not ( i == 3 and j ==3)
                        else 0) for j in range(self.base)]
                        for i in range(self.base)]
    self.start()

  def start(self):
    while True:
      self.limpaTela()
      self.printaMatriz()

      if(self.ganhou()):
        print("***GANHOU***")
        return
      elif(self.temJogadas()):
        print("Nao foi dessa vez --- \n Ainda restam {}".format(self.campos))
        return

      self.temJogadas()
      init, end = 0,0
      options = []

      while True:
        init = input ("Mover de (l, c): ")
        options = self.opcaoMovimento(self.quebraEntrada(init))
        if(len(options) > 0):
          break
        else:
          print("Posicao Invalida")

      while True:
        end = input ("Mover para (l, c): ")
        if(init != end and (self.quebraEntrada(end) in options)):
          break
        else:
          print("Posicao Invalida")
          
  def printaMatriz(self):
    result = [[x if x != 0 else ' ' for x in range(self.base + 1)]]
    custom = [[' ' if x == -1 else '-' if x == 0 else '0' for x in i] for i in self.matriz]

    i = 0
    while i < len(self.matriz):
      row = custom[i]
      result.append([chr(97+i)] + row)
      i +=1
    self.show(result)

  def show(self, matrizEnd):
    print("\n".join(' '.join([str(x) for x in i]) for i in matrizEnd))

  def temJogadas(self):
    for i in range(len(self.matriz)):
      for j, val in enumerate(self.matriz[i]):
        if val == 1 and self.opcaoMovimento([i, j]):
          return False
    
    return True
  
  def ganhou(self):
    return self.campos == 1

  def mover(self, init, end):
    initPos = self.quebraEntrada(init)
    endPos = self.quebraEntrada(end)

    self.matriz[initPos[0]][initPos[1]] = 0
    self.matriz[endPos[0]][endPos[1]] = 1
    self.come(initPos, endPos)

  def come(self, initPos, endPos):
    pos = self.opcaoMovimento(initPos, endPos)
    self.matriz[pos[0]][pos[1]] = 0
    self.campos = -1

  #condicoes de verificação da busca
  def opcaoMovimento(self, initPos):
    options = []
    if(self.matriz[initPos[0]][initPos[1]] == 1):

      if(initPos[0] - 2 >= 0 and self.matriz[initPos[0]-2][initPos[1]] == 0):
        p = [initPos[0]-2, initPos[1]]
        consomePos = self.opcaoConsumo(initPos, p)
        if(self.matriz[consomePos[0]][consomePos[1]] ==1):
          options.append(p)

      if(initPos[0] + 2 <len(self.matriz)  and self.matriz[initPos[0]+2][initPos[1]] == 0):
        p = [initPos[0]+2, initPos[1]]
        consomePos = self.opcaoConsumo(initPos, p)
        if(self.matriz[consomePos[0]][consomePos[1]] ==1):
          options.append(p)

      if(initPos[1] - 2 >= 0 and self.matriz[initPos[0]][initPos[1]-2] == 0):
        p = [initPos[0], initPos[1] - 2 ]
        consomePos = self.opcaoConsumo(initPos, p)
        if(self.matriz[consomePos[0]][consomePos[1]] ==1):
          options.append(p)

      if(initPos[0] + 2< len(self.matriz[0]) and self.matriz[initPos[0]][initPos[1]+2] == 0):
        p = [initPos[0], initPos[1]+2]
        consomePos = self.opcaoConsumo(initPos, p)
        if(self.matriz[consomePos[0]][consomePos[1]] ==1):
          options.append(p)

      return options

    return []

  def opcaoConsumo(self, initPos, endPos):
    return [endPos[0], round((initPos[1] + endPos[1])/2)] if initPos[0] == endPos[0] else [round((initPos[0] + endPos[0])/2), endPos[1]]

  def quebraEntrada(self, inp):
    pos = inp.split(";")
    return [ord(pos[0]) - 97, int(pos[1]) - 1]

  def limpaTela(self):
    os.system('cls' if os.name == 'nt' else 'clear')

r = Resta()

"""
valida(px, py) && tab[px][py] == 'B' &&

((px == dx && abs(dy-py) == 2) || (py == dy && abs(dx-px) == 2)) &&

tab[(px-dx)/2 + dx][(py-dy)/2 + dy] == 'P');

origem (1,3)
destino (3,3)

valida(3,3) && tab[3][3] == 0 &&
((3==1)&& modulo(3-3)==2)ou(3==3&& modulo(1-3)==2)
&& tab[(3-1)/2+1][(3-3)/2+3]==1

tab[(3-1)/2+1][(3-3)/2+3]= tab[2][3]
"""
