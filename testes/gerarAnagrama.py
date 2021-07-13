import random

def gerarAnagrama():
    '''Esta funcao gera um anagrama para uma palavra passada por input'''
    palavra = input('Digite uma palavra: ')
    lista = list(palavra)

    i=0
    saida = ''

    # a quantidade de vezes que o laco se repete eh um valor arbitrario
    # len(lista)*5 foi escolhido por nao ser um valor muito alto, mas tambem nao muito pequeno
    
    while (i<len(lista)*5):
        # aqui sao definidas as posicoes dos elementos a serem permutados
        primeiro = random.randrange(0,len(lista))
        segundo = random.randrange(0, len(lista))
        lista[primeiro], lista[segundo] = lista[segundo], lista[primeiro]
        i+=1

    for letra in lista:
        # construcao da string de saida
        saida += letra
    
    return print('Um dos anagramas de %s eh %s' %(palavra, saida))

gerarAnagrama()