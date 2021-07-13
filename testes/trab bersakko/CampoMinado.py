import random
import numpy as np    

def recorrencias(elemento,lista):
    '''Funcao que conta as recorrencias de um valor em uma lista'''
    recorrencia=0
    for n in range(len(lista)):
        if lista[n]==elemento:
            recorrencia=recorrencia+1
    return recorrencia

def geradordebombas(numerodebombas,ordemMatriz):
    '''Funcao que gera a posicao das bombas aleatoriamente com base no numero de bombas solicitadas e a ordem da matriz designada'''
    listabombas=[]

    for i in range(numerodebombas):
        # calcula a posicao da bomba, e a adiciona na lista
        posicaolinha=random.randint(1,ordemMatriz)
        posicaocoluna=random.randint(1,ordemMatriz)
        bomba=[posicaolinha,posicaocoluna]
        listabombas+=[bomba]

        # verificando se nao eh a primeira execucao
        if len(listabombas)<2:
            continue

        # verifica se a bomba ja existe na lista
        while recorrencias(bomba,listabombas)!=1:
            # calculando a nova posicao da bomba
            posicaolinha=random.randint(1,ordemMatriz)
            posicaocoluna=random.randint(1,ordemMatriz)

            # inserindo a nova posicao da bomba
            bomba=[posicaolinha,posicaocoluna]
            listabombas[i]=bomba
    return listabombas

def posicaoescolhida(ordemMatriz):
    '''Funcao que pede a posicao, recebe a ordem da matriz como argumento para delimitar os limites da posicao pedida'''
    #laco para verificar que os valores recebidos para a posicao na linha e na coluna sao validos
    while True:
        print('Digite um numero inteiro dentro dos limites do campo minado')

        posicaoEscolhidaX=input('Digite uma linha: ')

        # condicional para verifiar se o jogodar quer sair do jogo em andamento
        if posicaoEscolhidaX=='sair':
            return 'sair','sair'
        #try para verificar que os valores recebidos para a posicao na coluna sao validos    
        try:
            posicaoEscolhidaX=int(posicaoEscolhidaX)
            if posicaoEscolhidaX>ordemMatriz or posicaoEscolhidaX<1:
                raise ValueError
        except ValueError:
            print('Digite um valor valido')       
        else:
            posicaoEscolhidaY=input('Digite uma coluna: ')

            # condicional para verifiar se o jogodar quer sair do jogo em andamento
            if posicaoEscolhidaY=='sair':
                return 'sair','sair'
            #try para verificar que os valores recebidos para a posicao na linha e na coluna sao validos    
            try:        
                posicaoEscolhidaY=int(posicaoEscolhidaY)
                if posicaoEscolhidaY>ordemMatriz or posicaoEscolhidaY<1:
                    raise ValueError
            except ValueError:
                print('Digite um valor valido')
            else:
                return posicaoEscolhidaX,posicaoEscolhidaY
  
            
def contadordebombas(listabombas, posicaoEscolhidaX, posicaoEscolhidaY):
    '''Funcao que conta a quantidade de bombas no entorno de uma posicao'''

    #variavel contador, que contabiliza as bombas no entorno de cada posicao
    contador=0

    #laco para percorrer a lista com as posicoes da linha e da coluna de cada bomba, e compara com a posicao pedida no input
    for i in range(len(listabombas)):
        if posicaoEscolhidaX+1==listabombas[i][0] and posicaoEscolhidaY==listabombas[i][1]:
            contador=contador+1
        elif posicaoEscolhidaX+1==listabombas[i][0] and posicaoEscolhidaY+1==listabombas[i][1]:
            contador=contador+1
        elif posicaoEscolhidaX+1==listabombas[i][0] and posicaoEscolhidaY-1==listabombas[i][1]:
            contador=contador+1
        elif posicaoEscolhidaX==listabombas[i][0] and posicaoEscolhidaY+1==listabombas[i][1]:
            contador=contador+1
        elif posicaoEscolhidaX==listabombas[i][0] and posicaoEscolhidaY-1==listabombas[i][1]:
            contador=contador+1
        elif posicaoEscolhidaX-1==listabombas[i][0] and posicaoEscolhidaY==listabombas[i][1]:
            contador=contador+1
        elif posicaoEscolhidaX-1==listabombas[i][0] and posicaoEscolhidaY+1==listabombas[i][1]:
            contador=contador+1
        elif posicaoEscolhidaX-1==listabombas[i][0] and posicaoEscolhidaY-1==listabombas[i][1]:
            contador=contador+1 
    return contador


def campominadofacil(nomefacil,campofacil=np.array([[0,1,2,3],[1,'x','x','x'],[2,'x','x','x'],[3,'x','x','x']]),pontos=0,listabombas=geradordebombas(2,3)):
    '''funcao que define o campo minado 3x3 e realiza o jogo propriamente, note que a funcao recebe argumentos padrao caso nao haja nenhum jogo salvo'''

    #condicoes para que o laco se repita ate o fim do jogo
    lost=False
    win=False

    #Laco para comparar a posicao escolhida no input com a posicao das bombas sorteadas
    while not lost and not win:

        #Cada vez que o laco e percorrido, uma nova matriz e printada, para que o jogador esteja a par das bombas no entorno da posicao escolhida
        print(np.array(campofacil))

        #pede uma posicao de coluna e linha para cada rodada
        posicaoEscolhidaX,posicaoEscolhidaY=posicaoescolhida(3)

        #condicional que reconhe que o jogador quer sair do jogo atual, salvando-o
        if posicaoEscolhidaX=='sair' or posicaoEscolhidaY=='sair':

            #arquivos que salvam o estado do jogo ate o momento que ele e encerrado
            f=open('jogofacil.txt','w')
            f.write(str(campofacil)+'\n')
            f.write(str(pontos)+'\n')
            f.write(str(listabombas)+'\n')
            f.write(nomefacil+'\n')
            f.close()
            break

        #laco para comparar as posicoes escolhidas atraves do input com a posicao das bombas
        for i in range(len(listabombas)):
            if posicaoEscolhidaX==listabombas[i][0] and posicaoEscolhidaY==listabombas[i][1]:
                #mostra a mensagem de derrota, e salva  a pontuacao do jogador ate o momento da derrota
                print('Boom! Voce perdeu.')
                print('Localizacao das bombas: ')
                print(listabombas)
                f=open('pontuacaomedio.txt','a+')
                f.write(nomefacil+'   '+str(pontos)+'\n')
                f.close()
                lost=True
                break

        # condicional que so ocorre caso o jogador nao tenha colidido com nenhuma bomba, contabilizando um ponto    
        if not lost:
            contador = contadordebombas(listabombas, posicaoEscolhidaX, posicaoEscolhidaY)
            campofacil[posicaoEscolhidaX][posicaoEscolhidaY]=contador
            pontos = pontos+1
       
        #Condicional utilizada para encerrar o laco de repeticao , quando a pontuacao maxima por rodada e atingida, indicando a vitoria
        if pontos==7:

            #mostra a mensagem de vitoria, e salva a pontuacao do jogador nesta tentiva
            print('Voce venceu.')
            f=open('pontuacaofacil.txt','a')
            f.write(nomefacil+str(pontos)+'\n')
            f.close()
            win=True
    return
    

def campominadomedio(nomemedio,campomedio=np.array([[0,1,2,3,4,5,6],[1,'x','x','x','x','x','x'],[2,'x','x','x','x','x','x'],[3,'x','x','x','x','x','x'],[4,'x','x','x','x','x','x'],[5,'x','x','x','x','x','x'],[6,'x','x','x','x','x','x']]),pontos=0,listabombas=geradordebombas(10,6)):
    '''funcao que cria o campominado medio 6x6 e realiza o jogo propriamente, note que a funcao recebe argumentos padrao caso nao haja nenhum jogo salvo'''
    #condicoes para que o laco se repita ate o fim do jogo
    lost = False
    win = False
    
    #Variavel que contabiliza os pontos por rodada 
    pontos=0

    #Laco para comparar a posicao escolhida no input com a posicao das bombas sorteadas
    while not lost and not win:

        #Cada vez que o laco e percorrido, uma nova matriz e printada, para que o jogador esteja a par das bombas no entorno da posicao escolhida
        print(np.array(campomedio))

        posicaoEscolhidaX,posicaoEscolhidaY=posicaoescolhida(6)
        if posicaoEscolhidaX=='sair' or posicaoEscolhidaY=='sair':
            f=open('jogomedio.txt','w')
            f.write(str(campomedio)+'\n')
            f.write(str(2*pontos)+'\n')
            f.write(str(listabombas)+'\n')
            f.write(nomemedio+'\n')
            f.close()
            break
        #Condicional que verifica a colisao com a bomba, de modo a encerrar o jogo
        for i in range(len(listabombas)):
            if posicaoEscolhidaX==listabombas[i][0] and posicaoEscolhidaY==listabombas[i][1]:
                print('Boom! Voce perdeu.')
                print('Localizacao das bombas: ')
                print(listabombas)
                f=open('pontuacaomedio.txt','a+')
                f.write(nomemedio+'   '+str(2*pontos)+'\n')
                f.close()
                lost=True
                break

        # condicional que so ocorre caso o jogador nao tenha colidido com nenhuma bomba, contabilizando um ponto    
        if not lost:
            contador = contadordebombas(listabombas, posicaoEscolhidaX, posicaoEscolhidaY)
            campomedio[posicaoEscolhidaX][posicaoEscolhidaY]=contador
            pontos = pontos+1

        #Condicional utilizada para encerrar o laco de repeticao infinito, quando a pontuacao maxima por rodada e atingida, indicando a vitoria
        if pontos==26:
            print('Voce venceu.')
            pontos=2*pontos
            f=open('pontuacaomedio.txt','a+')
            f.write(nomemedio+'   '+str(2*pontos)+'\n')
            f.close()
            win=True
    return         
def pontuacao():
    '''funcao que contabiliza a pontuacao de cada jogador, retornando a pontuacao e o nome atraves de listas'''

    #listas com o nome e a pontuacao do jogador, discriminadas por dificuldade
    listanomefacil=[]
    listapontuacaofacil=[]
    listanomemedio=[]
    listapontuacaomedio=[]

    #try para verificar se ha alguma pontuacao preexistente, evitando que o programa encerre com o FileNotFoundError
    try:
        f=open('pontuacaofacil.txt','r')

        #laco para escrever os dados do arquivo na lista
        for linha in f:
            listanomefacil.append(linha[:-5])
            listapontuacaofacil.append(linha[-4:-1])
        f.close()    
    except FileNotFoundError:
        pass
    try:    
        g=open('pontuacaomedio.txt','r')         

        #laco para escrever os dados do arquivo na lista
        for conteudo in g:
            listanomemedio.append(conteudo[:-5])
            listapontuacaomedio.append(conteudo[-4:-1])
        g.close()    
    except FileNotFoundError:
        pass                           
    return listanomefacil,listapontuacaofacil,listanomemedio,listapontuacaomedio
    
def conversor(arquivo,ordemMatriz):
    '''Funcao que reconverte os estados dos jogos que foram salvos nos arquivos, recebendo por argumento uma string com o nome do arquivo e a 
    ordem da matriz'''

    #try para verificar se ha algum jogo salvo
    try:
        f=open(arquivo,'r')
    except FileNotFoundError:
        print('Nao ha jogo salvo')
    else:
        #Definicao das variaveis auxiliares a as listas que serao passadas por argumento para a funcao campominado
        linha=0
        campoSalvo=[]
        campoauxiliar=[]
        campo=[]
        bombasAuxiliar=[]
        listabombas=[]
        contador=0
        auxiliar1=0
        auxiliar2=ordemMatriz+1
        
        #lacos para ler as informacoes do estado do jogo no arquivo
        while linha<ordemMatriz+1:
            campoSalvo=campoSalvo+[f.readline()[:-1]]
            linha=linha+1

        #laco que transforma a lista com todas as informacoes da linha em uma lista com os dados relevantes para a matriz
        for indice in range(len(campoSalvo)):              
            for termo in campoSalvo[indice]:
                if termo=='x':
                    campoauxiliar=campoauxiliar+[termo]
                try:
                    campoauxiliar=campoauxiliar+[int(termo)]
                except ValueError:
                    continue 

        #laco que transforma a lista com dados relevantes da matriz em uma lista de lsitas
        for indice in range(ordemMatriz+1):
            for n in range(6):
                if indice==n+1:
                    auxiliar1=(n+1)*(ordemMatriz+1)
                    auxiliar2=(n+2)*(ordemMatriz+1) 
            campo=campo+[campoauxiliar[auxiliar1:auxiliar2]]

        #leitura dos demais dados que definem o estado do campo minado inacabado    
        pontosSalvo=f.readline()[:-1]
        listabombasSalva=f.readline()[:-1]
        nome=f.readline()[:-1]

        #laco para transformar a lista em lista de listas, para que esteja no formato utilizado na funcao campominado                      
        for caractere in listabombasSalva:
            try:
                bombasAuxiliar=bombasAuxiliar+[int(caractere)]
                contador=contador+1
            except ValueError:
                continue  
            for n in range(10): 
                if contador==2*n:
                    listabombas=listabombas+[bombasAuxiliar]
                    bombasAuxiliar=[]
        pontos=int(pontosSalvo) 
        f.close()

        #Condicional para verificar se o jogo salvo foi o facil       
        if ordemMatriz==3:
            campofacil=campo 
            nomefacil=nome
            return nomefacil,campofacil,pontos,listabombas

        #Condicional para verificar se o jogo salvo foi o medio    
        elif ordemMatriz==6:
            campomedio=campo
            nomemedio=nome
            return nomemedio,campomedio,pontos,listabombas    
       
def main():
    '''Funcao que define o menu principal e interage com o mesmo, recebendo todas as demais funcoes'''
    
    while True:
        #imprime o menu     
        print('|xxxxxxxx Bem vindo ao campo minado! xxxxxxxx|')
        print('1 - Escolha um modo de jogo')
        print('2 - Escolha para ver sua pontuacao')
        print('3 - Escolha para mais informacoes.')
        print('4 - Continuar um jogo salvo')
        print('5 - Escolha para sair.')

        #verifica se a opcao pedida no input e razoavel com as opcoes disponiveis
        try:
            opcao=int(input('Escolha uma das opcoes: '))
            if opcao>5 or opcao<1:
                raise ValueError 
        except ValueError:
            print('Opcao invalida') 
            print('Digite um valor entre 1 e 5')

        #verifica que opcao foi escolhida no input 'opcao'    
        else:           
            if opcao == 1:
                while True:
                    print('1 - Modo de jogo facil')
                    print('2 - Modo de jogo medio')
                    print('3 - Escolha para sair ')

                    #verifica se o valor passado por input e valido
                    try:
                        escolha=int(input('Escolha uma das opcoes:'))
                        if escolha>3 or escolha<1:
                            raise ValueError
                    except ValueError:
                        print('Valor invalido.')
                        print('DIgite um inteiro entre 1 e 3')
                    else:   
                        #inicia um jogo no facil   
                        if escolha==1:    
                            nomefacil=str(input('Digite o seu nome: '))
                            campominadofacil(nomefacil,campofacil=np.array([[0,1,2,3],[1,'x','x','x'],[2,'x','x','x'],[3,'x','x','x']]),pontos=0,listabombas=geradordebombas(2,3))

                        #inicia um jogo no medio     
                        elif escolha==2:      
                            nomemedio=str(input('Digite o seu nome: '))
                            campominadomedio(nomemedio,campomedio=np.array([[0,1,2,3,4,5,6],[1,'x','x','x','x','x','x'],[2,'x','x','x','x','x','x'],[3,'x','x','x','x','x','x'],[4,'x','x','x','x','x','x'],[5,'x','x','x','x','x','x'],[6,'x','x','x','x','x','x']]),pontos=0,listabombas=geradordebombas(10,6))

                        #retorna ao menu principal      
                        elif escolha==3:
                            break

            #mostra  a pontuacao do jogador ate o dado momento                                      
            if opcao == 2:
                print('Pontuacao:')
                print('Observacao: jogos inacabados nao tem sua pontuacao salva.')

                #chama a funcao pontuacao com as listas a serem mostradas pro jogador, devidamente formatadas
                listanomefacil,listapontuacaofacil,listanomemedio,listapontuacaomedio=pontuacao()

                pos=0

                #verifica se ha algum elemento na lista, para, entao, mostrar a pontuacao    
                if len(listanomefacil)>0:
                    while pos<len(listanomefacil):
                        print('Pontuacao campo minado facil: Jogador:'+listanomefacil[pos]+', Pontos: '+listapontuacaofacil[pos])
                        pos=pos+1

                #verifica se ha algum elemento na lista, para, entao, mostrar a pontuacao         
                if len(listanomemedio)>0:
                    pos=0        
                    while pos<len(listanomemedio):
                        print('Pontuacao campo minado medio: Jogador:'+listanomemedio[pos]+', Pontos: '+listapontuacaomedio[pos])
                        pos=pos+1

            #mostra um painel de explicacoes acerca do campo minado    
            elif opcao == 3:
                print('O jogo possui 2 niveis de dificuldade: um facil e um medio.')
                print('O modo de jogo facil e um campo minado 3x3 com 2 bombas.')
                print('O modo de jogo medio e um campo minado 6x6 com 10 bombas.')
                print('A aba de pontuacao mostra a pontuacao de cada jogador nos dois modos, a pontuacao do modo medio possui o dobro de valor')                
                print('A opcao continuar um jogo salvo permite que voce continue um jogo que nao foi terminado, seja ele no modo facil ou medio')
                print('Para encerrar um jogo em andamento, digite "sair" quando for perguntada uma posicao no campo minado \nlembre-se que o jogo e salvo automaticamente ao sair')

            #mostra o menu de jogos inacabados
            elif opcao==4:
                while True:
                    print('1 - Continuar o ultimo jogo facil inacabado.')
                    print('2 - Continuar o ultimo jogo medio inacabado.')
                    print('3 - Escolha para sair.')

                    #try para verificar se os valores passados por input sao validos    
                    try:
                        escolha=int(input('Escolha uma das opcoes:'))
                        if escolha<1 or escolha>3:
                            raise ValueError
                    except ValueError:
                        print('Opcao invalida.')
                        print('Escolha um valor entre 1 e 3.')
                    else:
                        #acessa um jogo facil inacabado, trazendo as informacoes do conversor como argumento da funcao campominadofacil
                        if escolha==1:
                            nomefacil,campofacil,pontos,listabombas=conversor('jogofacil.txt',3)
                            campominadofacil(nomefacil,campofacil,pontos,listabombas)

                        #acessa um jogo medio inacabado, trazendo as informacoes do conversor como argumento da funcao campominadomedio         
                        elif escolha==2:
                            nomemedio,campomedio,pontos,listabombas=conversor('jogomedio.txt',6)
                            campominadomedio(nomemedio,campomedio,pontos,listabombas)

                        #retorna ao menu                                  
                        elif escolha==3:
                            break
            #encerra o programa quando o jogador selecionar esta opcao            
            elif opcao==5:
                print('Obrigado por jogar')
                break
    return 
if __name__=='__main__':
    main()   


    

    








     



            
    

        















    

                  

        

    
    
    



    


        





    