#!/usr/bin/env python
# coding: utf-8
"""
- Sem erros.
"""
# In[20]:

"""
Esse programa calcula a soma dos elementos de uma lista
"""
lista1 = [1,2,3]               #Definir as listas
lista2 = ['Hello, ', 'World!'] 
lista3 = [[1, 2],[4,3]]        
def mysum(x):                  #Essa função calcula a soma dos elementos de uma função
    """
    Calcula a soma dos elementos de uma lista
    return: a soma dos elementos da lista
    """
    soma = x[0]                #A variável assume o valor do primeiro item da lista
    for i in x[1:]:            #Percorrer cada elemento da lista a partir do segundo
        soma += i              #Somar cada valor da lista na variável soma
    return soma
print(mysum(lista1))
print(mysum(lista2))
print(mysum(lista3))

