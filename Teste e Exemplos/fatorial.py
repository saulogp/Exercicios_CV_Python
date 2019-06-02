def fatorial(n):
    if n <= 1:
        return 1
    else:
        vfatorial = n * fatorial(n - 1)
        return vfatorial


num = int(input("Deseja resolver o fatorial de qual número?\n>>>"))
f = float(fatorial(num))
print("O fatorial de", num, "é", f)
print("O fatorial de {} é {}".format(num, f))
print("O fatorial de {1} é {0}".format(num, f))
print(f'O fatorial de {num} é {f}')
