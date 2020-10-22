'''
sem erros
'''
# -*- coding: utf-8 -*-
from math import *  #Importar a lib math
print 'Esse programa calcula a equação da Gaussiana para m = 0, s = 2 e x = 1'
m = 0  #Declarar as variáveis com seus respectivos valores
s = 2.
x = 1
f = (1 / ((sqrt(2 * pi)) * s)) * exp((-1. / 2) * ((x - m) / s)**2)  #Escrever a função no formato do python2
print 'O valor de f(x) é: ', f  #Mostrar o valor da função
