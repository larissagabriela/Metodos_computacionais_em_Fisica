# -*- coding: utf-8 -*-
"""pontosLagrange.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-Ve1mEXiu8Y8HgignUqxiBOQ_7bgXTYN
"""

'''
Esse programa calcula a distância do Sol à Terra
'''
def funcao1(x):
  '''
  return: f(x)
  '''
  y = (g*M)/(x**2) - g*m/(R-x)**2 - (omega**2)*x
  return y

def derivada(x):
  '''
  Função que determina a derivada da funcao1
  return: derivada
  '''
  derivada_ = -g*2*M/x**3 - g*2*m/(R-x)**3 - omega**2
  return derivada_
 
R = 1.5*10**(11)                               #Definir constantes
g = 6.674*10**(-11)
M = 1.989*10**(30)
m = 5.9736*10**(24)
omega = 1.992*10**(-7)

xo = 0.5                                           #Definir xi
delta = 1.e7
interacao = 100
precisao = 1.e-7

nit = 0

while abs(delta) > precisao and nit < interacao:      #Enquanto essas condições forem obedecidas
  x = xo - (funcao1(xo)/derivada(xo))
  delta = x - xo
  xo = x
  
  nit += 1

print("A distância entre o sol e a Terra é:" , xo)