#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np

def funcao2(x):
    '''
    Essa função calcula a função  f(x) = e^−x − sin((pi*x)/2)
    return: f(x)
    '''
    y = np.sin(0.1*x**2+3) - np.sqrt(2/x)
    return y

x_ = np.linspace(2, 10)    # O eixo x no intervalo de x ∈ [0, 4]
y = funcao1(x_)            # y assumindo o valor da funcao em relação a x_
plt.ylabel('f(x)')
plt.title('Gráfico da função f(x) = e^−x − sin((pi*x)/2)')
plt.grid(True)
plt.plot(x_,y)
plt.savefig("funcao1.pdf")
plt.show()

