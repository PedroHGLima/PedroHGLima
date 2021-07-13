#include                        <stdio.h>
#include                        <string.h>

#define OK                      0
#define TAMANHO_MAX             50

int main()
{
    char letra, palavra1[TAMANHO_MAX], palavra2[TAMANHO_MAX];
    int indice, contador, indiceMontador, tamanho;
      

    for (;;)
    {
        // Pegando a primeira palavra
        printf ("Digite a primeira palavra: ");
        scanf("%[^\n]%*c", palavra1);
        if (strlen(palavra1) > TAMANHO_MAX)
            printf ("A palavra excede o tamanho maximo de %d caracteres\n", TAMANHO_MAX);
        else
            break;
    }

    for (;;)
    {
        // Pegando a segunda palavra
        printf ("Digite a segunda palavra: ");
        scanf("%[^\n]%*c", palavra2);
        if (strlen(palavra2) > TAMANHO_MAX)
            printf ("A palavra excede o tamanho maximo de %d caracteres\n", TAMANHO_MAX);
        else
            break;
    }

    tamanho = strlen(palavra2);

    if (strlen(palavra1) != tamanho)
    {
        printf ("As palavras nao sao anagramas\r\n");
        return OK;
    }

    for (indice = 0; indice < strlen(palavra1); indice++)
    {
        letra = palavra1[indice];
        for (contador = 0; contador < tamanho; contador++)
        {
            if (letra == palavra2[contador])
            {
		    tamanho--;
		    for (indiceMontador=contador; indiceMontador<tamanho; indiceMontador++)
			    palavra2[indiceMontador] = palavra2[indiceMontador+1];
		    break;
	        }
	    }
    }

    if (tamanho == 0)
	    printf ("As palavras sao anagramas\r\n");
    else
	    printf ("As palavras nao sao anagramas\r\n");
    
    return OK;
}