# 1. Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('Insira o primeiro número: ')) # pede a informação para o usuário
num2 = float(input('Insira o segundo número: '))

if num1 > num2: # se a esta condição for verdadeira
    print(f'O maior número é o {num1:.0f}')
elif num2 > num1: # elif --> um segunda condição imposta ao programa (independente da primeira)
    print(f'O maior número é o {num2:.0f}')
else: # caso nenhuma das condições acima seja verdadeira
    print('Os números são iguais')