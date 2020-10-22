'''
Gabriella
 - sem erros
'''
#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Mostrar o que o programa faz
print("Esse programa calcula o valor do seno de um ângulo: ")
#Importar a lib math
from math import *
#Pedir o valor do ângulo e o valor de n
x = float(input("Entre com o valor do ângulo: "))    
n = int(input("Entre com o valor de n: "))


# In[3]:


sen = 0                    #Definir um valor inicial para sen como zero
for n in range(0,n+1):     #Esse for percorre um valor de n até que ele chegue ao valor de entrada 
    sen += ((-1)**n)/(factorial(2*n+1))*(x**(2*n+1))     #Escrever o somatório do seno
print("O valor do seno através da fórmula é:" ,sen)       #Mostrar o valor do seno


# In[4]:


#Calculando o valor do seno usando seno usando sin da lib math
print("O valor do seno usando o sin da lib math é:", sin(x))

