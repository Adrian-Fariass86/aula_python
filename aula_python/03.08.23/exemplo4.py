#soma 5 valores positivos informados pelo usuario
soma = 0
cont = 1
while cont<=5:
    valor = float(input('informe um valor positivo:'))
    if valor<0:
        print('digite um numero positivo!!!')
        continue
        #break
        #pass
    elif valor>0 :
        soma += valor
        cont += 1
print(f"O resultado da soma é = {soma}")
