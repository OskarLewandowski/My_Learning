#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void SprDlugosc(int dlugosc)
{
    if(dlugosc < 4)
    {
        printf("\nPodana wartosc dlugosci hasla jest za mala (%d) MIN [4<=]\n",dlugosc);
        exit(0);
    }
    else if(dlugosc > 20)
    {
        printf("\nPodana wartosc dlugosci hasla jest za duza (%d) MAX [>=20]\n",dlugosc);
        exit(0);
    }
    else
    {
        printf("\nPodano prawdidlowa dlugosc hasla...\n\n");
    }
}

int main()
{
    srand(time(NULL));
    int specjalsi[]={33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,123,124,125,126}; //ZNAKI SPECJALNE JAKO KOD ASCII
    int ilosc_znakow=0;
    int dlugosc;
    int trzym;
    int i = 0;


    printf("Podaj dlugosc hasla do wygenerowania (od 4 do 20): ");
    scanf("%d",&dlugosc);
    SprDlugosc(dlugosc);

    int haslo[dlugosc];
    int literaDuza[dlugosc];
    int literaMala[dlugosc];
    int cyfra[dlugosc];
    int znakSpecjalny[dlugosc];

    for(i = 0; i < dlugosc; i++)
    {
        //duza
        literaDuza[i] = rand() % 26 + 65;
        haslo[i]=literaDuza[i];
        //mala
        literaMala[i] = rand() % 26 + 97;
        haslo[i+1]=literaMala[i];
        //cyfra
        cyfra[i] = rand() % 10 + 48;
        haslo[i+2]=cyfra[i];
        //znak specjalny
        trzym = rand() % 32;
        znakSpecjalny[i] = specjalsi[trzym] ;
        haslo[i+3]=znakSpecjalny[i];
    }

    printf("Twoje haslo to: ");

    for(i = 0; i < dlugosc; i++)
    {
        if(ilosc_znakow!=dlugosc)
        {
            printf("%c",literaDuza[i]);
            ilosc_znakow++;
        }
        if(ilosc_znakow!=dlugosc)
        {
            printf("%c",literaMala[i]);
            ilosc_znakow++;
        }
        if(ilosc_znakow!=dlugosc)
        {
            printf("%c",cyfra[i]);
            ilosc_znakow++;
        }
        if(ilosc_znakow!=dlugosc)
        {
            printf("%c",znakSpecjalny[i]);
            ilosc_znakow++;
        }
        else
        {
            printf("\n");
            exit(0);
        }
    }
    return 0;
}
