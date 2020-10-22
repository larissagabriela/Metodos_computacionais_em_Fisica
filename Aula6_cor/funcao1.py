# -*- coding: utf-8 -*-
"""funcao1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hfHE0l3_GQIDPoSO_yV9jmsW4cIc8Pof
"""

'''
Esse programa plota o gráfico de f(x) = e^−x − sin((pi*x)/2)
Com x ∈ [0, 4]
'''

import matplotlib.pyplot as plt
import numpy as np

def funcao1(x):
  '''
  Essa função calcula a função  f(x) = e^−x − sin((pi*x)/2)
  return: f(x)
  '''
  y = np.exp(-x) - np.sin(np.pi*x/2)
  return y

x_ = np.linspace(0, 4)    # O eixo x no intervalo de x ∈ [0, 4]
y = funcao1(x_)            # y assumindo o valor da funcao em relação a x_
plt.ylabel('f(x)')
plt.title('Gráfico da função f(x) = e^−x − sin((pi*x)/2)')
plt.grid(True)
plt.plot(x_,y)
plt.savefig("funcao1.pdf")
plt.show()