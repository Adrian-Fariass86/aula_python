#Leia 3 notas e mostre a média, caso seja digitado um valor negativo ou acima de 10 será solicitado um novo valor
soma = 0
cont = 1
while cont<=3:
    nota = float(input('informe sua nota:'))
    
    if nota<0 or nota>10:
        print('digite um novo valor')
        continue
    soma += nota
    cont += 1
    #elif nota>10 :
    #    print('digite um novo valor')
    #    continue
    #else:
    #    soma += nota
    #    cont += 1
media=soma/3
print(f"A média é: {media:.1f}")

'''if media>=7:
    print("Aprovado!!")
else:
    print("Reprovado!!")'''