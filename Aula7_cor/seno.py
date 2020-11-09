#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
def f(y):
    '''
    Definir a função gaussiana
    retunrn: A função Gaussiana
    '''
    fy = np.sin(y)
    return fy

def trapezio(f,a,b,k):
    '''
    Implementar o método do trapézio
    return: a função tk para calcular a integral
    '''
    deltak = (b - a)/2**k
    j = 1
    soma = 0
    while j <= (2**k-1):
        y = a + j*deltak
        fj = f(y)
        soma += fj
        j += 1
    tk = deltak/2 *(f(a) + 2*soma +f(b))
    return tk

def simpson(tk_, tk_1):
    '''
    Implementar o método de Simpson
    return: a função sk para calcular a integral
    '''
    sk = tk_ + (tk_ - tk_1)/3
    return sk

a = 0                         #Limites de integração
b = np.pi
k = np.array(range(0,21,1))    #Valores em k pode variar (levando em consederação que na aula foi dito que 20 já poderia ser um valor alto)
precisao = 10**-6

cont = 0                       #Método de convergência para o método dos trapézios
for cont in k:
    if abs(trapezio(f, a, b, k[cont+1]) - trapezio(f, a, b, k[cont])) < precisao:
        break

cont1 = 0                       #Método de convergência para o método de Simpson
for cont1 in k:
    if cont1==0:
        tk_1 = trapezio(f, a, b, k[cont1])
        tk_ = trapezio(f, a, b, k[cont1+1])
        sk_ = simpson(tk_, tk_1)
    else: 
        tk_1 = trapezio(f, a, b, k[cont1])
        tk_ = trapezio(f, a, b, k[cont1+1])
        sk_1 = simpson(tk_, tk_1)
        if abs(sk_1 - sk_) < precisao:
            break
        sk_ = sk_1 
trap = trapezio(f, a, b, cont)
print("O valor da integral da função Gaussiana pelo método dos trapézios no intervalo de a até b é %.3f usando k igual a %d" %(trap, cont))
simp = simpson(tk_, tk_1)
print("O valor da integral da função Gaussiana pelo método de Simpson no intervalo de a até b é %.3f usando k igual a %d "%(simp, cont1))

#Para o caso de funções pares, podemos otimizar utilizando o intervalo, nesse caso, de [0,2] e multiplicando o valor da integral por 2.
#Isso pode ser feito por conta simetria. Os intervalos [-2,0] e [0,2] teriam valores de área iguais. 
#Usando um dos intervalos de multiplicando por 2 poderíamos diminuir o tempo de execução do programa.

