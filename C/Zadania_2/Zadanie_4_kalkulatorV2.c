#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define ROZMIAR 20

int sprawdzenieX(char x[ROZMIAR])
{
    int i;
    char znak='Q';
    for(i = 0; x[i]; i++)
    {
        if(x[i]==znak)
        {
            return 0;
            //exit(0);
        }
        else
        {
            return 1;
        }
    }
}

int sprawdzenieY(char y[ROZMIAR])
{
    int i;
    char znak='Q';
    for(i = 0; y[i]; i++)
    {
        if(y[i]==znak)
        {
            return 0;
            //exit(0);
        }
        else
        {
            return 1;
        }
    }
}

int main()
{
    char x[ROZMIAR];
    char y[ROZMIAR];
    int xx;
    int yy;

    while(1)
    {

    printf("Podaj pierwsza liczbe:");
    scanf("%s",&x);
    xx = atoi(x);
    if(sprawdzenieX(x)==0)
    {
        exit(0);
    }


    printf("Podaj druga liczbe:");
    scanf("%s",&y);
    yy = atoi(y);
    if(sprawdzenieY(y)==0)
    {
        exit(0);
    }

    printf("\nWynik dodawania: %d + %d = %d ",xx,yy,xx+yy);
    printf("\nWynik odejmowania: %d - %d = %d ",xx,yy,xx-yy);
    printf("\nWynik mnozenia: %d * %d = %d ",xx,yy,xx*yy);
    if(xx==0||yy==0)
    {
        printf("\nNie dzielimy przez zero!\n");
    }
    else
    {
        printf("\nWynik dzielenia: %d / %d = %d \n",xx,yy,xx/yy);
    }
    printf("\n");
    }

    return 0;
}
