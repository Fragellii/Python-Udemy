"""
Seção 3 - Exercício 7

Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7 * altura) - 58
"""
#entrada
altura = float(input("Informe sua altura "))
#processamento
peso_ideal = (72.7 * altura) - 58
#saída
print("O seu peso ideal é {0:.1f}" .format(peso_ideal))