"""
Seção 6 - Exercício 02

Elabore um algoritimo que leia um número. Se positivo armazene-o em 'a',
se for negativo, em 'b'. No final mostrar o resultado
"""
#entrada
n = int(input("Informe um valor: "))
#processamento
if n > 0:
    a = n
    print("O valor é positivo")
else:
    b = n
    print("O valor é negativo")
print(n)
