#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void GenerujPesel()
{
    int pesel[20];
    char Rok[4];
    int trzymRok;
    char Miesiac[2];
    char Dzien[2];
    char Plec;
    srand(time(NULL));

//ROK wypisanie
    printf("Podaj rok urodzenia (np. 1939): ");
    scanf("%s",&Rok);

    //ROK sprawdzenie
    if (strlen(Rok) != 4)
    {
        printf("\nNiepoprawny zapis roku (BLEDNE DANE)");
        exit(0);
    }

    pesel[0]=Rok[2] - '0';
    pesel[1]=Rok[3] - '0';
    trzymRok = atoi(Rok);

//MIESIAC wypisanie
    printf("Podaj miesiac urodzenia (Od: 1-12): ");
    scanf("%s",&Miesiac);

    //MIESIAC sprawdzenie
    if (strlen(Miesiac) != 1)
    {
       pesel[2]=Miesiac[0] - '0';
       pesel[3]=Miesiac[1] - '0';
    }
    else
    {
        pesel[2]=0;
        pesel[3]=Miesiac[0] - '0';
    }

    if(trzymRok>=1800 && trzymRok<=1899)
    {
        pesel[1] = pesel[1] + 8;
    }
    else if(trzymRok>=1900 && trzymRok<=1999)
    {
        pesel[1] = pesel[1];
    }
    else if(trzymRok>=2000 && trzymRok<=2099)
    {
        pesel[1] = pesel[1] + 2;
    }
    else if(trzymRok>=2100 && trzymRok<=2199)
    {
        pesel[1] = pesel[1] + 4;
    }
    else if(trzymRok>=2200 && trzymRok<=2299)
    {
        pesel[1] = pesel[1] + 6;
    }

//DZIEN
    printf("Podaj dzien urodzenia (Od: 1-31): ");
    scanf("%s",&Dzien);

    //DZIEN sprawdzenie
    if (strlen(Dzien) != 1)
    {
       pesel[4]=Dzien[0] - '0';
       pesel[5]=Dzien[1] - '0';
    }
    else
    {
        pesel[4]=0;
        pesel[5]=Dzien[0] - '0';
    }
//PLEC
    printf("Podaj plec jesli Kobieta podaj 'K' lub 'k' jesli Mezczyzna podaj 'M' lub 'm':");
    scanf("%s",&Plec);

    //PLEC sprawdzenie
    if(Plec == 'M' || Plec == 'm')
    {
        do
        {
            pesel[9] = rand() % 10;
        }while (pesel[9]%2==0);
    }
    else if(Plec == 'K' || Plec == 'k')
    {
        do
        {
            pesel[9] = rand() % 10;
        }while (pesel[9]%2!=0);
    }
    else
    {
        printf("Podana NIEDOZWOLONA plec!");
        exit(0);
    }

    //LICZBY uzupelniajce do nr pesel
    pesel[6] = rand() % 10;
    pesel[7] = rand() % 10;
    pesel[8] = rand() % 10;

    //WYLICZENIE sumy kontrolnej
    pesel[10]=(1*pesel[0])+(3*pesel[1])+(7*pesel[2])+(9*pesel[3])+(1*pesel[4])+(3*pesel[5])+(7*pesel[6])+(9*pesel[7])+(1*pesel[8])+(3*pesel[9]);
    pesel[10] = pesel[10] % 10;
    pesel[10] = 10 - pesel[10];
    if(pesel[10]==10)
    {
        pesel[10]=0;
    }
    printf("Twoj PESEL to: ");
    for(int x=0; x<11; x++)
    {
       printf("%d",pesel[x]);
    }

}

int main()
{
    GenerujPesel();

    return 0;
}


