#!/usr/bin/env python
# coding: utf-8

# In[3]:
'''
- Sem erros.

OBS: Poderia ter feito uma breve introdução sobre do que se trata o programa
'''

#Importe a lib numpy
import numpy as np
from math import *

#Carregar o arquivo .txt
notas = np.loadtxt("media")
print(notas)  #Mostrar as notas

#A função len conta a qauntidade de termos o array
num_alunos = len(notas)
print("O número de alunos é: ", num_alunos)   #Mostrar o número de alunos

#Para calcular a média soma-se todas as notas com o sum e divide pelo número de alunos
media = sum(notas)/num_alunos
print("A média das notas da turma foi: %.1f" %media)  #Mostrar a média

#A partir daqui calcula-se o valor do desvio padrão
des_pad = 0                                  #Definir variável de controle
for x in notas:                              #Fazer o loop em cada termo do array
    des_pad += (x - media)**2                #Escrever o termo do somatório
dp = sqrt((1/(num_alunos - 1))*des_pad)      #Incluir o somatório na foŕmula geral do desvio padrão
print("O desvio padrão das notas é: %.1f" %dp)   #Mostrar o desvio padrão

aprovado = 0          #Definir três variáveis de controle
reprovado = 0
prova_final = 0
for x in notas:       #Esse for percorre todos os termos do array
    if x >= 7:        #Esse if soma 1 na variável aprovado toda vez que a condição é verdadeira
        aprovado += 1
    elif x<3:         #Esse elif soma 1 na variável reprovado toda vez que a condição é verdadeira
        reprovado +=1
    else:             #Esse else soma 1 na variável prova_final(adicionei para ficar mais bonito) toda vez que a condição é verdadeira
        prova_final += 1
print("O número de aprovados direto com nota maior ou igual a 7:", aprovado)  #Mostrar o número de aprovados
print("O número de reprovados direto com nota menor que 3:", reprovado) #Mostrar o número de reprovados
print("O número de alunos que precisarão de prova final será:", prova_final)   #Mostrar o número de provas finais

#Usando .std ele calcula o desvio padrão sem necessidade de muitas linhas de código
print("O desvio padrão usando o np.std(array) é: %.1f" %(np.std(notas)))

#Usando .mean ele calcula a média sem necessidade de foŕmula
print("O média usando o np.mean(array): %.1f" %(np.mean(notas)))

