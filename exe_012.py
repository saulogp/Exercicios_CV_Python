'''Desconto de 5%'''
prod = float(input("Preço do produto: R$"))
preco_final = prod - (prod * 5 / 100)

print("O produto que custava R${}, com 5% de desconto passa a valer R${:.2f}.".format(prod, preco_final))
