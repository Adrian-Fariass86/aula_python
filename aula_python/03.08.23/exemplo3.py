#Leia 2 valores e mostre a soma do intervalo entre eles
num1 = int(input('digite o valor incial:'))
num2 = int(input('digite o valor final:'))
soma = 0
if num1 < num2:
    while num1<=num2:
        print(num1, end="+")
        soma+=num1
        num1+=1 
    print("\n O resultado é:",soma)  
elif num2 < num1:
    while num2<=num1:
        print(num2, end="+")
        soma+=num2
        num2+=1
    print("\n O resultado é:",soma)
else:
    print('Os valores são iguais...')