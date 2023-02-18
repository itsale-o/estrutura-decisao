# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
# V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
# "Valor Inválido!", conforme o caso.

periodo = input('Informe qual período você estuda: ') # pede a informação para o usuário

if periodo == 'M' or periodo == 'm': # acontece caso uma das condições seja verdadeira (or)
    print('Bom Dia!')
elif periodo == 'V' or periodo == 'v':
    print('Boa Tarde!')
elif periodo == 'N' or periodo == 'n':
    print('Boa Noite!')
else:
    print('Entrada Inválida!')