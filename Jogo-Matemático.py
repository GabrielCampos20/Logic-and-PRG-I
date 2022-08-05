#jogo de aprendizado matemático

import random
o1 = ("+")
o2 = ("-")
operação = [o1, o2]
op1 = random.choice(operação)

import random
n1 = 1 
n2 = 2 
n3 = 3 
n4 = 4 
n5 = 5 
n6 = 6
n7 = 7
n8 = 8
n9 = 9
cálculo = [n1, n2, n3, n4, n5, n6, n7, n8, n9]
nu1 = random.choice(cálculo)

import random
n1 = 1 
n2 = 2 
n3 = 3 
n4 = 4 
n5 = 5 
n6 = 6
n7 = 7
n8 = 8
n9 = 9
cálculo = [n1, n2, n3, n4, n5, n6, n7, n8, n9]
nu2 = random.choice(cálculo)

import random
n1 = 1 
n2 = 2 
n3 = 3 
n4 = 4 
n5 = 5 
n6 = 6
n7 = 7
n8 = 8
n9 = 9
cálculo = [n1, n2, n3, n4, n5, n6, n7, n8, n9]
nu3 = random.choice(cálculo)

import random
n1 = 1 
n2 = 2 
n3 = 3 
n4 = 4 
n5 = 5 
n6 = 6
n7 = 7
n8 = 8
n9 = 9
cálculo = [n1, n2, n3, n4, n5, n6, n7, n8, n9]
nu4 = random.choice(cálculo)

print ("Olá, vamos testar seu nível de matemática?")
print ("Pra começar, seleciona e dificuldade.")
print ("1 = Fácil")
print ("2 = Médio")
print ("3 = Difícil")
dificuldade = int(input(""))
if dificuldade == 1:
    print ("Certo, vamos começar então.")
    print ("Questão 1: quanto é",nu1,op1,nu2,"?")
    resposta = int(input(""))
    if resposta == nu1+nu2:
        print ("Acertou")