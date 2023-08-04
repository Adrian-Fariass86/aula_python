# valor1 = 45
# valor2 = 258.45
# operadores aritiméticos

# print(f"Soma: {valor1} + {valor2} = ", valor1 + valor2)
# print(f"Subtracao: {valor1} - {valor2} = ", valor1 - valor2)
# print(f"Multiplicao: {valor1} x {valor2} = ", valor1 * valor2)
# divisão com duas casas decimais usa a expressão :.2f
# print(f"Divisao: {valor1} : {valor2} = {valor1 / valor2:.2f}")
# obter dados do teclado (entrada de dados)
usuario = input("digite seu nome: ")
print(f"Seja Bem Vindo, {usuario}")
idade = input("digite sua idade:")
print(f"O nome do usuario {usuario} e sua idade atual e {idade}")
# print(f"O dobro da idade e: {idade*2}")
# print ("usuario: ",type(usuario))
# print ("idade: ",type(idade))
valor_curso = float(input("informe o valor pago pelo curso: "))
print(f"O valor do curso informado R$: {valor_curso:.2f}")
# valor uma msg com 25% do curso
# Parabens!! vc ganhou <valor> de créditos na proxima compra
valor_desconto = valor_curso*(25/100)
print(f"Parabens!! vc ganhou R$ {valor_desconto} de creditos na proxima compra")
#Solicitar quantidade de parcelas do pagamento
qtd_parcela = int(input("Digite a quantidade de parcelas para fazer o pagamento:"))
valor_parcela = valor_curso/qtd_parcela
#mostrar valor das parcelas sem juros
print(f"valor das parcelas sem juros: R${valor_parcela:.2f}")