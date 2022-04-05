#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int licz=0;
    char znak;
    char zdanie[100];
    char c;

    printf("Podaj znak do zliczania: ");
    scanf(" %c", &znak);

    while(getc(stdin)!='\n'){} //czysciciel

    printf("Podaj zdanie do sprawdzenia: ");

    while(1)
    {
        scanf("%s", &zdanie);
        for( char * p = strchr( zdanie, znak ); p != NULL; p = strchr( p + 1, znak ) )
        {
            licz=licz+1;
        }
        if ((c = getchar()) == '\n') break;
    }

    printf("Znak '%c' wystapil '%d' raz/y\n",znak,licz);

    return 0;
}
