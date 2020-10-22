'''
 - Erro na função taylor_seno:
   [linha 31] 'for n in range(0,n+1)' em vez de 'for n in range(n)'
 - Sem erros na comparação com a diferença entre o valor da biblioteca e o da série;
   o valor obtido está errado devido ao erro na construção da função
 - Erro no gráfico:
   [linhas 45 a 48 e 52 a 55] Plotou a função com 'n' termos como sendo o função com
   'n+1' termos. Por essa razão, o erro cometido na construção da função é compensado
   e o gráfico parece estar correto.
5/6
'''
#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import matplotlib.pyplot as plt
from math import *
"""
Esse programa plota o gráfico da funçãos seno
"""

def taylor_seno(x,n):
    '''
    Essa função calculo o seno de um ângulo
    return: seno
    '''
    sen = 0                                                  #Definir um valor inicial para sen como zero
    for n in range(0,n+1):                                   #Esse for percorre um valor de n até que ele chegue ao valor de entrada 
        sen += ((-1)**n)/(factorial(2*n+1))*(x**(2*n+1))     #Escrever o somatório do seno
    return sen

x = float(input("Entre com o valor do ângulo: "))
n = int(input("Entre com o valor de n: "))

print("O valor de seno(x) utilizando Série de Taylor é: ", taylor_seno(x,n))
print("O valor de seno(x) utilizando a lib math: ", sin(x))
print("A diferença entre os valores é",sin(x) -  taylor_seno(x,n))   #Calcular a diferença entre o seno da serie de taylor e da função sin
termo_seguinte = taylor_seno(x,n+1) - taylor_seno(x,n)               #Calcular o valor do próximo termo 
print("O termo seguinte é: ",termo_seguinte)                         #Esse termo deve ter a mesma ordem do erro
x_ = np.linspace(0, 3*np.pi/2, 51)       #x no intervalo de 0 a 3pi/2
y = np.sin(x_)
y1 = taylor_seno(x_,1)
y2 = taylor_seno(x_,2)
y3 = taylor_seno(x_,3)
y4 = taylor_seno(x_,4)

xgraus = x_ * 180 / np.pi               #Converter de radiano para graus
plt.plot(xgraus,y, label='Sen(x)')      #Plotar o gráfico para diferentes n
plt.plot(xgraus,y1, label='N = 2')
plt.plot(xgraus,y2, label='N = 3')
plt.plot(xgraus,y3, label='N = 4')
plt.plot(xgraus,y4, label='N = 5')

#Embelezar o gráfico
plt.ylabel('Sen(x)')
plt.xlabel('Ângulo (graus)')
plt.title('Gráfico do seno')
plt.grid(True)
plt.ylim(-2,2)
plt.legend()
plt.show()

