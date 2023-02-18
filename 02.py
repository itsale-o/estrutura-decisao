# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input('Insira um número: ')) # pede a informação para o usuário

if valor > 0: # caso esta condição seja verdadeira
    print(f'{valor:.0f} é um número positivo')
elif valor < 0: # elif --> outra condição independente da primeria
    print(f'{valor:.0f} é um número negativo')
else: # caso as outras condições não sejam verdadeiras
    print('O número informado é o número zero')