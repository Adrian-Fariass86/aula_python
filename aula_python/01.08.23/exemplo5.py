#Leia a idade do usuario e informe se ele eh maior ou menor de idade
#verificar numeros negativos antes da idade
idade = int(input("digite sua idade: "))
if idade <=0:
    print("idade invalida!!")
    print("verifique o valor informado!!")
else:
    if idade >= 18:
        print("Você é de maior!")
# elif idade <= 0:
    # print("essa idade não existe, digite sua idade!")
    else:
        print("Você é de menor!")