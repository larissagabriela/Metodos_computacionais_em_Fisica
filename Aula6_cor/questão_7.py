# -*- coding: utf-8 -*-
"""questão 7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FYecwsj4tvkToTkmKLsabkb4zoyWJ_QI
"""

'''
Esse programa calcula o valor da primeira raiz positiva da função f(x) = e^−x − sin((pi*x)/2)
Quando x está no intervalo de 0 e 4
'''
import matplotlib.pyplot as plt
import numpy as np
import sys

#Função definida na tarefa anterior
def funcao1(x):
  '''
  Essa função calcula a função  f(x) = e^−x − sin((pi*x)/2)
  return: f(x)
  '''
  y = np.exp(-x) - np.cos(np.pi*x/2)
  return y

def derivada(x):
  '''
  Função que determina a derivada da funcao1
  return: derivada
  '''
  derivada_ = -np.exp(-x) + (np.pi*np.sin(np.pi*x/2))/2
  return derivada_

x_ = np.linspace(0, 4)    # O eixo x no intervalo de x ∈ [0, 4]
y = funcao1(x_)            # y assumindo o valor da funcao em relação a x_
plt.ylabel('f(x)')
plt.title('Gráfico da função f(x) = e^−x − sin((pi*x)/2)')
plt.grid(True)
plt.plot(x_,y)
plt.show()

xo_ = 0.5                         #Definir xi
fxo_ = funcao1(xo_)
flinhaxo_ = derivada(xo_)
x_ = xo_ - (fxo_/flinhaxo_)
a = derivada(xo_)
delta = 1.e7                      #Valor muito maior que a precisão
interacao = 100
precisao = 1.e-7

nit = 0

while abs(delta) > precisao and nit < interacao:      #Enquanto essas condições forem obedecidas
  x = xo_ - funcao1(xo_)/derivada(xo_)
  delta = x - xo_
  xo_ = x
  nit += 1

print("O número de interações é %d e a raiz é %f" %(nit, xo_))