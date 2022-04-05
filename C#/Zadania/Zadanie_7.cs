using System;
using System.Collections.Generic;
using System.Collections;

namespace Lekcja2
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Talia.Inicjuj();
            Console.Read();
        }

        class Talia
        {
            public static void Inicjuj()
            {
                // Generowanie talii
                Random random = new Random();
                List<Karta> talia = new List<Karta>();
                foreach (string figura in Karta.Figury)
                {
                    foreach (string kolor in Karta.Kolory)
                    {
                        talia.Add(new Karta(kolor, figura));
                    }
                }
                // Tasowanie talii
                List<Karta> taliaTasowana = new List<Karta>();

                while (talia.Count > 0)
                {
                    int i = random.Next(talia.Count);
                    taliaTasowana.Add(talia[i]);
                    talia.RemoveAt(i);
                }

                // Rozdawanie talii
                int iloscGraczy = 4;
                string[] imiona = new string[] { "North", "West", "South", "East" };
                Gracz[] gracze = new Gracz[iloscGraczy];
                for (int i = 0; i < iloscGraczy; i++)
                {
                    gracze[i] = new Gracz(imiona[i]);
                }
                int n = 0;
                while (n + iloscGraczy <= taliaTasowana.Count)
                {
                    for (int i = 0; i < iloscGraczy; i++)
                    {
                        gracze[i].Dodaj(taliaTasowana[n + i]);
                    }
                    n += iloscGraczy;
                }
                // Wyswietlanie kart poszczegolnych graczy
                foreach (Gracz gracz in gracze)
                {
                    Console.WriteLine(gracz);
                }
            }
        }

        // Klasa opisujaca pojedyncza karte
        class Karta
        {
            // Dostepne kolory oraz kody symboli w zapisie unicode
            public static string[] Kolory = new string[]
            {
              "Trefl(\u2663) ","Karo(\u2666) ","Kier(\u2665) ","Pik(\u2660) "
            };

            // Dostepne figury
            public static string[] Figury = new string[]
            {
                "As\n", "Król\n", "Dama\n", "Walet\n", "10\n", "9\n" ,"8\n", "7\n", "6\n", "5\n", "4\n", "3\n", "2\n"
            };

            // Kolor danej karty
            public string Kolor { get; set; }

            // Figura danej karty
            public string Figura { get; set; }

            // Konstruktor tworzacy nowa karte z figura danego koloru
            public Karta(string kolor, string figura)
            {
                Kolor = kolor;
                Figura = figura;
            }

            // Zwraca symbol karty
            public override string ToString()
            {
                return string.Format("\t{0}{1}", Kolor, Figura);
            }
        }

        // Klasa opisujaca gracza, obslugujaca ukladanie kart
        class Gracz : IComparer<Karta>
        {
            // Imie gracza
            public string Imie { get; set; }

            // Karty na reku gracza
            List<Karta> Karty;

            // Konstruktor tworzacy nowego gracza z okreslonym imieniem
            public Gracz(string imie)
            {
                Imie = imie;
                Karty = new List<Karta>();
            }

            // Dodanie graczowi karty
            public void Dodaj(Karta karta)
            {
                Karty.Add(karta);
            }

            // Ulozenie i wyswietlenie kart
            public override string ToString()
            {
                Karty.Sort(this);
                string karty = "";
                foreach (Karta karta in Karty)
                {
                    karty += karta + "";
                }
                return string.Format("{0}:\n{1}", Imie, karty);
            }

            // Algorytm ukladania kart; karty wedlug koloru, a jak rowne to wedlug figury rosnaco
            public int Compare(Karta x, Karta y)
            {
                int porownanieKolorow = -x.Kolor.CompareTo(y.Kolor);
                if (porownanieKolorow != 0)
                {
                    return porownanieKolorow;
                }
                int porownanieFigur = x.Figura.CompareTo(y.Figura);
                return porownanieFigur;
            }
        }
    }
}