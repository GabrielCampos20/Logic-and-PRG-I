matriz = []

for i in range (5):
    vetor = []
    for j in range (5):
        if i == j:
            vetor.append(1)
        else:
            vetor.append(0)
    matriz.append(vetor)
print (matriz)
            