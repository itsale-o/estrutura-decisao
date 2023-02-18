# 4. Faça um Programa que verifique se uma letra digitada é vogal ou
# consoante.

vogais = 'A, a, E, e, I, i, O, o, U, u' # aqui definimos quais serão nossas vogais.
letra = input('Digite uma letra: ') # pede a informação para usuário

if letra in vogais: # se a letra informada estiver contida (in) na variável 'vogais'
    print(f'{letra} é uma vogal')
else: # caso a condição acima não seja verdade
    print(f'{letra} é uma consoante')