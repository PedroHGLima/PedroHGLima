import random

def recorrencias(elemento,lista):
    '''Funcao que conta as recorrencias de um valor em uma lista'''
    recorrencia=0
    for n in range(len(lista)):
        if lista[n]==elemento:
            recorrencia=recorrencia+1
    return recorrencia

def bombasmedio(n=10):
    listabombas=[]

    for i in range(n):
        # calcula a posicao da bomba, e a adiciona na lista
        posicaolinha=random.randint(1,6)
        posicaocoluna=random.randint(1,6)
        bomba=[posicaolinha,posicaocoluna]
        listabombas+=[bomba]

        # verificando se nao eh a primeira execucao
        if len(listabombas)<2:
            continue

        # verifica se a bomba ja existe na lista
        while recorrencias(bomba,listabombas)!=1:
            # calculando a nova posicao da bomba
            posicaolinha=random.randint(1,6)
            posicaocoluna=random.randint(1,6)

            # inserindo a nova posicao da bomba
            bomba=[posicaolinha,posicaocoluna]
            listabombas[i]=bomba

    return listabombas

print(bombasmedio(10))