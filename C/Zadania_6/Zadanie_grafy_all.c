#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>
#define ILE 10 //ilosc wierzcholkow
#define MAX 9999 //wagi rozmiar max suma
#define ILE_KOLEJKA 10  //miejsce kolejkowe

//Takie tam kolorki informacja
void kolorki()
{
    HANDLE kolor;
    kolor = GetStdHandle( STD_OUTPUT_HANDLE );
    SetConsoleTextAttribute( kolor, 15 );

    printf("LEGENDA KOLORKOWA:\n");
    printf("Kolor bialy oznacza zwykly tekst - inforamcyjny wazny.\n");
    SetConsoleTextAttribute( kolor, 12 );
    printf("Kolor czerwony oznacza niedostepnosc danej \"rzeczy\" opisanej tekstem - niedostepne/falszywe.\n");
    SetConsoleTextAttribute( kolor, 10 );
    printf("Kolor zielony oznacza dostepnosc danej \"rzeczy\" opisanej tekstem  - dostepne/prawidlowe wazny.\n");
    SetConsoleTextAttribute( kolor, 14 );
    printf("Kolor zolty oznacza inforamcje pomocnicza  - inforamacyjny malo wazny.\n");
    SetConsoleTextAttribute( kolor, 11 );
    printf("Kolor niebieski oznacza inforamcje pomocnicza - informacyjny malo wazny.\n");
    SetConsoleTextAttribute( kolor, 13 );
    printf("Kolor rozowy oznacza numer zadania - informacyjny kolor oddzielajacy.\n");
    SetConsoleTextAttribute( kolor, 15 );
    printf("\n\n");
}

//--------------------------------------------------- ZADANIE_1
//wyswietla polacznia wagowe wierzcholkow
void wyswietl(int Graf[ILE][ILE])
{
    int i, j;
    printf("------------------------------------------------------------------------------------\n");
    for(int k = 0; k < ILE; k++)
    {
        printf("\t[%d]",k);
    }
    printf("\n");

    for(i = 0; i < ILE; i++)
    {
        printf("[%d]",i);
        for(j = 0; j < ILE; j++)
        {
            if(Graf[i][j]==0)
            {
                printf("\t -");
            }
            else
            {
                printf("\t %d",Graf[i][j]);
            }
        }
        printf("\n");
    }
    printf("------------------------------------------------------------------------------------");
    printf("\n\n");
}

void polaczenia(int Graf[ILE][ILE])
{
    HANDLE kolor;
    kolor = GetStdHandle( STD_OUTPUT_HANDLE );
    int i, j;
    int ilosc=0;
    for(i = 0; i < ILE; i++)
    {

        printf("Wierzcholek [%d] spis polaczen:\n",i);
        for(j = 0; j < ILE; j++)
        {
            if(Graf[i][j]==0)
            {
                SetConsoleTextAttribute( kolor, 12 );
                printf("Nie ma polaczenia z wierzcholkiem [%d]\n",j);
            }
            else
            {
                SetConsoleTextAttribute( kolor, 10 );
                printf("Ma polaczenie z wierzcholkiem [%d] o wadze (%d)\n",j,Graf[i][j]);
                ilosc++;
            }
        }
        SetConsoleTextAttribute( kolor, 14 );
        printf("Wierzcholek [%d] posiada %d polaczenia\n\n",i,ilosc);
        ilosc=0;
        SetConsoleTextAttribute( kolor, 15 );
        printf("\n");
    }
}

//--------------------------------------------------- ZADANIE_2
void dijkstra(int G[ILE][ILE], int odktorego)
{
    HANDLE kolor;
    kolor = GetStdHandle( STD_OUTPUT_HANDLE );

	int koszt[ILE][ILE], odleglosc_suma[ILE], trzym[ILE];          //trzym przechowuje porzedni wezel
	int odwiedzone[ILE], licz, dystans_min, nastepny, i, j;           //licz przechowuje liczbe wezlow

    //macierz kosztow
	for(i = 0; i < ILE; i++)
    {
        for(j = 0; j < ILE; j++)
        {
            if(G[i][j]==0)
            {
                koszt[i][j]=MAX;
            }
            else
            {
                koszt[i][j]=G[i][j];
            }
        }
    }

    //przygotuwujemy pod start
	for(i = 0; i < ILE; i++)
	{
		odleglosc_suma[i]=koszt[odktorego][i];
		trzym[i]=odktorego;
		odwiedzone[i]=0;
		//printf(" odleglosc=%d\n\n trzym=%d\n\n odwiedzone=%d\n\n\n",odleglosc_suma[i], trzym[i], odwiedzone[i]);
	}

	odleglosc_suma[odktorego]=0;
	odwiedzone[odktorego]=1;
	licz=1;

	while(licz<ILE-1)
	{
		dystans_min=MAX;

		//nastepny przekazuje wartosc do dystans_min
		for(i = 0; i < ILE; i++)
        {
            if(odleglosc_suma[i] < dystans_min && !odwiedzone[i])
			{
				dystans_min=odleglosc_suma[i];
				nastepny=i;
			}
        }
            //sprawdzenie czy jest lepsza droga krotsza
			odwiedzone[nastepny]=1;
			for(i = 0; i < ILE; i++)
            {
                //if(!odwiedzone[i])
					if(dystans_min+koszt[nastepny][i]<odleglosc_suma[i])
					{
						odleglosc_suma[i]=dystans_min+koszt[nastepny][i];
						trzym[i]=nastepny;
					}
            }
		licz++;
	}

    int ile_razy=0;
    int trzym2[100];
    int trzymodwrotnie[100];
    int x;
    int ostatni;

	//wypisuje najkrotsza droge z punktu zero do 9 i sume wag
	for(i=0;i<ILE;i++)
    {
		if(i!=odktorego)
		{
            SetConsoleTextAttribute( kolor, 11 );
		    printf("\n\nZ wierzcholka [%d] do wierzcholka [%d]:",odktorego, i);
		    SetConsoleTextAttribute( kolor, 14 );
			printf("\nSuma wag najkrotszej drogi wierzcholka [%d] wynosi: (%d)",i,odleglosc_suma[i]);
            SetConsoleTextAttribute( kolor, 10 );
			printf("\nNajkrotsza sciezka do wierzcholka [%d] z wierzcholka [%d] to: ", i, odktorego);

			j=i;
			do
			{

				j=trzym[j];
                trzym2[ile_razy]=j;
               // printf("--- [%d] ",j);
				ile_razy++;

			}while(j!=odktorego);
            x=ile_razy-1;
			//printf("\n%d\n",ile_razy);

                for(int o=0; o < ile_razy; o++)
                {
                    trzymodwrotnie[x]=trzym2[o];
                    x=x-1;
                }

				//printf("--- [%d] ",j);
                for(int l=0; l < ile_razy; l++)
                {
                    printf("[%d] ---> ",trzymodwrotnie[l]);
                }
                printf("[%d] ",i);
			ile_razy=0;
			SetConsoleTextAttribute( kolor, 15 );
        }
	}
}

//--------------------------------------------------- ZADANIE_3

int G[ILE][ILE],odwiedzone[ILE];
int liczDFS=0;

void DFS(int i)
{

    int j;
    if(liczDFS==ILE-1)
    {
        printf(" %d",i);
    }
    else
    {
        printf(" %d -->",i);
    }
    liczDFS++;

    odwiedzone[i]=1;
    for(j=0;j<ILE;j++)
    {
       if(!odwiedzone[j]&&G[i][j]==1)
       DFS(j);
    }
}

//--------------------------------------------------- ZADANIE_4


int kolejka[ILE_KOLEJKA];
int kolejka_1, kolejka_2;

void ustaw_kolejki(int x)
{
	kolejka[kolejka_2] = x;
	kolejka_2++;
}

int usun_kolejki()
{
	int ktory = kolejka_1;
	kolejka_1++;
	return kolejka[ktory];
}

void bfs(int Graf[ILE][ILE], int od_czego)
{
	int i, j;
    int licz=0;
	int odwiedzony[ILE];

	//koleja 1 poczatek 2 koniec
	kolejka_1 = 0;
	kolejka_2 = 0;

	//zerujewmy odwiedzone aby byly nieodwiedzone - 0
	for(i = 0; i < ILE; i++)
    {
		odwiedzony[i] = 0;
    }

    //poczatkowy wierzcholek odwiedzony z automatu
	odwiedzony[od_czego] = 1;

	//zapisz do kolejki jako dowiedzony
	ustaw_kolejki(od_czego);

	//wypisujemny pierwszy odwiedzony czyli poczatkowy startowy
	printf(" %d -->", od_czego);

	//dopoki kolejka nie bedzie pusta
	while(kolejka_1 <= kolejka_2)
    {
		//usuwamy pierwszy element z kolejki
		i = usun_kolejki();

		for(j = 0; j < ILE; j++)
        {
			if(odwiedzony[j] == 0 && Graf[i][j] == 1)
            {
				//zazanaczamy jako odwiedzony
				odwiedzony[j] = 1;
                licz++;
				ustaw_kolejki(j);

				//wyspisujemy wyniki
				if(licz==ILE-1)
                {
                   printf(" %d", j);
                }
                else
                {
                   printf(" %d -->", j);
                }
			}
		}
	}
	printf("\n");
}



int main()
{
    HANDLE kolor;
    kolor = GetStdHandle( STD_OUTPUT_HANDLE );
    SetConsoleTextAttribute( kolor, 15 );
    kolorki();

	int i,j;
	int od_ktorego=0;   //od ktorego wirzcholka zaczynamy DIKSTRE

	//                         0    1    2    3    4    5    6    7    8    9
    int Graf0[ILE][ILE] = {
                    /* 0 */   {0,   1,   0,   0,   0,   0,   0,   7,   0,   0}, //POLACZENIA 2

                    /* 1 */   {1,   0,   3,   0,   0,   0,   0,  18,   9,   0}, //POLACZENIA 4

                    /* 2 */   {0,   3,   0,   5,   0,   0,  28,   0,  10,  11}, //POLACZENIA 5

                    /* 3 */   {0,   0,   5,   0,  17,  38,   0,   0,   0,  12}, //POLACZENIA 4

                    /* 4 */   {0,   0,   0,  17,   0,  19,   0,   0,   0,   0}, //POLACZENIA 2

                    /* 5 */   {0,   0,   0,  38,  19,   0,  21,   0,   0,  24}, //POLACZENIA 4

                    /* 6 */   {0,   0,  28,   0,   0,  21,   0,  13,  14,  30}, //POLACZENIA 5

                    /* 7 */   {7,  18,   0,   0,   0,   0,  13,   0,  15,   0}, //POLACZENIA 4

                    /* 8 */   {0,   9,  10,   0,   0,   0,  14,  15,   0,   0}, //POLACZENIA 4

                    /* 9 */   {0,   0,  11,  12,   0,  24,  30,   0,   0,   0}  //POLACZENIA 4
                          };

    SetConsoleTextAttribute( kolor, 13 );
    printf("Zadanie 2 z kartki numer 6 oraz zadanie 1 z kartki numer 7\n\n\n");                                          // 2-6 1-7
    SetConsoleTextAttribute( kolor, 15 );

    wyswietl(Graf0);
    printf("\n");
    polaczenia(Graf0);
    SetConsoleTextAttribute( kolor, 14 );

    SetConsoleTextAttribute( kolor, 13 );
    printf("Zadanie 2 z kartki numer 7\n\n\n");                                                                // 2-7
    SetConsoleTextAttribute( kolor, 15 );

    printf("Dijkstra - nakrotsza sciezka od wierzcholka poczatkowego do pozostalych wierzcholkow:\n");
    SetConsoleTextAttribute( kolor, 15 );
	dijkstra(Graf0,od_ktorego);
    printf("\n");

    for(i=0;i<ILE;i++)
    {
        for(j=0;j<ILE;j++)
        {
            if(Graf0[i][j]==0)
            {
                G[i][j]=0;
            }
            else
            {
                G[i][j]=1;
            }
        }
    }
    //zerujemy
    for(i=0;i<ILE;i++)
    {
        odwiedzone[i]=0;
    }

    SetConsoleTextAttribute( kolor, 13 );
    printf("\n\nZadanie 1 z kartki numer 8\n");               // 1-8
    SetConsoleTextAttribute( kolor, 15 );

    SetConsoleTextAttribute( kolor, 14 );
    printf("\n\nPrzeszukiwanie w glab DFS:\n\n");
    SetConsoleTextAttribute( kolor, 15 );
    DFS(0);

    SetConsoleTextAttribute( kolor, 13 );
    printf("\n\n\nZadanie 2 z kartki numer 8\n");             // 2-8
    SetConsoleTextAttribute( kolor, 15 );

    SetConsoleTextAttribute( kolor, 14 );
    printf("\n\nPrzeszukiwanie wszerz BFS:\n\n");
    SetConsoleTextAttribute( kolor, 15 );

	int od_czego = 0; // wierzcholek poczatkowy

	bfs(G, od_czego);

    printf("\n\n");
	return 0;
}
