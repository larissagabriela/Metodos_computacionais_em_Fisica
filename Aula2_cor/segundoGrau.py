'''
Viviane
O programa roda e fornece os resultados esperados para todas as raizes.
Obs 1: Poderia ter limitado as casas decimais em algumas respostas (linha 45 e 46) 
Obs: Não se deve comparar uma variável float usando == pois os números no computador são aproximados. Deve-se usar if fabs(delta)<1.e-12  (ou qualquer numero muito pequeno) 
'''

#!/usr/bin/env python
# coding: utf-8

# In[4]:


from math import * #Importar a lib para trabalhar com raízes, por exemplo
#Dizer o que o programa faz
print ("Esse programa calcula as raízes de uma equação do segundo grau.\nSabendo que a equação o segundo grau tem a forma ax² + bx + c = 0")
#Pedir o valor de a
a = float(input("Digite o valor de a: "))
#Enquanto a for igual a zero, pedir novamente o valor de a e informar o porquê
while a == 0:
    print ("O valor de a deve ser diferente de zero")
    a = float(input("Digite o valor de a: "))
#Pedir o valor de b e o valor de c
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
#Calcular o valor de delta
delta = b**2 - 4*a*c


# In[6]:


#Agora, trabalhar com as condições para cada valor de delta
if delta == 0:
    print ("A equação possui uma raiz real. O valor de x é: ", (-b)/(2*a))
elif delta > 0:
    x1 = ((-b + (sqrt(delta))) / (2*a))
    x2 = ((-b - (sqrt(delta))) / (2*a))
    print ("X pode assumir dois valores reais: %.2f e %.2f" %(x1, x2))
else:
    from cmath import sqrt #Aqui importar essa lib para trabalhar com raiz negativa
    x1 = ((-b + (sqrt(delta))) / (2*a))
    x2 = ((-b - (sqrt(delta))) / (2*a))
    print ("X possui duas raízes complexas")
    print ("Um possui valor real igual a %.f e valor imaginário igual a %.3f" %(x1.real,x1.imag))
    print ("Um possui valor real igual a %.f e valor imaginário igual a %.3f" %(x2.real,x2.imag))

