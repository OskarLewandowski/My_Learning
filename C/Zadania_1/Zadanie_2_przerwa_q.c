#include <stdio.h>
#include <string.h>

int main()
{
    char tekst;
    printf("Mozesz teraz pisac do woli, aby zakonczyc nacisnj 'Q':");
    putchar(tekst);
    while(tekst!='Q')
    {
        tekst=getchar();
        putchar(tekst);
    }
    printf("\n\nKoniec programu nacisnoles 'Q'\n");
    return 0;
}
