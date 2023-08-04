#soma 5 valores negativos informados pelo usuario
'''soma = 0
cont = 1
while cont<=5:
    valor = float(input('informe um valor negativo:'))
    if valor>0:
        print('digite um numero negativo!!!')
        break
    elif valor<0 :
        soma += valor
        cont += 1
print(f"O resultado da soma é = {soma}")'''
inicio = int(input('digite o valor incial:'))
fim = int(input('digite o valor final:'))
while inicio <= fim:
    if inicio%2==1:
        print(inicio)
    inicio+=1


