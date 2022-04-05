#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define ROZMIAR 20

int czyliczba(char ciag[ROZMIAR])
{
    int i;
    //int liczba=0;
    int znak=0;

    for(i = 0; ciag[i]; i++)
    {
         if(isdigit(ciag[i]))
         {
             //liczba=liczba + 1;
         }
         else
         {
             znak = znak +1;
         }
    }
    if(znak>0)
    {
        return 0;
        //printf("\nPodany ciag nie jest liczba!\n");
    }
    else
    {
        return 1;
        //printf("\nPodany ciag jest liczba!\n");
    }

}

int main()
{
    char ciag[ROZMIAR];
    printf("Podaj ciag do sprawdzenia: ");
    scanf("%s",&ciag);
    if(czyliczba(ciag)==0)
    {
        printf("\nPodany ciag nie jest liczba!\n");
    }
    else
    {
        printf("\nPodany ciag jest liczba!\n");
    }
    return 0;
}
