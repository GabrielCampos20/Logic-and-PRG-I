import random
d1 = 1 
d2 = 2 
d3 = 3 
d4 = 4 
d5 = 5 
d6 = 6 
dado = [d1, d2, d3, d4, d5, d6]
n = random.choice(dado)
print ('Vc tirou {}'.format(n))
if n == 1:
    print ("A")
if n == 2:
    print ("B")
if n == 3:
    print ("C")
if n == 4:
    print ("D")
if n == 5:
    print ("E")
if n == 6:
    print ("F")
