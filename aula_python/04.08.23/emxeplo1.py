#Exemplo da funcao range()
#print(list(range(2,20)))#lista do valor 2 ate 19
#print(list(range(10)))#lista do valor 0 ate 9
#print(list(range(10,100,5)))#lista do valor 10 ate 100 contando de 5 em 5
#for i in range(10):
#    print(i)
#print("\n valor final do contador:",i)
#print("-"*50)
#contagem de 20 ate 30 usando laco for
#for i in range(20,31):
#    print(i)
#print("\n valor final do contador:",i)
#print("-"*50)
#contagem 10 até zero usando o laço for
#for i in range(10,-1,-1):
#    print(i)
#Leia 5 numeros inteiros e mostre uma mensagem quando o numero for par
#for i in range (5):
#    num = int(input('informe um valor:'))
#    if num%2==0:
#        print('O valor informado e par!')
#Leia 5 numeros e some somente os valores impares e mostre a quantidade de impares
soma = 0
cont_impar=0
for i in range (5):
 
    num = int(input('informe um valor:'))
    if num%2==1:
        soma+=num
        cont_impar+=1
print(f'A soma dos impares valor = {soma} e foram {cont_impar} numeros de impares digitados!')
#Mostre a média aritmetica dos impares
media=soma/cont_impar
print(f'A media = {media:.2f}')
