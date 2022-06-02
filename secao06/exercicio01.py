"""
Seção 6 - Exercício 01

Ler uma variável numérica n e imprimi-la somente se a mesma for maior que 100, caso contrário imprimí-la
com o valor zero
"""
#entrada
n = int(input("Informe um número: "))
#processamento
if n > 100:
    print(n)
else:
    n = 0
    print(n)