'''15.	Faça um script em Python que leia o valor do salário de um funcionário e mostre se o salário é maior ou menor que o valor mínimo.'''
salario = float(input("Informe o seu salário R$: "))
salario_minimo = 1320.00
if salario>salario_minimo:
    print(f" O seu salário de R${salario} é maior que o valor mínimo")
else:
    print(f" O seu salário de R${salario} é menor que o valor mínimo")