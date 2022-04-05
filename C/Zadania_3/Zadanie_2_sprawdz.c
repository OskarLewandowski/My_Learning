#include <stdio.h>
#include <stdlib.h>

int SprPesel(char PESEL[11])
{
    int a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0, i=0, j=0, k=0, suma=0, wynik=0;

    a=PESEL[0] - '0'; //ASCII 0=48
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
/*
    printf("Wynik = %d\n", a );
    printf("Wynik = %d\n", b );
    printf("Wynik = %d\n", c );
    printf("Wynik = %d\n", d );
    printf("Wynik = %d\n", e );
    printf("Wynik = %d\n", f );
    printf("Wynik = %d\n", g );
    printf("Wynik = %d\n", h );
    printf("Wynik = %d\n", i );
    printf("Wynik = %d\n", j );
    printf("Wynik = %d\n", k );
*/

    suma=(1*a)+(3*b)+(7*c)+(9*d)+(1*e)+(3*f)+(7*g)+(9*h)+(1*i)+(3*j);

    //printf("SUMA = %d\n",suma);

    wynik = 10 - (suma%10);

    //printf("WYNIK = %d\n",wynik);

    if(wynik==k)
    {
        return 1;
        //printf("\nPodany PESEL jest prawidlowy!\n");
    }
    else
    {
        return 0;
        //printf("\nPodany PESEL jest nieprawidlowy!\n");
    }
}

int main()
{

  char PESEL[11];
  printf("Podaj numer PESEL: ");
  scanf("%s",PESEL);

  if (strlen(PESEL) != 11)
  {
      printf("\nERROR (BLEDNE DANE)\n");
      exit(0);
  }

  if(SprPesel(PESEL)==1)
  {
      printf("\nPodany PESEL jest prawidlowy!\n");
  }
  else
  {
      printf("\nPodany PESEL jest nieprawidlowy!\n");
  }

  return 0;
}
