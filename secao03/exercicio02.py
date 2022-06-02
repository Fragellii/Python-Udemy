"""
Seção 3 - Exercício 2

Faça um algoritmo para "calcular o estoque médio de uma peça",
sendo que:

estoque_medio = (quantidade_minima + quantidade_maxima) / 2
"""

#entrada
quantidade_minima = int(input("Informe a quantidade mínima: "))
quantidade_maxima = int(input("Informe a quantidade máxima: "))

#processamento
estoque_medio = (quantidade_minima + quantidade_maxima) / 2

#saída
input("O estoque médio é de: {}" .format(estoque_medio))