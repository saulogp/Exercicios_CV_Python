texto = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
x = True
while x == True:
    num = int(input("Digite um número de 0 e 5: \n>>>"))
    if num >= 0 and num <= 5:
        print("Número {}".format(texto[num]))
        break
    x = True