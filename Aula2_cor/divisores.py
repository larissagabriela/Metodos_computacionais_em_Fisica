'''
Sem erros.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Mostrar o que o programa faz
print("Esse é um programa que mostra os divisores de um número e a quantidade de divisores")
#Pedir o número
x = int(input("Entre com um número inteiro e positivo: "))
while x <=0: #O número precisa ser positivo, então de alertar se colocar um número negativo ou igual a zero
    print("O número precisa ser positivo")
    x = int(input("Entre com um número inteiro e positivo: "))
#Declarar duas variáveis como zero(elas mudarão seu valor)
n = 0
div = 0
#Escrever uma frase que indica os divisores
print("Os divisores são: ")
#Esse while calcula os os devisores através de algumas condições
while n <= x:      #Rodar o loop enquanto n for menor ou igual a x
    n = n + 1 
    if x%n == 0:   
        div += 1
        print(n)
#Por fim, printar o número de divisores
print("O número %d tem %d divisores" %(x , div))

