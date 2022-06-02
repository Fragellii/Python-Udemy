"""
Ler um número e verificar se ele é par ou impar. Quando for par armazenar esse valor em 'p' e quando for
impar armazenar em 'i'.
"""
#variáveis
p = 0
i = 0
#entrada
numero = int(input("Informe um número: "))
#processamento
if numero % 2 == 0:
    p = numero
else:
    i = numero
print(p)
print(i)