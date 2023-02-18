# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Informe o preço do primeiro produto: R$ ')) # pede as informações para o usuário
produto2 = float(input('Informe o preço do segundo produto: R$ '))
produto3 = float(input('Informe o preço do terceiro produto: R$ '))

if produto1 < produto2 and produto1 < produto3: # caso as duas condições sejam verdadeiras ao mesmo tempo (and)
    print(f'Deve-se comprar o primeiro produto.\nValor: R$ {produto1:.2f}')
elif produto2 < produto1 and produto2 < produto3:
    print(f'Deve-se comprar o segundo produto.\nValor: R$ {produto2:.2f}')
elif produto3 < produto1 and produto3 < produto2:
    print(f'Deve-se comprar o terceiro produto.\nValor: R$ {produto3:.2f}')