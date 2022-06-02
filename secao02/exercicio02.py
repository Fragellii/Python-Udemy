""" Seção 2 - Exercício 2
Faça um algoritmo para somar dois números e multiplicar o resultado
pelo primeiro número """

#entrada
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

#processamento
soma = num1 + num2
multiplicacao = soma * num1

#saída
print("o resultado da multiplicação é {0}".format(multiplicacao))