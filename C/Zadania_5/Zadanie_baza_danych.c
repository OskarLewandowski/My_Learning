#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <conio.h>
#include <string.h>
#define ILE 200

int main()
{
    //KOLOROWA SKLADNIA
    HANDLE kolor;
    kolor = GetStdHandle( STD_OUTPUT_HANDLE );

    // ZMIENNE [ S ]
    int plec[ILE];
    for(int i =0; i<ILE; i++)
    {
        plec[i]=3;
    }

    int AA=0, BB=0, CC=0, DD=0, EE=0, FF=0, GG=0, HH=0, II=0, JJ=0, KK=0, SS=0;
    int A=0, B=0, C=0, D=0, E=0, F=0, G=0, H=0, I=0, J=0, K=0;
    int zero=0;
    int tak=0;
    int nie=0;
    int wybor2;
    char ImiePrzechowaj[ILE][ILE];
    char NazwiskoPrzechowaj[ILE][ILE];
    char AdresPrzechowaj[ILE][ILE];
    char MiastoPrzechowaj[ILE][ILE];
    char TelefonPrzechowaj[ILE][ILE];
    char PeselPrzechowaj[ILE][ILE];
    char PlecPrzechowaj[ILE][ILE];
    char ZapiszPlec[50];
    char plecznak;
    int SPRpeselznak=0;
    int Liczplec=0, Liczmiasto=0, Licznazwisko=0, Liczimie=0;
    int Liczplec1=0, Liczmiasto1=0, Licznazwisko1=0, Liczimie1=0;
    int odzera=0;
    int licz=0;
    int wybor;
    int i;
    int ileosob=0;
    char imie[50];
    char nazwisko[50];
    char miasto[50];
    int plecZnak2;
    int suma=0, wynik=0;
    int x=0;
    // ZMIENNE [ K ]

    //POCZATEK PROGRAMU
    while(1)
    {
    // MENU GLOWNE [ S ]
    SetConsoleTextAttribute( kolor, 10 );                                   //KOLOR ZIELONY
    printf("Wpisz ( 1 ) aby dodac nowa osobe!\n");
    printf("Wpisz ( 2 ) aby wyszukac osobe podajac wybrane parametry!\n");
    printf("Wpisz ( 3 ) aby wyswietlic wszystkie wpisane osoby!\n");
    printf("Wpisz ( 4 ) aby wyczyscic okno!\n");
    printf("Wpisz ( 5 ) aby zakonczyc - WYJSCIE!\n");
    printf("\nCo chcesz zrobic wpisz odpowieni numer:");
    SetConsoleTextAttribute( kolor, 15 );                                   //KOLOR BIALY
    scanf("%d",&wybor);
    printf("\n");
    // MENU GLOWNE [ K ]

    //MENU WYBOR DEKLARACJA
switch(wybor)
	{

    case 1:
                                                                          //WYBOR 1 WPROWADZANIE DANYCH
    for(i=0 ;i<1 ;i++ )
    {
        SPRpeselznak=0;
        printf("Podaj pesel (11 cyfr): ");
        scanf("%s",&PeselPrzechowaj[odzera][i]);

        AA=PeselPrzechowaj[odzera][0] - '0';                                        //ASCII 0=48
        BB=PeselPrzechowaj[odzera][1] - '0';
        CC=PeselPrzechowaj[odzera][2] - '0';
        DD=PeselPrzechowaj[odzera][3] - '0';
        EE=PeselPrzechowaj[odzera][4] - '0';
        FF=PeselPrzechowaj[odzera][5] - '0';
        GG=PeselPrzechowaj[odzera][6] - '0';
        HH=PeselPrzechowaj[odzera][7] - '0';
        II=PeselPrzechowaj[odzera][8] - '0';
        JJ=PeselPrzechowaj[odzera][9] - '0';
        KK=PeselPrzechowaj[odzera][10] - '0';
        SS=PeselPrzechowaj[odzera][11];

        suma=0;
        wynik=0;

        suma=(1*AA)+(3*BB)+(7*CC)+(9*DD)+(1*EE)+(3*FF)+(7*GG)+(9*HH)+(1*II)+(3*JJ);
        wynik = 10 - (suma%10);

        if(wynik==KK)
        {                                                               //JESLI PRAWDZIWY PESEL [ S ]
            printf("Podany PESEL jest prawidlowy!\n");

        if (JJ % 2 == 1) //JJ==0 || JJ==2 || JJ==4 || JJ==6 || JJ==8
        {
            printf("Plec: Mezczyzna\n");
            plec[odzera]=1;          //mezczyzna 1
            PlecPrzechowaj[odzera][i]='m';
            //printf("Plec: %s",PlecPrzechowaj[i]);
        }
        else
        {
            printf("Plec: Kobieta\n"); //kobieta 0
            plec[odzera]=0 ;
            PlecPrzechowaj[odzera][i]='k';
            //printf("Plec: %s",PlecPrzechowaj[i]);
        }

        zero=0;
        tak=0;
        nie=0;

        for(int q = 0; q<ileosob; q++)
        {
            A=PeselPrzechowaj[zero][0] - '0'; //ASCII 0=48
            B=PeselPrzechowaj[zero][1] - '0';
            C=PeselPrzechowaj[zero][2] - '0';
            D=PeselPrzechowaj[zero][3] - '0';
            E=PeselPrzechowaj[zero][4] - '0';
            F=PeselPrzechowaj[zero][5] - '0';
            G=PeselPrzechowaj[zero][6] - '0';
            H=PeselPrzechowaj[zero][7] - '0';
            I=PeselPrzechowaj[zero][8] - '0';
            J=PeselPrzechowaj[zero][9] - '0';
            K=PeselPrzechowaj[zero][10] - '0';
            zero=zero+1;

            if(A==AA && B==BB && C==CC && D==DD && E==EE && F==FF && G==GG && H==HH && I==II && J==JJ && K==KK)
            {
                printf("\nW bazie znajduje sie juz osoba o takim numerze PESEL\n\n");
                plec[odzera]=2 ;         //COS 2
                PlecPrzechowaj[odzera][i]='c';
                SPRpeselznak=1;
                tak++;
            }
            else
            {
                nie++;
            }
        }
    }
    else
    {
        printf("Podany PESEL jest nieprawidlowy!\n");
        plec[odzera]=2 ;         //COS 2
        PlecPrzechowaj[odzera][i]='c';
        SPRpeselznak=1;
        break;
        //printf("Plec: %s",PlecPrzechowaj[i]); //kobieta 0
    }

    if(tak>0)
    {
        break;
    }

    printf("Podaj imie: ");
    scanf("%s",&ImiePrzechowaj[odzera][i]);

    printf("Podaj nazwisko: ");
    scanf("%s",&NazwiskoPrzechowaj[odzera][i]);

    printf("Podaj adres zamieszkania: ");
    scanf("%s",&AdresPrzechowaj[odzera][i]);

    printf("Podaj miasto zamieszkania: ");
    scanf("%s",&MiastoPrzechowaj[odzera][i]);

    printf("Podaj telefon (9 cyfr): ");
    scanf("%s",&TelefonPrzechowaj[odzera][i]);

}
    if(SPRpeselznak>0)
    {
        odzera=odzera;
        ileosob=ileosob;
    }
    else
    {
        odzera=odzera + 1;
        ileosob=ileosob + 1;
        printf("Osoba nr (%d)\n\n",ileosob);
    }

        break;

    case 2:                                                                                             //FILTROWANIE

        SetConsoleTextAttribute( kolor, 11 );                                                           //KOLOR NIEBIESKI

        printf("Wpisz ( 1 ) aby filtrowac osoby o podanym imieniu!\n");
        printf("Wpisz ( 2 ) aby filtrowac osoby o podanym nazwisku!\n");
        printf("Wpisz ( 3 ) aby filtrowac osoby o podanym miescie zamieszkania!\n");
        printf("Wpisz ( 4 ) aby filtrowac osoby o podanej plci!\n");
        printf("Wpisz ( 5 ) aby zakonczyc filtrowanie wyjscie do glownego menu!\n");
        printf("\nCo chcesz zrobic wpisz odpowieni numer:");
        SetConsoleTextAttribute( kolor, 15 );                                                           //KOLOR BIALY
        scanf("%d",&wybor2);
        //SZUKANIE PO IMIENIU
        if(wybor2==1)
        {
             Liczimie=0;
             Liczimie1=0;
             printf("Podaj imie do wyszukania: ");
             scanf("%s",&imie);

             for(int j = 0; j<ileosob; j++)
             {
                 if( stricmp( imie, ImiePrzechowaj[j] ) == 0 )
                 {
                    printf("\nOsoba nr (%d)\n",j+1);
                    printf("Imie: %s\n", ImiePrzechowaj[j]);
                    printf("Nazwisko: %s\n",NazwiskoPrzechowaj[j]);
                    printf("Adrees: %s\n",AdresPrzechowaj[j]);
                    printf("Miasto: %s\n",MiastoPrzechowaj[j]);
                    printf("Telefon: %s\n",TelefonPrzechowaj[j]);
                    printf("Pesel: %s\n",PeselPrzechowaj[j]);
                    printf("\n");
                    Liczimie1=Liczimie1+1;
                 }
                 else
                 {
                    Liczimie=Liczimie + 1;
                 }
             }

            if(Liczimie>=0 && Liczimie1<=0)
            {
                printf( "\nNie ma osoby o podanym kryterium (%s)\n\n",imie );
            }
        }
        //SZUKANIE PO NAZWISKU
        else if(wybor2==2)
        {
            Licznazwisko=0;
            Licznazwisko1=0;
            printf("Podaj nazwisko do wyszukania: ");
            scanf("%s",&nazwisko);

            for(int j = 0; j<ileosob; j++)
            {
                if( stricmp( nazwisko, NazwiskoPrzechowaj[j] ) == 0 )
                {
                    printf("\nOsoba nr (%d)\n",j+1);
                    printf("Imie: %s\n", ImiePrzechowaj[j]);
                    printf("Nazwisko: %s\n",NazwiskoPrzechowaj[j]);
                    printf("Adrees: %s\n",AdresPrzechowaj[j]);
                    printf("Miasto: %s\n",MiastoPrzechowaj[j]);
                    printf("Telefon: %s\n",TelefonPrzechowaj[j]);
                    printf("Pesel: %s\n",PeselPrzechowaj[j]);
                    printf("\n");
                    Licznazwisko1=Licznazwisko1+1;
                }
                else
                {
                    Licznazwisko=Licznazwisko+1;
                }
             }
            if(Licznazwisko>=0 && Licznazwisko1<=0)
            {
                printf( "\nNie ma osoby o podanym kryterium (%s)\n\n",nazwisko );
            }
        }
        // SZUKANIE PO MIESCIE
        else if(wybor2==3)
        {
            Liczmiasto=0;
            Liczmiasto1=0;
            printf("Podaj miasto do wyszukania: ");
            scanf("%s",&miasto);

            for(int j = 0; j<ileosob; j++)
            {
                if( stricmp( miasto, MiastoPrzechowaj[j] ) == 0 )
                {
                    printf("\nOsoba nr (%d)\n",j+1);
                    printf("Imie: %s\n", ImiePrzechowaj[j]);
                    printf("Nazwisko: %s\n",NazwiskoPrzechowaj[j]);
                    printf("Adrees: %s\n",AdresPrzechowaj[j]);
                    printf("Miasto: %s\n",MiastoPrzechowaj[j]);
                    printf("Telefon: %s\n",TelefonPrzechowaj[j]);
                    printf("Pesel: %s\n",PeselPrzechowaj[j]);
                    printf("\n");
                    Liczmiasto1=Liczmiasto1+1;
                }
                else
                {
                    Liczmiasto=Liczmiasto+1;
                }
             }
             if(Liczmiasto>=0 && Liczmiasto1<=0)
             {
                 printf( "\nNie ma osoby o podanym kryterium (%s)\n\n",miasto );
             }
        }
        //  SZUKANIE PO PLCI
        else if(wybor2==4)
        {
            Liczplec=0;
            Liczplec1=0;
            printf("Podaj plec do wyszukania wpisz ( m ) jesli mezczyzne lub ( k ) jesli kobiete: ");
            scanf("%s",&ZapiszPlec);

            for(int j = 0; j<ileosob; j++)
            {
                if( stricmp( ZapiszPlec, PlecPrzechowaj[j] ) == 0 )
                {
                    printf("\nOsoba nr (%d)\n",j+1);
                    printf("Imie: %s\n", ImiePrzechowaj[j]);
                    printf("Nazwisko: %s\n",NazwiskoPrzechowaj[j]);
                    printf("Adrees: %s\n",AdresPrzechowaj[j]);
                    printf("Miasto: %s\n",MiastoPrzechowaj[j]);
                    printf("Telefon: %s\n",TelefonPrzechowaj[j]);
                    printf("Pesel: %s\n",PeselPrzechowaj[j]);
                    printf("\n");
                    Liczplec1=Liczplec1+1;
                }
                else
                {
                    Liczplec=Liczplec+1;
                }
             }
             if(Liczplec>=0 && Liczplec1<=0)
             {
                printf( "\nNie ma osoby o podanym kryterium (%s)\n\n",ZapiszPlec );
             }
        }
        // ZAMKNIECIE FILTROWANIA
        else if(wybor2==5)
        {
        printf("Zamykanie opcji filtrowania...");
        Sleep(1000);
        system("cls");
        }
        // INNE POLECENIE
        else
        {
           printf("\nNie prawidlowe polecenie filtrowania! \n");
        }
        break;

    case 3:                                                                                     //WYSWIETLANIE WSZYSTKICH Z BAZY
            if(odzera==0)
            {
                printf("Brak osob [Baza jest pusta]\n\n");
            }
            else
            {
                x=0;
                for (int i = 0; i <ileosob; ++i)
                {
                    printf("\nOsoba nr (%d)\n",i+1);
                    printf("Imie: %s\n", ImiePrzechowaj[i]);
                    printf("Nazwisko: %s\n",NazwiskoPrzechowaj[i]);
                    printf("Adrees: %s\n",AdresPrzechowaj[i]);
                    printf("Miasto: %s\n",MiastoPrzechowaj[i]);
                    printf("Telefon: %s\n",TelefonPrzechowaj[i]);
                    printf("Pesel: %s\n",PeselPrzechowaj[i]);

                   if(PlecPrzechowaj[x][0]=='m')
                   {
                       printf("Plec: Mezczyzna\n");
                   }
                   else if(PlecPrzechowaj[x][0]=='k')
                   {
                       printf("Plec: Kobieta\n");
                   }
                    x++;
                    printf("\n");
                }
            }
        break;

    case 4:                                                                                        //CZYSC OKNO
        system("cls");
        break;
                                                                                                    //Zakonczenie dzialanie
    case 5:
        puts("Zakonczone dzialanie programu");
        exit(0);

        break;
                                                                                                    //NIEPRAWIDLOWE POLECENIE
    default:
        printf("\nNie prawidlowe polecenie! \n");
	}
}
    return 0;
}
