#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x, y;
    printf("Podaj pierwsza liczbe:");
    scanf("%d",&x);
    printf("Podaj druga liczbe:");
    scanf("%d",&y);
    printf("\nWynik dodawania: %d + %d = %d ",x,y,x+y);
    printf("\nWynik odejmowania: %d - %d = %d ",x,y,x-y);
    printf("\nWynik mnozenia: %d * %d = %d ",x,y,x*y);
    if(x==0||y==0)
    {
        printf("\nNie dzielimy przez zero!\n");
    }
    else
    {
        printf("\nWynik dzielenia: %d / %d = %d \n",x,y,x/y);
    }

    return 0;
}
