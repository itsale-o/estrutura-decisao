#!/usr/bin/env python
# coding: utf-8

# # Estruturas de decisão

# #### 1. Faça um Programa que peça dois números e imprima o maior deles.

# In[ ]:


num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

if num1 > num2:
    print(f'O maior número é o {num1:.0f}')
elif num2 > num1:
    print(f'O maior número é o {num2:.0f}')
else:
    print('Os números são iguais')


# #### 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# In[ ]:


valor = float(input('Insira um número: '))

if valor > 0:
    print(f'{valor:.0f} é um número positivo')
elif valor < 0:
    print(f'{valor:.0f} é um número negativo')
else: 
    print('O número informado é o número zero')


# #### 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Inválido.

# In[ ]:


genero = input('Informe seu gênero utilizando F ou M: ')

if genero == 'F' or genero == 'f':
    print('Feminino')
elif genero == 'M' or genero == 'm':
    print('Masculino')
else:
    print('Entrada inválida')


# #### 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# In[ ]:


vogais = 'A, a, E, e, I, i, O, o, U u'
letra = input('Digite uma letra: ')

if letra in vogais:
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consoante')


# #### 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# 
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.

# In[ ]:


nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2

if 7 <= media < 10:
    print(f'Média: {media:.1f} - Aprovado')
elif media == 10:
    print(f'Média: {media:.1f} - Aprovado com Distinção')
else:
    print(f'Média: {media:.1f} - Reprovado')


# #### 6. Faça um Programa que leia três números e mostre o maior deles.

# In[ ]:


num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))

if num1 > num2 and num1 > num3:
    print(f'O maior número é o: {num1:.0f}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é o: {num2:.0f}')
elif num3 > num1 and num3 > num2:
    print(f'O maior número é o: {num3:.0f}')


# #### 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

# In[ ]:


num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))

if num1 > num2 and num1 > num3:
    if num2 > num3:
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


# #### 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

# In[ ]:


produto1 = float(input('Informe o preço do primeiro produto: R$ '))
produto2 = float(input('Informe o preço do segundo produto: R$ '))
produto3 = float(input('Informe o preço do terceiro produto: R$ '))

if produto1 < produto2 and produto1 < produto3:
    print(f'Deve-se comprar o primeiro produto.\nValor: R$ {produto1:.2f}')
elif produto2 < produto1 and produto2 < produto3:
    print(f'Deve-se comprar o segundo produto.\nValor: R$ {produto2:.2f}')
elif produto3 < produto1 and produto3 < produto2:
    print(f'Deve-se comprar o terceiro produto.\nValor: R$ {produto3:.2f}')


# #### 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

# In[ ]:


num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo número: '))
num3 = float(input('Terceiro número: '))

if num1 > num2 and num1 > num3:
    if num2 > num3:
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


# #### 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# In[ ]:


periodo = input('Informe qual período você estuda: ')

if periodo == 'M' or periodo == 'm':
    print('Bom Dia!')
elif periodo == 'V' or periodo == 'v':
    print('Boa Tarde!')
elif periodo == 'N' or periodo == 'n':
    print('Boa Noite!')
else:
    print('Entrada Inválida!')


# #### 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# 
# ##### salários até R\\$ 280,00 (incluindo) : aumento de 20% 
# 
# ##### salários entre R\\$ 280,00 e R\\$ 700,00 : aumento de 15% 
# 
# ##### salários entre R\\$ 700,00 e R\\$ 1500,00 : aumento de 10% 
# 
# ##### salários de R\\$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela: 
# 
# ###### o salário antes do reajuste;
# 
# ###### o percentual de aumento aplicado;
# 
# ###### o valor do aumento;
# 
# ###### o novo salário, após o aumento.

# In[ ]:


salario = float(input('Informe seu salário: '))

if salario <= 280:
    percentual_aumento = 0.2
elif 280 < salario <= 700:
    percentual_aumento = 0.15
elif 700 < salario <= 1500:
    percentual_aumento = 0.1
else:
    percentual_aumento = 0.05
aumento = (percentual_aumento * salario)
novo_salario = salario + aumento
print(f'Salário anterior: R$ {salario:.2f}\nPercentual de aumento aplicado: {percentual_aumento * 100:.0f}%\nValor do aumento: R$ {aumento:.2f}\nNovo valor para o salário: R$ {novo_salario:.2f}')


# #### 12 . Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# 
# Desconto do IR:<br>
# Salário Bruto até 900 (inclusive) - isento<br>
# Salário Bruto até 1500 (inclusive) - desconto de 5%<br>
# Salário Bruto até 2500 (inclusive) - desconto de 10%<br>
# Salário Bruto acima de 2500 - desconto de 20%<br>
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
# 
# Salário Bruto: (5 * 220)        : R\\$ 1100,00<br>
# (-) IR (5%)                     : R\\$   55,00<br>
# (-) INSS ( 10%)                 : R\\$  110,00<br>
# FGTS (11%)                      : R\\$  121,00<br>
# Total de descontos              : R\\$  165,00<br>
# Salário Liquido                 : R\\$  935,00<br>

# In[ ]:


valor_hora = float(input('Valor recebido por hora trabalhada: R$ '))
horas = float(input('Horas trabalhadas no referido mês: '))
salario_bruto = valor_hora * horas

if salario_bruto <= 900:
    porcentagem_ir = 0
elif 900 < salario_bruto <= 1500:
    porcentagem_ir = 0.05
elif 1500 < salario_bruto <= 2500:
    porcentagem_ir = 0.1
else:
    porcentagem_ir = 0.2
ir = salario_bruto * porcentagem_ir
inss = 0.1 * salario_bruto
fgts = 0.11 * salario_bruto
descontos = ir + inss
salario_liquido = salario_bruto - descontos

print(f'Salário Bruto ({valor_hora:.2f} x {horas:.0f}): R$ {salario_bruto}\n(-) IR ({porcentagem_ir * 100:.0f}%): R$ {ir:.2f}\n(-) INSS (10%): R$ {inss:.2f}\nFGTS (11%): R$ {fgts:.2f}\nTotal de Descontos: R$ {descontos:.2f}\nSalário Líquido: R$ {salario_liquido:.2f}')


# #### 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

# In[ ]:


dia = float(input('Digite um número correspondente a um dia da semana: '))

if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda-Feira')
elif dia == 3:
    print('Terça-Feira')
elif dia == 4:
    print('Quarta-Feira')
elif dia == 5:
    print('Quinta-Feira')
elif dia == 6:
    print('Sexta-Feira')
elif dia == 7:
    print('Sábado')
else:
    print('Entrada Inválida')


# #### 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. Em seguida, mostre qual conceito o aluno teve. A atribuição de conceitos obedece à tabela abaixo:
# <pre>
# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0        A
# Entre 7.5 e 9.0         B
# Entre 6.0 e 7.5         C
# Entre 4.0 e 6.0         D
# Entre 4.0 e zero        E
# </pre>

# In[ ]:


nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print(f'Média: {media:.1f}')

if 9 <= media <= 10:
    print('Conceito - A')
elif 7.5 <= media < 9:
    print('Conceito - B')
elif 6 <= media < 7.5:
    print('Conceito - C')
elif 4 <= media < 6:
    print('Conceito - D')
else:
    print('Conceito - E')

