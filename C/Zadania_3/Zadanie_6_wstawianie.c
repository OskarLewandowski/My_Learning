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

void SortPrzWstawianie(int tablica[],int n)
{
    int x,j,i;

    for(j = n - 2; j >= 0; j--)
    {
        x = tablica[j];
        i = j + 1;
        while((i < n) && (x > tablica[i]))
        {
            tablica[i - 1] = tablica[i];
            i++;
        }
        tablica[i - 1] = x;
    }
}

int main()
{

    int tablica[]={99,26,42,57,2,77,19,69,24,9,54,433};
    int n = sizeof(tablica)/sizeof(tablica[0]);
    printf("Przed sortowaniem: \n\n");
    wyswietl(tablica,n);
    SortPrzWstawianie(tablica,n);
    printf("Po sortowaniu: \n\n");
    wyswietl(tablica,n);

    return 0;
}
