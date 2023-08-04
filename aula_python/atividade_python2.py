''' 1.	Crie um script em Python para receber dois números informados pelo usuário e mostrar todos números entre eles em ordem decrescente.
num1 = int(input('digite o valor incial:'))
num2 = int(input('digite o valor final:'))

if num1>num2:
    while num1>=num2:
        print(num1, end=" ")
        num1-=1

elif num1<num2:
    while num2>=num1:
        print(num2, end=" ")
        num2-=1     
else:
    print('valores iguais!!')'''

'''2.	Faça um script que mostre uma contagem iniciando em 10, finalizando em 500 com incremento de 5 em 5.
a=10
b=500
while a<=b:
    print(f'{a}')
    a=a+5'''

'''3.	Faça um script que mostre os números pares em um intervalo definido pelo usuário.
inicio = int(input('digite o valor incial:'))
fim = int(input('digite o valor final:'))
while inicio <= fim:
    if inicio%2==0:
        print(inicio)
    inicio+=1'''

''' 4.	Faça um script que leia dois valores positivos e mostre a soma dos números ímpares entre eles.
n1 = int(input('digite o valor incial:'))
n2 = int(input('digite o valor final:'))
soma=0
if n1>0 and n2>0:
    while n1 <= n2:
        if n1%2==1:
            soma=soma+n1
            print(n1)
        n1+=1
    print(f'A soma dos impares {soma}')
else:
    print('Esse valor é negativo!!!')'''

''' 5.	Faça um script que mostre uma sequência numérica iniciando em 63, terminado em 129, calcule e mostre a soma destes valores.
a=63
b=129
soma=0
while a<=b:
    soma=soma+a
    a=a+1
print(f'A soma desses valores {soma}')'''
