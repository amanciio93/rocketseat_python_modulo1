# OPERAÇÕES ARITMETICAS:

#SOMA
soma = 1 + 1
print("SOMA DE 1 + 1 = ", soma, type(soma))

#SUBTRAÇÃO
subtracao = 2 - 1
print("SUBTRAÇÃO DE 2 - 1 = ", subtracao, type(subtracao))

#MULTIPLICAÇÃO
multiplicacao = 3 * 3
print("MULTIPLICAÇÃO DE 3 X 3 = ", multiplicacao, type(multiplicacao))

#DIVISÃO
divisao = 10 / 5
print("DIVISÃO DE 10 / 5 = ", divisao, type(divisao))

""" 
    A divisão sempre retorna um valor FLOAT, se for necessário, podemos 
    converte- lo usando a função int() ou realizar a divisão com
    '//' ( duas barras) ou para fazer o inverso float()
"""
print("CONVERTENDO O TIPO DE DIVISÃO: ", int(divisao), type(int(divisao)))
print("CONVERTENDO O TIPO DE SOMA: ", float(soma), type(float(soma)))

#MODULO
modulo = 5 % 2
print("MODULO DE 5 / 2 = ", modulo, type(modulo))