def anagrama():
    palavra1 = list(input('Digite a primeira palavra: '))
    palavra2 = list(input('Digite a segunda palavra: '))

    tamanho = len(palavra2)

    for letra in palavra1:
        for pos in range(len(palavra2)):
            if letra == palavra2[pos]:
                palavra2[pos] = ''
                tamanho-=1

    if tamanho==0:
        return print('As palavras sao anagramas')
    else:
        return print('As palavras nao sao anagramas')

anagrama()