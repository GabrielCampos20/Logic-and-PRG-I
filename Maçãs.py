print ("Boa tarde, estou vendendo maçãs, veja a seguir os valores:")
print ("Até   12   maçãs - 1,30R$ a unidade")
print ("12 ou mais maçãs - 1,00R$ a unidade")
print ("Quantas maçãs deseja comprar?")
maçãs = int(input(""))
if maçãs < 12:
    print ("Certo, então",maçãs,"maçãs vão lhe custar",maçãs*1.30)
if maçãs >= 12:
    print ("Certo, então",maçãs,"maçãs vão lhe custar", maçãs*1)
    
