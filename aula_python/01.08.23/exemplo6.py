# Leia dois numeros inteiros e mostre somente o menor valor
print("Informe numeros inteiros\n")
print("-"*50)
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
if n1<n2:
    print(f"o numero {n1} é o menor!!")
# elif n1==n2:
    # print("Você digitou valores iguais!!")
elif n1>n2:
    print(f"O numero {n2} é o menor!!")
else:
   print("Você digitou valores iguais!!") 
