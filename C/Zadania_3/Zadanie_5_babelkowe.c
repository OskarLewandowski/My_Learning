#include <stdio.h>
#include <stdlib.h>

void wyswietl(int tablica[], int n)
{
    int i = 0;
    for(i = 0; i < n; i++)
    {
        printf(" %*d ",2,tablica[i]); //printf("%*d", width, value);
    }
    printf("\n\n");
}

void SortBabelkowe(int tablica[], int n)
{
    int j,i;
    //int schowek;
    for(j = 0; j < n; j++)
    {
        for(i = 0; i < n - 1; i++)
        {
            if(tablica[i] > tablica[i + 1])
            {
                tablica[i] =  tablica[i]  ^  tablica[i + 1] ; // swap <-> xor
                tablica[i + 1] = tablica[i]  ^  tablica[i + 1] ;
                tablica[i] =  tablica[i + 1] ^ tablica[i];
               //schowek = tablica[i];
               //tablica[i] = tablica[i + 1];
               //tablica[i + 1] = schowek;
            }
        }
    }
}

int main()
{

    int tablica[]={99,26,42,57,241,77,19,69,24,9,63,77,23,1337};
    int n = sizeof(tablica)/sizeof(tablica[0]);
    printf("Przed sortowaniem: \n\n");
    wyswietl(tablica,n);
    SortBabelkowe(tablica,n);
    printf("Po sortowaniu: \n\n");
    wyswietl(tablica,n);

    return 0;
}
