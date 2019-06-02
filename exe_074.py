tupla = (1, 3, 5, 2, 6)
print(tupla)
maior = [0]
for i in range(0, 5):
    if maior <= tupla[i]:
        maior = tupla[i]
    else:
        menor = tupla[i]
print(maior, menor)
