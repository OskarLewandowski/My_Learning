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
            //Ścieżka do pliku                                     \/
            string path = @"C:\Users\Oskar\Desktop\Graf_planarny\graf0.gxl";
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
                //Console.WriteLine("+ Znaleziono {0} wierzchołków", ileW);
                //Console.WriteLine("+ Znaleziono {0} krawędzi", ileK);
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

            int fromTempINT = 0;
            int toTempINT = 0;

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
                                
                                if (ile == 3)
                                {
                                    //Console.WriteLine(idTemp);
                                    //Console.WriteLine(fromTemp);
                                    //Console.WriteLine(toTemp);
                                    ile = 0;

                                    fromTempINT = int.Parse(fromTemp);
                                    toTempINT = int.Parse(toTemp);


                                    tablica[fromTempINT, toTempINT] = 1;
                                    tablica[toTempINT, fromTempINT] = 1;
                                }
                            }

                            Console.WriteLine();
                            break;
                    }
                }
            }

            //Wyswietlanie macierzy przyległosci
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


            //Zadanie_2 Do sprawdzenia czy graf jest planarny wykorzystam twierdzenie Eulera
            //http://home.agh.edu.pl/~zobmat/2017/2_tarkowskijakub/teoria/planarnosc.php

            int M = ileK; //krawedzie
            int N = ileW; //wierzcholki
            int F = M + 2 - N; //sciany

            //Console.WriteLine("\nIlość wierzchołków = {0} ", N);
            //Console.WriteLine("Ilość krawędzi = {0} ", M);
            //Console.WriteLine("Ilość ścian = {0} ", F);

            int Lewa = N - M + F;
            int Prawa = 2;

            //Console.WriteLine("Lewa strona = {0}\nPrawa strona = {1}", Lewa, Prawa);

            if (Lewa == Prawa && N >=3 && M <= (3*N)-6 && M <=(2*N)-4)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("\nGraf jest planarny");
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("\nGraf nie jest planarny");
            }
            Console.ReadKey();
        }
    }
}
