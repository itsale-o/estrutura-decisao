# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular
# a média alcançada por aluno e apresentar:
#- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#- A mensagem "Reprovado", se a média for menor do que sete;
#- A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Nota 1: ')) # pede as notas do aluno
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2 # faz o cálculo da média

if 7 <= media < 10: # condição para que o aluno seja aprovado
    print(f'Média: {media:.1f} - Aprovado')
elif media == 10: # uma segunda condição caso o aluno seja aprovado com distinção
    print(f'Média: {media:.1f} - Aprovado com Distinção')
else: # caso nenhuma das condições acima seja verdadeira, ou seja, caso o aluno seja reprovado
    print(f'Média: {media:.1f} - Reprovado')