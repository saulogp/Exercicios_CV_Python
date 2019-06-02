salario = float(input("Qual o salario do funcionario: "))
reajuste = 15
salario_atual =salario +(salario * reajuste / 100)
print("O salario de R${}, teve {}% de reajuste: R${:.2f}.".format(salario, reajuste, salario_atual))
