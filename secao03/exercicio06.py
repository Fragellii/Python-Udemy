"""
Seção 3 - Exercício 6

Faça um algoritmo que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

#entrada
valor_por_hora = float(input("Qual valor você ganha por hora? "))
horas_trabalhadas = int(input("Quantas horas você trabalhou neste mês? "))
#processamento
salario = horas_trabalhadas * valor_por_hora
#saída
print("Neste mês você vai receber R$ {0:.2f}" .format(salario))