'''
O programa roda mas não fornece resultados esperados para o caso de ângulos de 0 e 180 graus. Além de possuir um erro para vetores de módulo nulo.
Erro: Observe que os parâmetros fornecidos para a função
em sua definição são x e y e não vetor1 e vetor2.
Erro:  não impôs uma condição que impede o cálculo do cosseno para o caso de um ou mais vetores possuirem módulo nulo (divisão por zero).
Erro: Por tratar-se de uma variável float, os números no computador são aproximados. 
Portanto, para que seja possível calcularmos o valor exato do cosseno para ângulos paralelos, 
anti-paralelos e perpendiculares, devemos realizar arredondamentos utilizando a função round(), por exemplo.

'''
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from math import * 

print("Esse programa calcula o ângulo formado por dois vetores de três dimensões")
def angulo(x, y): #Criar a função para calcular o cosseno
    """
    Calcula o cosseno do ângulo formado por dois vetores que possuem três coordenadas(x1,y1,z1) e (x2,y2,z2)
    return: o cosseno (float) do ângulo 
    """
    x1 = vetor1[0]
    y1 = vetor1[1]
    z1 = vetor1[2]
    x2 = vetor2[0]
    y2 = vetor2[1]
    z2 = vetor2[2]
    #Escrever a função que determina o cosseno do ângulo
    cosseno = (np.dot(vetor1,vetor2)) / ((sqrt((x1)**2 + y1**2 + z1**2)) * (sqrt((x2)**2 + (y2)**2 + (z2)**2)))                                 
    return cosseno
vetor1 = list() #Criar listas para entrar com o valor das coordenadas dos vetores
vetor2 = list()
for c in range(1, 4): #Esse for pede os valores e adiciona na lista vetor1
    x = float(input(f'Digite a {c}ª coordenada do vetor 1: '))
    vetor1.append(x)
for c in range(1, 4): #Esse for pede os valores e adiciona na lista vetor2
    y = float(input(f'Digite a {c}ª coordenada do vetor 2: '))
    vetor2.append(y)
ang = angulo(vetor1, vetor2)  #Aplicar a função para as coordenadas do vetor 1 e do vetor 2
ang2 = acos(ang)              #Encontrar o ângulo (em radianos) formado pelos vetores através do arcosseno
graus = ang2 * (180/pi)       #Converter o angulo de radianos para graus
print(angulo.__doc__)
print("O ângulo em radiano é: %.2f" %ang2)
print("O ângulo em graus é: ", graus)


# In[ ]:





# In[ ]:




