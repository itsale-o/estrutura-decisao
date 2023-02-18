# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input('Primeiro número: ')) # pede as informações para o usuário
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))

if num1 > num2 and num1 > num3: # acontece caso as duas condições ejam verdaeiras ao mesmo tempo (and)
    if num2 > num3: # uma condição para caso a condição acima seja verdadeira
        print(f'{num1:.0f}, {num2:.0f}, {num3:.0f}')
    else:
        print(f'{num1:.0f}, {num3:.0f}, {num2:0f}')
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f'{num2:.0f}, {num1:.0f}, {num3:.0f}')
    else:
        print(f'{num2:.0f}, {num3:.0f}, {num1:.0f}')
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print(f'{num3:.0f}, {num1:.0f}, {num2:.0f}')
    else:
        print(f'{num3:.0f}, {num2:.0f}, {num1:.0f}')