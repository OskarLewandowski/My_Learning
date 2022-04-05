#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void SprDlugosc(char PESEL[11])
{
    if (strlen(PESEL) != 11)
    {
        printf("\nERROR (BLEDNE DANE)\n");
        exit(0);
    }
}

int SprPesel(int a, int b, int c, int d, int e, int f, int g, int h,int i, int j , int k)
{
    int suma, wynik;
    suma=(1*a)+(3*b)+(7*c)+(9*d)+(1*e)+(3*f)+(7*g)+(9*h)+(1*i)+(3*j);
    wynik = 10 - (suma%10);

    if(wynik==k)
    {
        return 1;
        //printf("Podany PESEL jest prawidlowy!\n");
    }
    else
    {
        return 0;
        //printf("Podany PESEL jest nieprawidlowy!\n");
    }
}

int RokUr(int a,int b,int c,int d)
{
    int rok;
    int miesiac;
	rok = 10 * a;
	rok = rok + b;
	miesiac = 10 * c;
	miesiac = miesiac + d;

	if (miesiac > 80 && miesiac < 93)
    {
		rok = rok + 1800;
	}
	else if (miesiac > 0 && miesiac < 13)
    {
		rok = rok + 1900;
	}
	else if (miesiac > 20 && miesiac < 33)
    {
		rok = rok + 2000;
	}
	else if (miesiac > 40 && miesiac < 53)
	{
		rok = rok + 2100;
	}
	else if (miesiac > 60 && miesiac < 73)
    {
		rok = rok + 2200;
	}
	return rok;
    //printf("Rok urodzenia: %d\n",rok);
}

void MiesiacUr(int c,int d)
{
    int miesiac;
	miesiac = 10 * c;
	miesiac = miesiac + d;
	if (miesiac > 80 && miesiac < 93)
    {
        miesiac = miesiac - 80;
	}
	else if (miesiac > 20 && miesiac < 33)
	{
		miesiac = miesiac - 20;
	}
	else if (miesiac > 40 && miesiac < 53)
	{
		miesiac = miesiac - 40;
	}
	else if (miesiac > 60 && miesiac < 73)
	{
		miesiac = miesiac - 60;
	}
	switch(miesiac)
	{
    case 1:
        printf("Miesiac urodzenia: Styczen(%d)\n",miesiac);
        break;
    case 2:
         printf("Miesiac urodzenia: Luty(%d)\n",miesiac);
        break;
    case 3:
         printf("Miesiac urodzenia: Marzec(%d)\n",miesiac);
        break;
    case 4:
         printf("Miesiac urodzenia: Kwiecien(%d)\n",miesiac);
        break;
    case 5:
         printf("Miesiac urodzenia: Maj(%d)\n",miesiac);
        break;
    case 6:
         printf("Miesiac urodzenia: Czerwiec(%d)\n",miesiac);
        break;
    case 7:
         printf("Miesiac urodzenia: Lipiec(%d)\n",miesiac);
        break;
    case 8:
         printf("Miesiac urodzenia: Sierpien(%d)\n",miesiac);
        break;
    case 9:
         printf("Miesiac urodzenia: Wrzesien(%d)\n",miesiac);
        break;
    case 10:
         printf("Miesiac urodzenia: Pazdziernik(%d)\n",miesiac);
        break;
    case 11:
         printf("Miesiac urodzenia: Listopad(%d)\n",miesiac);
        break;
    case 12:
         printf("Miesiac urodzenia: Grudzien(%d)\n",miesiac);
        break;
    default:
         printf("Miesiac urodzenia: %d\n",miesiac);
	}
	}

int DzienUr(int e,int f)
{
   	int dzien;
	dzien = 10 * e;
	dzien = dzien + f;
	return dzien;
    //printf("Dzien urodzenia: %d\n",dzien);
}

int Plec(int j)
{
	if (j % 2 == 1)
    {
        return 1;
        //printf("Plec: Mezczyzna");
    }
    else
    {
        return 0;
        //printf("Plec: Kobieta");
    }
}

int main()
{
    int a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0, i=0, j=0, k=0;
    char PESEL[11];
    printf("Podaj numer PESEL: ");
    scanf("%s",PESEL);
    SprDlugosc(PESEL);

    a=PESEL[0] - '0';
    b=PESEL[1] - '0';
    c=PESEL[2] - '0';
    d=PESEL[3] - '0';
    e=PESEL[4] - '0';
    f=PESEL[5] - '0';
    g=PESEL[6] - '0';
    h=PESEL[7] - '0';
    i=PESEL[8] - '0';
    j=PESEL[9] - '0';
    k=PESEL[10] - '0';

    if(SprPesel(a,b,c,d,e,f,g,h,i,j,k)==1)
    {
        printf("Podany PESEL jest prawidlowy!\n");
    }
    else
    {
        printf("Podany PESEL jest nieprawidlowy!\n");
    }


    printf("Rok urodzenia: %d\n",RokUr(a,b,c,d));
    MiesiacUr(c,d);

    printf("Dzien urodzenia: %d\n",DzienUr(e,f));
    if(Plec(j)==1)
    {
        printf("Plec: Mezczyzna");
    }
    else
    {
        printf("Plec: Kobieta");
    }


  return 0;
}
