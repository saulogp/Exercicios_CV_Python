def tabuada(x):
    i = 0
    while i <= 10:
        print("{} x {} = {}".format(x, i, x * i))
        i = i + 1

num = int(input("Digite um número: "))

tabuada(num)
