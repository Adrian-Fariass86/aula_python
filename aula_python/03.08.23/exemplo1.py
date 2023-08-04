#estrutura  de repetição while(continuação)
#Leia 5 numeros e mostre a soma de todos os valores informados

cont = 1
soma = 0 #acumulador
while cont<=5:
    num=float(input('Digite mais um valor:'))
    #print(cont)
    soma = soma+num
    cont+=1
print(f"Resultado da soma é:  {soma:.0f}")
