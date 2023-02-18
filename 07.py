# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input('Primeiro número: ')) # pede as informações para o usuário
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))

if num1 > num2 and num1 > num3: # caso as duas condições sejam verdadeiras ao mesmo tempo (and)
    if num2 > num3: # uma outra condição imposta caso a condição aacima seja verdadeira (if dentro de if)
        print(f'O maior número é: {num1:.0f}\nO menor número é: {num3:.0f}')
    else:
        print(f'O maior número é: {num1:.0f}\nO menor número é: {num2:.0f}')
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f'O maior número é: {num2:.0f}\nO menor número é: {num3:.0f}')
    else:
        print(f'O maior número é: {num2:.0f}\nO menor número é: {num1:.0f}')
if num3 > num1 and num3 > num2:
    if num1 > num2:
        print(f'O maior número é: {num3:.0f}\nO menor número é: {num2:.0f}')
    else:
        print(f'O maior número é: {num3:.0f}\nO menor número é: {num1:.0f}')