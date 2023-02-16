#!/usr/bin/env python
# coding: utf-8

# # Estruturas de decisão

# #### 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# 
# 
# Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes;

# In[ ]:


lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))

if ((lado1 + lado2) > lado3) or ((lado1 + lado3) > lado2) or ((lado2 + lado3) > lado1):
    if lado1 == lado2 == lado3:
        print('É um triângulo equilátero')
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print('É um triângulo isósceles')
    else:
        print('É um triângulo escaleno')
else:
    print('Não é um triângulo')


# #### 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma $ax² + bx + c$. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# 
# - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

# In[ ]:


import math
a = float(input('a = '))

if a == 0:
    print('a = 0 não retorna uma equação do segundo grau')
else:
    b = float(input('b = '))
    c = float(input('c = '))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print(f'▲ negativo --> Portanto esta equação não possui raízes reais como solução')
    elif delta == 0:
        x = -b / (2 * a)
        print(f'▲ = 0 --> Portanto esta equação possui apenas uma raíz: x = {x:.0f}')
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Esta equação possui duas raízes:\nx_1 = {x1:.0f}\nx_2 = {x2:.0f}')


# #### 17. Você está construindo um calendário para controlar dias de trabalho a pedido do RH. Nessa construção, você vai precisar definir quais anos são bissextos e quais não são, para montar o calendário de forma correta. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
# <pre>
# Dica para determinar se um ano é bissexto: 
# - São bissextos todos os anos múltiplos de 400, p.ex.: 1600, 2000, 2400, 2800...
# - São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, 
# p.ex.: 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028...
# - Não são bissextos todos os demais anos.<br>
# ex1: 2004 é múltiplo de 4, mas não é múltiplo de 100, então é bissexto.
# ex2: 2000 é múltiplo de 4, mas é múltiplo de 100, só que também é multiplo de 400, então é bissexto (porque todo ano múltiplo de 400 é bissexto, independente do resto).
# ex3: 1900 é múltiplo de 4, é múltiplo de 100, mas não é múltiplo de 400, então não é bissexto
# 
# </pre>
# 
# Dica: lembre que: numero % 4 é o resto da divisão do número por 4, ex: 10 % 3 = 1 (já que 10/3 = 3 e resta 1)

# In[ ]:


ano = float(input('Ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano:.0f} é um ano bissexto')
else:
    print(f'{ano:.0f} não é um ano bissexto')


# #### 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# In[ ]:


data = (input("Data: "))

if int(data[0:2]) != 0  and int(data[0:2]) <= 31 :
    if int(data[3:5]) != 0  and int(data[3:5]) <= 12 :
        if int(data[6:11]) != 0 :
            print("Data Válida")
        else :
            print("Data Inválida")
    else :
        print("Data Inválida")
else:
    print("Data Inválida")


# #### 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# 
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 
# - 326 = 3 centenas, 2 dezenas e 6 unidades
# - 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

# In[ ]:


num = float(input('Informe um número entre 1 e 999: '))
centena = num // 100
dezena = (num % 100) // 10
unidade = (num % 100) % 10

if centena == 0:
    if dezena == 0:
        print(f'{unidade:.0f} unidades')
    elif unidade == 0:
        print(f'{dezena:.0f} dezenas')
    else:
        print(f'{dezena:.0f} dezenas e {unidade:.0f} unidades')
elif dezena == 0:
    if unidade == 0:
        print(f'{centena:.0f} centenas')
    else:
        print(f'{centena:.0f} centenas e {unidade:.0f} unidades')
elif unidade == 0:
    if centena == 0:
        print(f'{dezena:.0f} dezenas')
    else:
        print(f'{centena:.0f} centenas e {dezena:.0f} dezenas')
else:
    print(f'{centena:.0f} centenas, {dezena:.0f} dezenas e {unidade:.0f} unidades')


# #### 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# <pre>
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.
# </pre>

# In[ ]:


nota1 = float(input('Primeira nota parcial: '))
nota2 = float(input('Segunda nota parcial: '))
nota3 = float(input('Terceira nota parcial: '))
media = (nota1 + nota2 + nota3) / 3

if media == 10:
    print(f'Média: {media:.1f}\nAprovado com Distinção')
elif media >= 7:
    print(f'Média: {media:.1f}\nAprovado')
else:
    print(f'Média: {media:.1f}\nReprovado')


# #### 21. Faça um Programa para um caixa eletrônico. 
# 
# O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# - Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# - Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

# In[ ]:


valor_saque = float(input('Valor do saque: R$ '))
notas100 = 0
notas50 = 0
notas10 = 0
notas5 = 0
notas1 = 0

if 10 <= valor_saque <= 600:
    print('Serão necessárias: ')
    if valor_saque >= 100:
        notas100 = valor_saque // 100
        print(f'{notas100:.0f} notas de R$100')
    if valor_saque % 100 >= 50:
        notas50 = (valor_saque - (100 * notas100)) // 50
        print(f'{notas50:.0f} notas de R$50')
    if valor_saque % 50 >= 10:
        notas10 = (valor_saque - (100 * notas100) - (50 * notas50)) // 10
        print(f'{notas10:.0f} notas de R$10')
    if valor_saque % 10 >= 5:
        notas5 = (valor_saque - (100 * notas100) - (50 * notas50) - (10 * notas10)) // 5
        print(f'{notas5:.0f} notas de R$5')
    if valor_saque % 5 >= 1:
        notas1 = (valor_saque - (100 * notas100 )- (50 * notas50)- (10 * notas10) - (5 * notas5))
        print(f'{notas1:.0f} notas de R$1')
else:
    print('Valor indisponível. O valor disponível para saque é entre R$ 10,00 e R$ 600,00')


# #### 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# 
# Dica: utilize o operador módulo (resto da divisão).

# In[ ]:


num = int(input('Informe um número inteiro: '))

if num % 2 == 0:
    print(f'{num:.0f} é um número par')
else:
    print(f'{num:.0f} é um número ímpar')


# #### 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# 
# Dica: utilize uma função de arredondamento.

# In[ ]:


numero = float(input('Digite um número: '))

if numero % 1 == 0:
    print(f'{numero:.0f} é um número inteiro')
else:
    print(f'{numero} é um número decimal')


# #### 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# - par ou ímpar;
# - positivo ou negativo;
# - inteiro ou decimal.

# In[ ]:


num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
op = input('Informe qual operação deseja fazer com estes dois números (+, -, *, / ou **): ')

if op == '+':
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado:.1f}')
if op == '-':
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado:.1f}')
if op == '*':
    resultado = num1 * num2
    print(f'{num1} x {num2} = {resultado:.1f}')
if op == '/':
    resultado = num1 / num2
    print(f'{num1} / {num2} = {resultado:.1f}')
if op == '**':
    resultado = num1 ** num2
    print(f'{num1} ^ {num2} = {resultado:.1f}')
    
if resultado % 2 == 0:
    print('O resultado é um número par')
else:
    print('O resultado é um número ímpar')

if resultado > 0:
    print('O resultado é positivo')
elif resultado == 0:
    print('O resultado é zero')
else:
    print('O resultado é negativo')

if resultado % 1 == 0:
    print('O resultado é um número inteiro')
else:
    print('O resultado é um número decimal')


# #### 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# 
# - "Telefonou para a vítima?"
# - "Esteve no local do crime?"
# - "Mora perto da vítima?"
# - "Devia para a vítima?"
# - "Já trabalhou com a vítima?"
# 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# In[ ]:


sim = 0
p1 = input('Telefonou para a vímtima? ')
p2 = input('Esteve no local do crime? ')
p3 = input('Mora perto da vítima? ')
p4 = input('Devia para a vítima? ')
p5 = input('Já trabalhou com a vítima? ')

if p1 == 'sim':
    sim += 1
if p2 == 'sim':
    sim += 1
if p3 == 'sim':
    sim += 1
if p4 == 'sim':
    sim += 1
if p5 == 'sim':
    sim += 1

if sim == 2:
    print('Suspeito(a)')
elif 3 <= sim <= 4:
    print('Cúmplice')
elif sim == 5:
    print('Assassino(a)')
else:
    print('Inocente')


# #### 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# <pre>
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro
# </pre>
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R\\$ 2,50 o preço do litro do álcool é R$ 1,90.
# 

# In[ ]:


tipo = input('Tipo de combustível: ')
litros = float(input('Quantidade: '))
preco_g = 2.5

if tipo == 'A':
    if litros <= 20:
        preco_a = 1.9 - (0.03 * 1.9)
        total = litros * preco_a
        print(f'Total a pagar: R$ {total:.2f}')
    else:
        preco_a = 1.9 - (0.05 * 1.9)
        total = litros * preco_a
        print(f'Total a pagar: R$ {total:.2f}')
if tipo == 'G':
    if litros <= 20:
        preco_g = 2.5 - (0.04 * 2.5)
        total = litros * preco_g
        print(f'Total a pagar: R$ {total:.2f}')
    else:
        preco_g = 2.5 - (0.06 * 2.5)
        total = litros * preco_g
        print(f'Total a pagar: R$ {total:.2f}')
    


# #### 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# <pre>
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# </pre>
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
# 

# In[ ]:


morango = float(input('Informe a quantidade de morangos: '))
maca = float(input('Informe a quantidade de maçãs: '))

if morango <= 5:
    preco_morango = 2.5 * morango
else:
    preco_morango = 2.2 * morango
if maca <= 5:
    preco_maca = 1.8 * maca
else:
    preco_maca = 1.5 * maca
    
total = preco_morango + preco_maca
if (morango + maca > 8) or (total > 25):
    total_com_desconto = total - (0.1 * total)
    print(f'Total a pagar: R$ {total_com_desconto:.2f}')
else:
    print(f'Total a pagar: R$ {total:.2f}')


# #### 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
# <pre>
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# </pre>
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
# 

# In[ ]:


tipo = input('Informe o corte da carne: ')
qtde = float(input('Informe a quantidade de carne: '))
pagamento = input('Informe o método de pagamento: Dinheiro - D, Cartão Tabajara - T, Cartão - C: ')

if tipo == 'Filé Duplo':
    if qtde <= 5:
        preco = 4.9 * qtde
    else:
        preco = 5.8 * qtde
if tipo == 'Alcatra':
    if qtde <= 5:
        preco = 5.9 * qtde
    else:
        preco = 6.8 * qtde
if tipo == 'Picanha':
    if qtde <= 5:
        preco = 6.9 * qtde
    else:
        preco = 7.8 * qtde
if pagamento == 'T':
    desconto = 0.05 * preco
    preco = preco - desconto
else:
    desconto = 0
    preco = preco
    
print('---CUPOM FISCAL---')
print(f'Corte da carne: {tipo}')
print(f'Quantidade: {qtde:.0f} kg ')
print(f'Desconto: R$ {desconto:.2f}')
print(f'Total a pagar: R$ {preco:.2f}')

