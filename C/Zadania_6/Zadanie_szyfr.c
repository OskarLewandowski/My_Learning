#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int sprawdzenie(int klucz)
{
    if(klucz<=-26 || klucz>=26)
    {
        //printf("%d",klucz);
        return 0;
    }
    else
    {
        //printf("%d",klucz);
        return 1;
    }
}

int czyliczba(char ciag[100])
{
    int i;
    int tak=0;
    int nie=0;
    for(i = 0; ciag[i]; i++)
    {
         if(isdigit(ciag[i]))
         {
             tak++;
         }
         else
         {
             nie++;
         }
    }
    if(tak>0)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

int sprawdz(char znak)
{
	//jezeli jest mala litera
	if(znak >= 'a' && znak <= 'z')
    {
        return 0;
	}
	//jezeli jest duza litera
	if(znak >= 'A' && znak <= 'Z')
	{
	    return 1;
	}
	else
    {
        return 2;
    }
}

char* szyfruj(int klucz, char tab[], int n)
{
    n=n+1;
    char *DoZwrocenia = (char *) malloc(sizeof(char) * n);
    //char *DoZwrocenia[n];
	//sprawdzenie, czy klucz miesci sie w zakresie

	int pom;
	char a, z;

	for(int i = 0; i < n; i++)
	{
		pom = sprawdz(tab[i]);

		if(pom < 2)
		{
			if(pom == 0)
            {
                a = 'a', z = 'z';
            }
            else
            {
                a = 'A', z = 'Z';
            }

			if(klucz >= 0)
				if(tab[i] + klucz <= z)
                {
                    tab[i] += klucz;
                }
				else
                {
                    tab[i] = tab[i] + klucz - 26;
                }
                else if(tab[i] + klucz >= a)
                {
                    tab[i] += klucz;
                }
				else
                {
                    tab[i] = tab[i] + klucz + 26;
                }
		 }
	}

	for(int j=0;j<n;j++)
    {
       DoZwrocenia[j]=tab[j];
    }
    return DoZwrocenia;
}

int main()
{
    char DoZaszyfrowania[100];
    int x;
    int trzym;

    printf("Podaj tekst do zaszyfrowania:");\
    scanf("%[^\t\n]s",&DoZaszyfrowania);
    if(czyliczba(DoZaszyfrowania)==0)
    {
        printf("\nWprowadzono niedozwolony znak w tekscie {BEZ LICZB)\n");
        exit(0);
    }

    printf("Podaj liczbe przesuniecia (-25 do 25):");\
    scanf("%d",&x);

    if(sprawdzenie(x)==0)
    {
        printf("\nWprowadzono niedozwolony przedzial przesuniecia\n");
        exit(0);
    }

    int n = strlen(DoZaszyfrowania);
    //printf("Tekst: %s Liczba: %d N: %d ",DoZaszyfrowania,x,n);

    printf("\nZaszyfrowanie...");
    printf("\n%s\n",szyfruj(x,DoZaszyfrowania,n));

    printf("\nDeszyfrowanie...");
    printf("\n%s\n",szyfruj(-x,DoZaszyfrowania,n));

    return 0;
}
