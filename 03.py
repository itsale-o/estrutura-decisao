# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M" Conforme a letra escrever:
# F - Feminino, M - Masculino, Inválido.

genero = input('Informe seu gênero utilizando F ou M: ') # pede a informação para o usuário

if genero == 'F' or genero == 'f': # condição 1
    print('Feminino')
elif genero == 'M' or genero == 'm': # condição 2
    print('Masculino')
else: # caso nenhuma das condições seja verdadeira
    print('Entrada inválida')