#maneira mais eficiente - Versão Alfa

from math import sqrt # importando o método de cálculo de raiz quadrada da biblioteca de matemática

class Ponto: # classe para definir valores de x e y
  def __init__(self, x, y):
    self.x = x
    self.y = y

def calcular_distancia(p1,p2): # função para calcular a fórmula de distancia entre dois pontos
  return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

ponto1 = Ponto(2,3) #valores de xb,xa
ponto2 = Ponto(-2,-2) #valores de yb, ya

print(calcular_distancia(ponto1, ponto2)) #printando o resultado

#maneira mais simples - Versão Beta
import math

#user inserindo valores
xA = int(input("Digite o valor de xA: "))
yA = int(input("Digite o valor de yA: "))
xB = int(input("Digite o valor de xB: "))
yB = int(input("Digite o valor de yB: "))

#fórmula
dAB = (((xB - xA) ** 2) + ((yB - yA)  ** 2))
raiz = math.sqrt(dAB)
#printando o resultado
print(f'\nA raiz quadrada de {dAB} é {raiz}\n')