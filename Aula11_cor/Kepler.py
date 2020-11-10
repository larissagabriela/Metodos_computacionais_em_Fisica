'''
 - [linhas 54 a 56] Os valores usados para 'n' estão incorretos.
   Para passos h de dia, hora e minuto deveriam ser usados n=365,
   n=24*365 e n=60*24*365, respectivamente.
 - [linha 73] Valor de 'n' para o método de Runge-Kutta está incorreto.
   Para um passo h de um dia deveria ser usado um n=365.
OBS: A questão 3 não foi respondida.
OBS: Faltaram legendas nos eixos x e y do gráfico.
OBS: A legenda 't' do gráfico é inadequada.

'''
#!/usr/bin/env python
# coding: utf-8

# In[15]:


'''
Programa que usa o Metodo de Euler para calcular a trajetória da Terra
'''
import numpy as np
import matplotlib.pyplot as plt

def derivada(x,t):
    '''
    Definir a função derivada
    return: derivada
    '''
    di = -g*Massa_sol*(x[0]/(np.sqrt(x[0]**2+x[1]**2)**3))
    dii = -g*Massa_sol*(x[1]/(np.sqrt(x[0]**2 + x[1]**2)**3))
    return np.array([x[2], x[3], di, dii])

def euler(to, tf, xo, derivada,n):
    '''
    Definir o método de Euler
    Essa função tem como argumentos a EDO, o t inicial, x inicial, derivada e n
    '''
    t = np.zeros(n)
    if isinstance(xo, (float, int)):
        x = np.zeros(n, len(xo))
    else:
        x = np.zeros((n, len(xo)))
    x[0] = xo
    t[0] = to
    h = (tf-to)/n
    for i in range(n-1):
        t[i+1] = t[i] + h
        x[i+1] = x[i] + h*derivada(x[i], t[i])
    return t, x

to = 0    #Definir as condições exigidas
tf = 31536000
xo = np.array([1496*10**8, 0, 0, 297*10**2])
n = 3600 #para precisão de hora
#n = 60 para precisão de minuto
#n = 86400 #para precisão de dia
Massa_sol = 198*10**28
g = 667*10**-13

x, t = euler(to, tf, xo, derivada, n)

#Plotar o gráfico que mostra a trajetória ao redor da terra
plt.plot(t[:,0], t[:,1], label = 't')
plt.title("Trajetória da Terra com precisão de hora")
plt.legend()
plt.show()


# In[7]:


from rk4 import RungeKutta4
n1 = 86400 #precisão de dia
x_runge, t_runge = RungeKutta4(derivada, xo, to, tf, n1)


# In[9]:


plt.plot(x_runge[:,0], x_runge[:,1], label = 't')
plt.title("Movimento da Terra ao redor do Sol com precisão de dia")
plt.legend()
plt.show()
