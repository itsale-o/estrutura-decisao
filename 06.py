# 6. Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input('Primeiro número: ')) # pede as informações para o usuário
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))

if num1 > num2 and num1 > num3: # caso as duas condições impostas sejam verdadeiras ao mesmo tempo (and)
    print(f'O maior número é o: {num1:.0f}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é o: {num2:.0f}')
elif num3 > num1 and num3 > num2:
    print(f'O maior número é o: {num3:.0f}')