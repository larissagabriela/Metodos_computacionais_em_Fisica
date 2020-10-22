'''
- Sem erros.

OBS: Sem rótulo no eixo Y
'''

#!/usr/bin/env python
# coding: utf-8

# In[23]:


''' 
Esse programa calcula o desvio padrão e a média de medidas da gravidade
Além disso plota um histograma com 20 bins e 60 bins
'''

import matplotlib.pyplot as plt                         
import numpy as np
from math import *
grav = np.loadtxt("gravidade.dat")                      #Ler o arquivo.dat
plt.hist(grav, bins = 20, ec = 'k', label = '20 bins')  #Plotar gráfico para 20 bins e 60 bins
plt.hist(grav, bins = 60, ec = 'k', label = '60 bins')

#Embelezar o gráfico
plt.xlabel('Gravidade (cm/s²)')                 
plt.title('Histograma de medidas da gravidade')
plt.legend()

media = sum(grav)/len(grav)                      #Calcular média
print("A média das notas é: %.2f" %media)
des_pad = 0                                      
for x in grav:                                   #Esse lool calcula o valor do desvio padrão  
    des_pad += (x - media)**2                   
dp = sqrt((1/(len(grav) - 1))*des_pad)           
print("O desvio padrão das notas é: %.2f" %dp)

#Usando funções .std() e .mean() para calcular a média e o desvio padrão
desvio_padrao = grav.std()
print("O desvio padrão das medidas usando .std é: %.2f" %desvio_padrao)
media = grav.mean()
print("A média das medidas usando .mean é: %.2f" %media)
