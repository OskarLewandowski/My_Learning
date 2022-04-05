#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define ROZMIAR 20

int czyliczba(char ciag[ROZMIAR])
{
    int i;
    int liczba;
    int znak=0;

    for(i = 0; ciag[i]; i++)
    {

      if(isdigit(ciag[i]))
         {
            liczba = atoi(ciag);
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
        return liczba;
       // printf("\nPodany ciag jest liczba!\n\nWprowadzono liczbe: %d\n",liczba);
       // printf("\nSprawdzenie liczba*2: %d\n",liczba*2);
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
        printf("\nPodany ciag jest liczba!\n\nWprowadzono liczbe: %d\n",czyliczba(ciag));
        printf("\nSprawdzenie liczba*2: %d\n",czyliczba(ciag)*2);
    }

    return 0;
}

