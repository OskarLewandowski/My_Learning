using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using System.Threading;
using System.Xml;
using static System.Net.Mime.MediaTypeNames;

namespace Zadanie_2
{
    class Program
    {
        static void Main(string[] args)
        {
            //Ścieżka do pliku
            string path = @"C:\Users\Oskar\Desktop\Zadanie_2\miasta.gxl";
            int ileW = 0;
            int ileK = 0;
            string box = "";
            List<string> nazwy = new List<string>();
            //Czytanie pliku
            try
            {
                XmlTextReader czytaj = new XmlTextReader(path);

                while (czytaj.Read())
                {
                    if (czytaj.Name == "edge" || czytaj.Name == "node")
                    {
                        switch (czytaj.NodeType)
                        {
                            case XmlNodeType.Element:

                                if (czytaj.Name == "node")
                                {
                                    czytaj.MoveToNextAttribute(); //atrybut 2
                                    czytaj.MoveToNextAttribute(); //atrybut 3
                                    box = czytaj.Value;
                                    nazwy.Add(box);
                                    ileW++;
                                }
                                else
                                {
                                    ileK++;
                                }
                                break;
                        }
                    }
                }
                Console.WriteLine("+ Znaleziono {0} wierzchołków", ileW);
                Console.WriteLine("+ Znaleziono {0} krawędzi", ileK);
                // Console.WriteLine("+ Znaleziono {0} połączeń", ileK);            

            }
            catch (Exception e)
            {
                Console.WriteLine("Nie udało się wczytać pliku!");
                Console.WriteLine(e.Message);
                Thread.Sleep(2000);
            }

            Console.WriteLine("\nWczytyanie danych do tablicy przyległości...\n");
            Thread.Sleep(500);
            XmlTextReader wczytaj = new XmlTextReader(path);
            int[,] tablica = new int[ileW, ileW];

            int ile = 0;
            string idTemp = "";
            string fromTemp = "";
            string toTemp = "";
            string weightTemp = "";

            int fromTempINT = 0;
            int toTempINT = 0;
            int weightTempINT = 0;

            //Wczytanie danych do tablicy
            while (wczytaj.Read())
            {
                if (wczytaj.Name == "edge")
                {
                    switch (wczytaj.NodeType)
                    {
                        case XmlNodeType.Element:
                            //  Console.Write("<" + wczytaj.Name + ">");
                            while (wczytaj.MoveToNextAttribute())
                            {
                                // Console.Write(" " + wczytaj.Name + "='" + wczytaj.Value + "'");

                                if (ile == 0)
                                {
                                    idTemp = wczytaj.Value;
                                    ile++;
                                    //Console.WriteLine("1");
                                }
                                else if (ile == 1)
                                {
                                    fromTemp = wczytaj.Value;
                                    ile++;
                                    //Console.WriteLine("2");
                                }
                                else if (ile == 2)
                                {
                                    toTemp = wczytaj.Value;
                                    ile++;
                                    //Console.WriteLine("3");
                                }
                                else if (ile == 3)
                                {
                                    weightTemp = wczytaj.Value;
                                    ile++;
                                    //Console.WriteLine("3");
                                }


                                if (ile == 4)
                                {
                                    //Console.WriteLine(idTemp);
                                    //Console.WriteLine(fromTemp);
                                    //Console.WriteLine(toTemp);
                                    ile = 0;

                                    fromTempINT = int.Parse(fromTemp);
                                    toTempINT = int.Parse(toTemp);
                                    weightTempINT = int.Parse(weightTemp);

                                    tablica[fromTempINT, toTempINT] = weightTempINT;
                                    tablica[toTempINT, fromTempINT] = weightTempINT;
                                }
                            }

                            Console.WriteLine();
                            break;
                    }
                }
            }

            //Wyswietlanie macierzy
            Console.Clear();
            Console.WriteLine("\t\t\t<---------MACIERZ PRZYLEGŁOŚCIE--------->");

            Console.WriteLine("------------------------------------------------------------------------------------");
            for (int i = 0; i < tablica.GetLength(0); i++)
            {
                Console.Write("\t[{0}]", i);
            }
            Console.WriteLine();

            for (int i = 0; i < tablica.GetLength(0); i++)
            {
                Console.Write("[{0}]", i);
                for (int j = 0; j < tablica.GetLength(1); j++)
                {
                    if (tablica[i, j] == 0)
                    {
                        Console.Write("\t{0,2}", "-");
                    }
                    else
                    {
                        Console.Write("\t{0,2}", tablica[i, j]);
                    }
                }
                Console.WriteLine();
            }
            Console.WriteLine("------------------------------------------------------------------------------------\n");

            //Wypisanie opisu macierzy
            int l = 0;
            Console.WriteLine("LEGENDA:");
            foreach (var item in nazwy)
            {
                Console.WriteLine(item + " = [{0}]", l);
                l++;
            }

            //CZESC 2

            int odktorego = 0;
            int doktorego = 0;

            Console.Write("\nPodaj numer miejscowości startowej (0-{0}):", ileW - 1);
            odktorego = int.Parse(Console.ReadLine());
            Console.WriteLine("Wybrano {0}\n", nazwy[odktorego]);
            Console.Write("Podaj numer miejscowości końcowej (0-{0}):", ileW - 1);
            doktorego = int.Parse(Console.ReadLine());
            Console.WriteLine("Wybrano {0}\n", nazwy[doktorego]);

            //dikstra
            int[,] koszt = new int[ileW, ileW];
            int[] odleglosc_suma = new int[ileW];
            int[] trzym = new int[ileW];  //przechowuje porzedni wezel
            int[] odwiedzone = new int[ileW];  //przechowuje porzedni wezel
            int licz = 0; //przechowuje liczbe wezlow
            int dystans_min = 0;
            int nastepny = 0;
            int MAX = 9999;

            //macierz kosztow
            for (int i = 0; i < ileW; i++)
            {
                for (int j = 0; j < ileW; j++)
                {
                    if (tablica[i, j] == 0)
                    {
                        koszt[i, j] = MAX;
                    }
                    else
                    {
                        koszt[i, j] = tablica[i, j];
                    }
                }
            }

            //przygotuwujemy pod start
            for (int i = 0; i < ileW; i++)
            {
                odleglosc_suma[i] = koszt[odktorego, i];
                trzym[i] = odktorego;
                odwiedzone[i] = 0;
            }

            odleglosc_suma[odktorego] = 0;
            odwiedzone[odktorego] = 1;
            licz = 1;

            while (licz < ileW - 1)
            {
                dystans_min = MAX;

                //nastepny przekazuje wartosc do dystans_min
                for (int i = 0; i < ileW; i++)
                {
                    if (odleglosc_suma[i] < dystans_min && odwiedzone[i] == 0)
                    {
                        dystans_min = odleglosc_suma[i];
                        nastepny = i;
                    }
                }

                //sprawdzenie czy jest lepsza droga krotsza
                odwiedzone[nastepny] = 1;
                for (int i = 0; i < ileW; i++)
                {
                    //if(!odwiedzone[i])
                    if (dystans_min + koszt[nastepny,i] < odleglosc_suma[i])
                    {
                        odleglosc_suma[i] = dystans_min + koszt[nastepny,i];
                        trzym[i] = nastepny;
                    }
                }
                licz++;
            }

            int ile_razy = 0;
            int[] trzym2 = new int[ileW*ileW];
            int[] trzymodwrotnie = new int[ileW*ileW];
            int x;
            int y;

            //wypisuje najkrotsza droge z punktu zero do 9 i sume wag
            for (int i = 0; i < ileW; i++)
            {
                if (i != odktorego && i == doktorego)
                {

                    Console.WriteLine("Z {0} do {1}:", nazwy[odktorego], nazwy[i]);
                    Console.WriteLine("Suma km najkrotszej drogi wynosi: {0}km",odleglosc_suma[i]);
                    Console.WriteLine("Najkrotsza droga do {0} z {1} to: ", nazwy[i], nazwy[odktorego]);

                    y = i;
                    do
                    {

                        y = trzym[y];
                        trzym2[ile_razy] = y;
                        ile_razy++;

                    } while (y != odktorego);
                    x = ile_razy - 1;

                    for (int o = 0; o < ile_razy; o++)
                    {
                        trzymodwrotnie[x] = trzym2[o];
                        x = x - 1;
                    }

                    for (int k = 0; k < ile_razy; k++)
                    {
                        Console.Write("{0} ---> ", nazwy[trzymodwrotnie[k]]);
                    }
                    Console.Write("{0}\n\n", nazwy[i]);
                    ile_razy = 0;
                }
            }
            Console.ReadKey();
        }
    }
}
