#questãonumber2

print ("Eae meu mano, quer saber a quanto tempo você eestá neste planeta deplorável?Não?Não importa, você vai participar de qualquer jeito.")

ddn = int(input("Primeiramente me informe o dia de vosso nascimento:"))
mdn = int(input("Agora me informe o mês de vosso nascimento:"))
adn = int(input("E por último, me informe o ano de vosso nascimento:"))

da = int(input("Agora por favor informe qual é o dia de hoje:"))
ma = int(input("Agora informe o mês atual:"))
at = int(input("E por último o ano atual:"))

ia = at - adn

if mdn >= ma:
    if mdn == ma:
        if ddn > da:
            ia 
    else:
        ia - 1
        
ddv = (30 - ddn) + ((12 - mdn)*30) + ((ma - 1)*30) + da + (ia) * 365

print (ddv)