using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Projekt_1
{
    class Program
    {
        public static List<int> licznik = new List<int>();
        public static List<int> mianownik = new List<int>();

        public static List<double> dzielnikiWyrazuWolnego = new List<double>();
        public static List<double> dzielnikiWyrazuNajPotegi = new List<double>();

        public static List<double> pierwiastkiWartosci = new List<double>();
        public static List<double> pierwiastkiWartosciSort = new List<double>();
    
        public static List<string> pierwastkiWymierneZPow = new List<string>();
        public static List<string> test1String = new List<string>();
      
        public static List<double> test1double = new List<double>();
        public static List<double> test2double = new List<double>();
        public static List<double> test3double = new List<double>();
        public static List<double> test4double = new List<double>();
        public static List<double> test5double = new List<double>();

        public static List<double> ulamkiWym1 = new List<double>();
        public static List<double> ulamkiWym2 = new List<double>();
        public static List<double> ulamkiWym3 = new List<double>();

        public static List<double> ulamkiWymGora = new List<double>();
        public static List<double> ulamkiWymDol = new List<double>();

        public static List<string> ulamkiWymSort = new List<string>();
        public static List<string> ulamkiWymSortPro = new List<string>();

        public static List<int> pierwiastkiGotowe = new List<int>();

        public static int potegaMax = 0;
        public static int box = 0;

        public static int wyrazWolny = 0;
        public static int wyrazNajPotega = 0;
        public static int wyrazWolnyILE = 0;
        public static int wyrazNajPotegaILE = 0;
        public static int ileWyrazow = 0;
        public static int wyrazNajPotegaClear = 0;
        public static int wyrazWolnyClear = 0;
        public static int hornerWynik = 0;

        //Start
        static void Main(string[] args)
        {
            linia();
            wczytanie();
            linia();
            wypisanieRownania();
            linia();
            dzilnikiWolnyPotega();
            pierwiastkiWielomianu();
            linia();
            pierwiastkiWymierne();  
            linia();
            sprawdzPierwiastki();
            linia();
            startHorner();
            linia();
            krotnosci();
            linia();

            //stat();
            //statusA();
            //status();
            Console.ReadLine();
        }

        /// <summary>
        /// Wczytuje wartosci rowanania
        /// </summary>
        public static void wczytanie()
        {
            Console.Write("Podaj najwyzsza wartosc potegi: ");
            kolor("zolty");
            potegaMax = int.Parse(Console.ReadLine());
            kolor("bialy");

            for (int i = potegaMax; i >= 0; i--)
            {
                if (i == 0)
                {
                    Console.Write("Podaj wspolczynnik dla wyrazu wolnego: ");
                    kolor("zolty");
                    box = int.Parse(Console.ReadLine());
                    kolor("bialy");
                    wyrazWolny = box;
                    licznik.Add(box);
                }
                else
                {
                    Console.Write("Podaj wspolczynnik dla x^{0}: ", i);
                    kolor("zolty");
                    box = int.Parse(Console.ReadLine());
                    kolor("bialy");
                    licznik.Add(box);
                }
            }
            wyrazNajPotega = licznik[0];

            if (wyrazNajPotega < 0)
            {
                wyrazNajPotegaClear = wyrazNajPotega * (-1);
            }
            else
            {
                wyrazNajPotegaClear = wyrazNajPotega;
            }

            if(wyrazWolny<0)
            {
                wyrazWolnyClear = wyrazWolny * (-1);
            }
            else
            {
                wyrazWolnyClear = wyrazWolny;
            }
        }

        /// <summary>
        /// Wypisuje rownanie z podannymi wartosciami z x
        /// </summary>
        public static void wypisanieRownania()
        {
            int j = 0;
            Console.Write("Rownanie: ");
            kolor("niebieski2");
            for (int i = potegaMax; i >= 0; i--)
            {
                if (i == 0)
                {
                    Console.Write("({0}) = 0\n", licznik[j]);
                }
                else
                {
                    Console.Write("({0}x^{1}) + ", licznik[j], i);
                    j++;
                }
            }
            kolor("bialy");
        }

        /// <summary>
        /// Wylicza dzilenniki wyrazu wolnego
        /// </summary>
        public static void dzielnikiWyrazWolny()
        {
            int boxD = 0;
            for (int i = 1; i <= wyrazWolnyClear; i++)
            {
                if (wyrazWolnyClear % i == 0)
                {
                    dzielnikiWyrazuWolnego.Add(i);
                    boxD = i * (-1);
                    dzielnikiWyrazuWolnego.Add(boxD);
                    //Console.WriteLine(i);
                }
            }
            dzielnikiWyrazuWolnego.Sort();
            wyrazWolnyILE = dzielnikiWyrazuWolnego.Count();
            //dzielnikiWyrazuWolnegoSort = dzielnikiWyrazuWolnego.Distinct().ToList();
        }

        /// <summary>
        /// Wylicza dzilelniki najwyzszej potegi
        /// </summary>
        public static void dzielnikiWyrazNajwiekszejPotegi()
        {
            int boxD = 0;
            for (int i = 1; i <= wyrazNajPotegaClear; i++)
            {
                if (wyrazNajPotegaClear % i == 0)
                {
                    dzielnikiWyrazuNajPotegi.Add(i);
                    boxD = i * (-1);
                    dzielnikiWyrazuNajPotegi.Add(boxD);
                    //Console.WriteLine(i);
                }
            }
            dzielnikiWyrazuNajPotegi.Sort();
            wyrazNajPotegaILE = dzielnikiWyrazuNajPotegi.Count();
            //dzielnikiWyrazuNajPotegiSort = dzielnikiWyrazuNajPotegi.Distinct().ToList();
        }

        /// <summary>
        /// Liczy dzielniki oraz sortuje i usuwa duplikaty zapisujac do nowej listy
        /// </summary>
        public static void  dzilnikiWolnyPotega()
        {
            dzielnikiWyrazWolny();
            dzielnikiWyrazNajwiekszejPotegi();
            ileWyrazow = wyrazWolnyILE * wyrazNajPotegaILE;
        }

        /// <summary>
        /// Wypisuje wszystkie prawdopodobne piwerwiastki z powtorzeniami
        /// </summary>
        public static void pierwiastkiWielomianu()
        {
            int licznik = 0;
            double boxP = 0;
            string ciagA = "";
            string ciagB = "";
            string lacznik = "";

            Console.WriteLine("Wszystkie prawdopodobne pierwiastki z powtorzeniami:\n");
            //wszystkie
            for (int i = 0; i < wyrazWolnyILE; i++)
            {

                for (int j = 0; j < wyrazNajPotegaILE; j++)
                {
                    licznik++;
                    boxP = dzielnikiWyrazuWolnego[i] / dzielnikiWyrazuNajPotegi[j];

                    ciagA = dzielnikiWyrazuWolnego[i].ToString();
                    ciagB = dzielnikiWyrazuNajPotegi[j].ToString();
                    lacznik = "(" + ciagA + "/" + ciagB + ")";
                    kolor("szary1");
                    Console.WriteLine("{0,11}",lacznik);
                    kolor("bialy");
                    pierwastkiWymierneZPow.Add(lacznik);
                    pierwiastkiWartosci.Add(boxP);

                    // Console.Write("({0}/{1}) ", dzielnikiWyrazuWolnego[i], dzielnikiWyrazuNajPotegi[j]);
                    kolor("niebieski0");
                    Console.WriteLine("{0,9}", dzielnikiWyrazuWolnego[i]);
                    kolor("rozowy");
                    Console.WriteLine("     -------");
                    kolor("niebieski0");
                    Console.WriteLine("{0,9}\n", dzielnikiWyrazuNajPotegi[j]);   
                    kolor("bialy");
                }
            }
            pierwastkiWymierneZPow.Sort();
            pierwiastkiWartosci.Sort();
            pierwiastkiWartosciSort = pierwiastkiWartosci.Distinct().ToList();
        }

        /// <summary>
        /// Wypisuje mozliwe pierwiastki bez powtorzen  
        /// </summary>
        public static void pierwiastkiWymierne()
        {
  
            double boxitem = 0;
            bool gotowe = false;
            string ciagA = "";
            string ciagB = "";
            string lacznik = "";
            int licznik = 0;

            Console.WriteLine("Prawdopodobne pierwiastki bez powtorzen:\n");

            for (int i = 0; i < pierwiastkiWartosciSort.Count; i++)
            {
                boxitem = pierwiastkiWartosciSort[i];
                while(gotowe==false)
                {
                    for (int j = 0; j < wyrazWolnyILE; j++)
                    {
                        for (int k = 0; k < wyrazNajPotegaILE; k++)
                        {
                            if(boxitem == (dzielnikiWyrazuWolnego[j] / dzielnikiWyrazuNajPotegi[k]) && gotowe==false)
                            {
                                //Console.WriteLine("{0}/{1}", dzielnikiWyrazuNajPotegi[k], dzielnikiWyrazuNajPotegi[k]);
                                
                                ciagA = dzielnikiWyrazuWolnego[j].ToString();
                                ciagB = dzielnikiWyrazuNajPotegi[k].ToString();
                                lacznik = "(" + ciagA + "/" + ciagB + ")";
                                ulamkiWymSort.Add(lacznik);
                                ulamkiWymGora.Add(dzielnikiWyrazuWolnego[j]);
                                ulamkiWymDol.Add(dzielnikiWyrazuNajPotegi[k]);
                                gotowe = true;
                            }
                        }
                    }
                }
                gotowe = false;
              //  Console.WriteLine(boxitem);
            }

            ulamkiWymSortPro = ulamkiWymSort.Distinct().ToList();

            for (int i = 0; i < ulamkiWymSortPro.Count; i++)
            {
                licznik++;
                kolor("szary1");
                Console.WriteLine("{0,9}", ulamkiWymSort[i]);
                kolor("niebieski0");
                Console.WriteLine("{0,11}", ulamkiWymGora[i]);
                kolor("rozowy");
                Console.WriteLine("{0,3}) = -------", licznik);
                kolor("niebieski0");
                Console.WriteLine("{0,11}\n", ulamkiWymDol[i]);
                kolor("bialy");
            }
        }

        /// <summary>
        /// Podstawiamy pierwiastki do wzory w celu sprawdzenia czy pierwiastek jest razwiazaniem wielomianu
        /// </summary>
        public static void sprawdzPierwiastki()
        {
            double konwertDOU = 0;
            string konwertSTR = "";
            int konwertINT = 0;

            double liczydlo = 0;
            double temp = 0;
            double box = 0;
            double potega = potegaMax;
            int ile = 0;

            for (int i = 0; i < pierwiastkiWartosciSort.Count; i++)
            {
                Console.WriteLine("Pierwiastek nr. " + (i+1));
                for (int j = 0; j < potegaMax; j++)
                {
                    temp = ((licznik[j]) * (Math.Pow(pierwiastkiWartosciSort[ile], potega)));

                    //Console.WriteLine("!!!KONTROLA!!!\n licznik:{0} pier:{1} pot:{2}", licznik[j], pierwiastkiWartosciSort[ile],potega);

                    box = box + temp;

                    if(j==potegaMax-1)
                    {
                        liczydlo = box + wyrazWolny;
                        kolor("szary1");
                        Console.Write("({0}/{1}) ", ulamkiWymGora[i], ulamkiWymDol[i]);
                        kolor("bialy");
                        // Console.WriteLine("wynik {0}",liczydlo);
                        if (liczydlo == 0)
                        {
                            kolor("zielony");
                            Console.WriteLine("Jest pierwiastkiem wielomianu Reszta 0");
                            kolor("bialy");
                            konwertDOU = Math.Round(ulamkiWymGora[i] / ulamkiWymDol[i],0);
                            konwertSTR = konwertDOU.ToString();
                            konwertINT = int.Parse(konwertSTR);
                            pierwiastkiGotowe.Add(konwertINT);
           
                        }
                        else
                        {
                            kolor("czerwony");
                            Console.WriteLine("Nie jest pierwiastkiem wielomianu Reszta: {0}", Math.Round(liczydlo, 0));
                            kolor("bialy");
                        }
                    }
                    else
                    {
                        potega--;
                       // Console.WriteLine(box);
                    }                
                }
                temp = 0;
                box = 0;
                liczydlo = 0;

                potega = potegaMax;
                ile++;
            }
        }

        /// <summary>
        /// Podaje krotnosci wielomianu
        /// </summary>
        public static void krotnosci()
        {
            int j = 0;
            Console.WriteLine("Krotnosci:");
            for (int i = potegaMax; i >= 0; i--)
            {
                if (i == 0)
                {
                    //Console.Write("Dla ({0}) krotność wynosi: {1}\n", licznik[j], i);
                }
                else
                {
                    Console.Write("Dla ");
                    kolor("szary1");
                    Console.Write("({0}x^{1})", licznik[j], i);
                    kolor("bialy");
                    Console.Write(" krotność wynosi: ");
                    kolor("zielony");
                    Console.WriteLine("{0}",i);
                    kolor("bialy");
                    j++;
                }
            }
        }

        /// <summary>
        /// Kontrola1
        /// </summary>
        public static void status()
        {
            Console.WriteLine("P");
            foreach (var item in dzielnikiWyrazuWolnego)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("Q");
            foreach (var item in dzielnikiWyrazuNajPotegi)
            {
                Console.WriteLine(item);
            }
        }
      
        /// <summary>
        /// Kontrola2
        /// </summary>
        public static void stat()
        {
            foreach (var item in pierwiastkiWartosciSort)
            {
                Console.WriteLine(item);
            }
        }

        /// <summary>
        /// Algorytm Hornera 3
        /// </summary>
        /// <param name="tab"></param>
        /// <param name="n"></param>
        /// <param name="x"></param>
        /// <returns></returns>
        public static int horner(int[] tab, int n, int x)
        {
            int wynik = tab[0];

            for (int i = 1; i < n; i++)
            {
                wynik = wynik * x + tab[i];
            }
            hornerWynik = wynik;
            return hornerWynik;
        }

        /// <summary>
        /// Algorytm Hornera 2
        /// </summary>
        public static void liczymyHornerem(int xx)
        {
            int k = licznik.Count;
            int[] tablica = new int[k];
            for (int i = 0; i < k; i++)
            {
                tablica[i] = licznik[i];
            }
            int x = xx; 
            int n = tablica.Length;

            wypisanieRownania();
            horner(tablica, n, x);
            kolor("zielony");
            Console.Write("Rownanie mozna wyliczyc dla x = {0}\n",x);
            kolor("bialy");
            wypisanieRownaniaLiczba(x);
            Console.WriteLine();
        }

        /// <summary>
        /// Start Horner 1
        /// </summary>
        public static void startHorner()
        {
            int co = 0;
            if(pierwiastkiGotowe.Count==0)
            {
                kolor("czerwony");
                Console.WriteLine("Wielomian nie ma rozwiazania!");
                kolor("bialy");
            }
            else
            {
                for (int i = 0; i < pierwiastkiGotowe.Count; i++)
                {
                    co = pierwiastkiGotowe[i];
                    liczymyHornerem(co);
                }
            }       
        }

        /// <summary>
        /// Wypisuje rownanie z pierwiastkiem tego wielomianu
        /// </summary>
        /// <param name="ile"></param>
        public static void wypisanieRownaniaLiczba(int ile)
        {
            //wypisanie rownania
            int x = ile;
            int j = 0;
            Console.Write("Rownanie: ");
            kolor("niebieski2");
            for (int i = potegaMax; i >= 0; i--)
            {
                if (i == 0)
                {
                    Console.Write("({0}) = 0\n", licznik[j]);
                }
                else
                {
                    Console.Write("({0}*({1}^{2})) + ", licznik[j],x, i);
                    j++;
                }
            }
            kolor("bialy");
        }

        /// <summary>
        /// Wyswietla linie w celu odzielenia, przejrzystosci
        /// </summary>
        public static void linia()
        {
            kolor("niebieski1");
            Console.WriteLine("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n");
            kolor("bialy");
        }

        /// <summary>
        /// Kolorki po polsku niebieskix = od 0 do 3 szaryx od 0 do 1
        /// </summary>
        /// <param name="kolor"></param>
        public static void kolor(string kolor)
        {
            string jakiKolor = kolor;
            switch (jakiKolor)
            {
                case "bialy":
                    {
                        Console.ForegroundColor = ConsoleColor.White;
                        break;
                    }
                case "czerwony":
                    {
                        Console.ForegroundColor = ConsoleColor.DarkRed;
                        break;
                    }
                case "zielony":
                    {
                        Console.ForegroundColor = ConsoleColor.Green;
                        break;
                    }
                case "zolty":
                    {
                        Console.ForegroundColor = ConsoleColor.DarkYellow;
                        break;
                    }
                case "niebieski0":
                    {
                        Console.ForegroundColor = ConsoleColor.Blue;
                        break;
                    }
                case "rozowy":
                    {
                        Console.ForegroundColor = ConsoleColor.Magenta;
                        break;
                    }
                case "szary0":
                    {
                        Console.ForegroundColor = ConsoleColor.Gray;
                        break;
                    }
                case "niebieski1":
                    {
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        break;
                    }
                case "niebieski2":
                    {
                        Console.ForegroundColor = ConsoleColor.DarkCyan;
                        break;
                    }
                case "niebieski3":
                    {
                        Console.ForegroundColor = ConsoleColor.DarkBlue;
                        break;
                    }
                case "szary1":
                    {
                        Console.ForegroundColor = ConsoleColor.DarkGray;
                        break;
                    }
                default:
                    {
                        Console.ForegroundColor = ConsoleColor.White;
                        break;
                    }
            }
        }
    }
}


//SMIECI


//https://www.matmana6.pl/pierwiastki-wymierne-wielomianu-o-wspolczynnikach-calkowitych






          //                  Console.WriteLine("Jest pierwiastkiem wielomianu, Wynik: {0}", Math.Round(liczydlo, 0));
/* 
 *  if(licznik==0)
                    {
                        boxBezP = dzielnikiWyrazuWolnego[i] / dzielnikiWyrazuNajPotegi[j];
                        test1double.Add(dzielnikiWyrazuWolnego[i]);
                        test2double.Add(dzielnikiWyrazuNajPotegi[j]);

                        test3double.Add(boxBezP);
                    }
                    else
                    {
                        boxBezP = dzielnikiWyrazuWolnego[i] / dzielnikiWyrazuNajPotegi[j];
                        for (int k = 0; k < test3double.Count; k++)
                        {
                            if (boxBezP == test3double[k])
                            {
                                Console.WriteLine("POWTORKA");
                            }
                            else
                            {
                       
                                test1double.Add(dzielnikiWyrazuWolnego[i]);
                                test2double.Add(dzielnikiWyrazuNajPotegi[j]);

                                test3double.Add(boxBezP);
                            }
                        }
                    }
                    

                    Console.WriteLine(boxBezP);
                    licznik++;
 * 
 * 
 * 
      public static void statusA()
        {
            for (int i = 0; i < test4double.Count; i++)
            {
                for (int j = 0; j < test5double.Count; j++)
                {
                    Console.Write("({0}/{1}) ", test4double[i], test5double[j]);
                }
            }
        }


         public static void statusA()
        {
            for (int i = 0; i < test3double.Count; i++)
            {
                for (int j = 0; j < test4double.Count; j++)
                {
                    Console.Write("({0}/{1}) ", test3double[i], test4double[j]);
                }
            }
        }



              for (int k = 0; k < licznik2; k++)
                    {
                        if (boxP == pierwiastkiWartosci[k])
                        {
                            //Console.WriteLine("NiC");
                        }
                        else if(boxP != pierwiastkiWartosci[k])
                        {

                            ciagC = dzielnikiWyrazuWolnego[i].ToString();
                            ciagD = dzielnikiWyrazuNajPotegi[j].ToString();
                            lacznik2 = "(" + ciagA + "/" + ciagB + ")";
                            test1String.Add(lacznik2);

                            Console.WriteLine(lacznik2);
                        }
                        else
                        {
                            //Console.WriteLine("Nic");

                        }

                        
                    }
                    licznik2++;

    
       pierwiastkiBezP[0, 0] = 1;
            pierwiastkiBezP[0, 1] = 2;



            for (int i = 0; i < pierwiastkiBezP.GetLength(0); i++)
            {
                for (int j = 0; j < pierwiastkiBezP.GetLength(1); j++)
                {
                    Console.Write("\t" + pierwiastkiBezP[i, j] + " ");
                }
                Console.WriteLine();
            }

    
    public static List<int> dzielnikiWyrazuWolnegoSort = new List<int>();
       public static List<int> dzielnikiWyrazuNajPotegiSort = new List<int>();



public static void ulamek()
{

   // mianownik

   for (int i = potegaMax; i >= 0; i--)
   {
       if (i == 0)
       {
           box = 1;
           mianownik.Add(box);

       }
       else
       {
           box = i * -1;
           mianownik.Add(box);
       }
       //Console.WriteLine("ILER : {0} box {1} ",i,box);
   }
}

public static void wypiszUlamki()
{
   for (int i = 0; i < potegaMax; i++)
   {
       Console.WriteLine("({0}/{1})", licznik[i], mianownik[i]);
   }
}



public static void obliczaniePierwiastkow()
{

}







      public static void pierwiastkiWielomianuBezP()
        {
            double boxBezP = 0;
          //  int licznik = 0;
            Console.WriteLine("SHOWTIME!!!!");

            for (int i = 0; i < wyrazWolnyILE; i++)
            {
                for (int j = 0; j < wyrazNajPotegaILE; j++)
                {
                    boxBezP = dzielnikiWyrazuWolnego[i] / dzielnikiWyrazuNajPotegi[j];
                    test3double.Add(boxBezP);
                    Console.WriteLine(boxBezP);
                    for (int k = 0; k < test3double.Count; k++)
                    {
                        if(boxBezP==test3double[k])
                        {
                            
                        }
                        else if (boxBezP != test3double[k])
                        {
                            test1double.Add(dzielnikiWyrazuWolnego[i]);
                            test2double.Add(dzielnikiWyrazuNajPotegi[j]);
                        }
                        else
                        {

                        }
                    }

                }
            }

            double smallBox = 0;

            Console.WriteLine("Test CCCCCCCCCC");

            for (int i = 0; i < test1double.Count; i++)
            {
                smallBox = test1double[i] / test2double[i];

                if (i == 0)
                {
                    ulamkiWym1.Add(smallBox);
                    Console.WriteLine("TYLKO RAZ");
                }

                for (int j = 0; j < ulamkiWym1.Count; j++)
                {
                    if(smallBox==ulamkiWym1[j])
                    {

                    }
                    else
                    {
                        ulamkiWym2.Add(test1double[i]);
                        ulamkiWym3.Add(test2double[i]);
                    }


                }


                if (i != 0)
                {
                    ulamkiWym1.Add(smallBox);
                    Console.WriteLine("Gdy nie Zero RAZ");

                }

                Console.WriteLine(smallBox);
            }

            string ciagA = "";
            string ciagB = "";
            string lacznik = "";


            for (int i = 0; i < ulamkiWym2.Count; i++)
            {
                ciagA = ulamkiWym2[i].ToString();
                ciagB = ulamkiWym3[i].ToString();

                lacznik = "(" + ciagA + "/" + ciagB + ")";
                ulamkiWymSort.Add(lacznik);
            }

            ulamkiWymSort.Sort();
            ulamkiWymSortPro = ulamkiWymSort.Distinct().ToList();

            foreach (var item in ulamkiWymSortPro)
            {
                Console.WriteLine(item);
            }
        }



   */
