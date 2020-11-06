#!/usr/bin/env python
'''
 - Sem erros.

OBS: Não utiliza o parâmetro "deriv" passado como argumento da função euler(). Ao invés disso usa diretamente a derivada
definida anteriormente.
'''

# coding: utf-8

# In[1]:


'''
Esse problema calcula a EDO f'(x) = x²+1
'''
import numpy as np
import matplotlib.pyplot as plt

def derivada(x,t):
    '''
    Definir a função derivada
    return: derivada
    '''
    deriv = x**2+1
    return deriv

def euler(deriv, xo, to,tf,n):
    '''
    Definir o método de Euler
    Essa função tem como argumentos a EDO, o x inicial, tempo inicial, tempo final e o número de partições
    '''
    t = np.zeros(n)
    x = np.zeros(n)
    x[0] = xo
    t[0] = to
    h = (tf-to)/n
    for i in range(n-1):
        t[i+1] = t[i] + h
        x[i+1] = x[i] + h*derivada(x[i], t[i])
    return x, t

to = 0    #Definir as condições exigidas
tf = 1
xo = 0
n = 5     #Quanto mais n mais pontos serão acrescentados no gráfico

x, t = euler(derivada, xo, to, tf, n) 

#Plotar o gráfico comparando com a solução (solução esperada tan(t)) com a solução esperada
plt.plot(t, x, 'b.', label = 'numérico')
plt.plot(t, np.tan(t), 'r.', label = 'exato')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.show()

