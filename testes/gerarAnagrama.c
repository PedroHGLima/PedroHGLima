#include                        <stdio.h>
#include                        <stdlib.h>
#include                        <time.h>
#include                        <string.h>

#define OK                      0
#define TAMANHO_MAX             50

int main()
/** gera e imprime um anagrama para uma palavra passada por input */  
{
    char palavra[TAMANHO_MAX], auxiliar, saida[TAMANHO_MAX];
    int indice, teto, primeiro, segundo;

    srand(time(NULL));

    for (;;)
    {
        // Pegando a palavra
        printf ("Digite a palavra: ");
        scanf("%[^\n]%*c", palavra);
        teto = strlen(palavra);
        if (teto > TAMANHO_MAX)
            printf ("A palavra excede o tamanho maximo de %d caracteres\n", TAMANHO_MAX);
        else
            break;
    }

    /* Copiando a palavra de entrada para a saida, 
     * para poder permutar as letras da saida sem alterar a original.
     * A variavel teto serve para delimitar o maior inteiro a ser gerado
     * no processo de permutacao, para evitar erros inesperados */
    strcpy(saida, palavra);

    /* o valor escolhido para o fim do laco eh a quantidade de permutacoes que ocorrerao
     *   este valor eh completamente arbitrario */
    for (indice = 0; indice<teto*5; indice++)
    {
        // definindo as posicoes a serem permutadas
        primeiro = (rand()%(teto));
        segundo = (rand()%(teto));

        // permutando os valores
        auxiliar = saida[primeiro];
        saida[primeiro] = saida[segundo];
        saida[segundo] = auxiliar;
    }
    printf ("Um anagrama para %s eh %s\n", palavra, saida);
    return OK;
}