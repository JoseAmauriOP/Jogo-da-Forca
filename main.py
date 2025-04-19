import random as rd
palavra = ['melao','mamao', 'amora', 'limao']
palavra_escolhida = rd.choice(palavra)
print(palavra_escolhida)
print('Olá, vamo jogar um jogo da forca')
print('2 dicas é uma fruta e a palavra possui 5 letras')
letra = input('Digite uma letra para sua primeira tentativa:')
letra.lower()
letras_palavra = '- - - - -'
letras_palavra.split(' ')
print(letras_palavra)
i = palavra_escolhida.index(letra)
print(i)

letras_palavra[i] = letra
print(letras_palavra)

    
