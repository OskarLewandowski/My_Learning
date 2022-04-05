#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

bool sprcyfra(char tekst)
{
    if(tekst>=49 && tekst<=57)
    {
      return true;
    }
    return false;
}

bool sprspecjalna(char tekst)
{
    if((tekst>=33 && tekst<=47) ||(tekst>=58 && tekst<=64) || (tekst>=91 && tekst<=96)|| (tekst>=123 && tekst<=126))
    {
      return true;
    }
    return false;
}

bool duza(char tekst)
{
    if(isupper(tekst))
    {
      return true  ;
    }
    return false;
}

bool mala(char tekst)
{
    if(islower(tekst))
    {
        return true;
    }
    return false;
}

int main()
{

char tekst;
int malal=0;
int duze=0;
int cyfra=0;
int specjalna=0;

    printf("Sprawdz haslo (Wymagana co najmniej jedna duza lub mala litera, cyfra oraz znak specjalny) : ");

    putchar(tekst);

    while(tekst!='\n')
    {
        tekst=getchar();
        if(mala(tekst)==true)
        {
            malal = malal + 1;
        }
        if(duza(tekst)==true)
        {
            duze = duze + 1;
        }
        if(sprcyfra(tekst)==true)
        {
             cyfra = cyfra + 1;
        }
        if(sprspecjalna(tekst)==true)
        {
             specjalna = specjalna + 1;
        }
    }

    if((malal >= 1 || duze >= 1) && cyfra >= 1 && specjalna >=1 )
    {
        printf("mala = %d duza = %d liczba = %d specjalna=  %d \n", malal , duze , cyfra , specjalna );
        printf("\nHaslo poprawne!\n");
    }
    else
    {
        printf("mala = %d duza = %d liczba = %d specjalna = %d \n", malal , duze , cyfra , specjalna );
        printf("\nHaslo niepoprawne!\n");
    }

    return 0;
}
