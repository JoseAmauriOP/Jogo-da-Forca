import random as rd
palavra = ['melao','mamao', 'amora', 'limao','manga','uvaia','cabel','cacau', 'caqui', 'cidra']
palavra_escolhida = rd.choice(palavra)

print('Olá, vamo jogar um jogo da forca')
print('2 dicas é uma fruta e a palavra possui 5 letras')
letras_palavra = ['-', '-', '-', '-', '-']
print(''.join(letras_palavra))
print('Vamos lá, você tem 6 tentativas se você acertar a letra você ganha a opção de chute, a cada tentativa errada você será informado, se você utilizar das suas 6 tentativas e não acertar você ganha orpotunidade de chutar tambem.')
for i in range(6):
    i += 1
    letra = input('Digite uma letra para sua {}º tentativa:'.format(i))
    letra =letra.lower()
    if letra in palavra_escolhida:
        for index, char in enumerate(palavra_escolhida):
            if char == letra: 
                letras_palavra[index] = letra
        if ''.join(letras_palavra) == palavra_escolhida:
            print ('Você acertou a palavra!! fim do game')
            break
        else:
            pass
        print(''.join(letras_palavra))
        print('Parabéns você acertou uma letra')
        opc = input('Digite S de sim para chutar ou digite N de não para ir para proxima tentativa:')
        while opc != 'S' and opc != 'N': 
            print('opção invalida:')
            opc = input('Digite S de sim para chutar ou digite N de não para ir para proxima tentativa:')
            opc =opc.upper()
        if opc == 'S':
            chute = input('Sabe a palavra, vamos lá diga:')
            if chute == palavra_escolhida:
                print('Parabéns você acertou, a palavra era {} e voce acertou na {}º tentativa, incrivel'.format(palavra_escolhida, i))
                break
            else:
                print('Você errou, vamos para a proxima')
        elif opc == 'N':
            if i < 6:
                print('Certo então vamos para a proxima tentativa')
            else:
                 pass
        else:
            pass
    elif i == 6:
        print('Suas tentativas acabaram, mas você tem um chute ainda pra fazer')
        chute = input('Sabe a palavra, vamos lá diga:')
        if chute == palavra_escolhida:
            print('Parabéns você acertou, a palavra era {} e voce acertou na {}º tentativa, incrivel'.format(palavra_escolhida, i))
            break
        else:
            print('Infelizmente você não conseguiu, a palavra era {}'.format(palavra_escolhida))
            break
    else:
        print('Voce errou, vamos para a proxima')


    
