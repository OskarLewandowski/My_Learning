﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var krupier = new Rozdanie();
            krupier.Rozdaj();
            krupier.Wypisz();
            Console.Read();
        }
    }

    class Karta
    {
        private readonly string _nazwa;
        public string Nazwa
        {
            get
            {
                return _nazwa;
            }
        }

        public Karta(int indeks)
        {
            var kolor = indeks % 4;
            var figura = indeks % 13;

            switch (kolor)
            {
                case 0:
                    _nazwa = "Pik (\u2660)";
                    break;
                case 1:
                    _nazwa = "Kier (\u2665)";
                    break;
                case 2:
                    _nazwa = "Karo (\u2666)";
                    break;
                case 3:
                    _nazwa = "Trefl (\u2663)";
                    break;
            }
            _nazwa += " ";
            switch (figura)
            {
                case 12:
                    _nazwa += "As";
                    break;
                case 11:
                    _nazwa += "Król";
                    break;
                case 0:
                    _nazwa += "Dama";
                    break;
                case 1:
                    _nazwa += "Walet";
                    break;
                default:
                    _nazwa += figura.ToString();
                    break;
            }
        }
    }

    class Losowanie
    {
        public List<int> Losuj(int ileLiczb)
        {
            List<int> wynik = new List<int>();
            List<int> tmp = new List<int>();
 
            for (int i = 0; i < ileLiczb; i++)
            {
                tmp.Add(i);
            }

            for (int i = ileLiczb; i > 0; i--)
            {
                int losIndex = LosujZZakresu(0, i);
                int wylosowanaLiczba = tmp[losIndex];
                tmp.RemoveAt(losIndex);
                wynik.Add(wylosowanaLiczba);
            }
            return wynik;
        }

        public int LosujZZakresu(int min, int max)
        {
            //return min;
            var random = new Random();
            return random.Next(min, max);
        }
    }

    class Talia
    {
        private List<Karta> Karty { get; set; }

        public Talia()
        {
            Karty = new List<Karta>();
            for (int licznikKart = 0; licznikKart < 52; licznikKart++)
            {
                var karta = new Karta(licznikKart);
                DodajKarte(karta);
            }
        }

        public void Tasuj()
        {
            var losowanie = new Losowanie();
            List<int> wylosowane = losowanie.Losuj(Karty.Count);
            List<Karta> poLosowaniu = new List<Karta>();

            foreach (int los in wylosowane)
            {
                Karta losowaKarta = Karty[los];
                poLosowaniu.Add(losowaKarta);
            }
            Karty = poLosowaniu;
        }

        public Karta WezKarte()
        {
            Karta ostatnia = Karty[0];
            Karty.RemoveAt(0);
            return ostatnia;
        }

        private void DodajKarte(Karta karta)
        {
            Karty.Add(karta);
        }
    }

    class Rozdanie
    {
        private List<Gracz> ListaGraczy { get; set; }

        public Rozdanie()
        {        
            ListaGraczy = new List<Gracz>();
            for (int graczIndeks = 1; graczIndeks <= 4; graczIndeks++)
            {
                Gracz gracz = new Gracz(graczIndeks);
                ListaGraczy.Add(gracz);
            }
        }

        public void Rozdaj()
        {
            //Console.WriteLine("Tworze rozdanie");
            var talia = new Talia();
            talia.Tasuj();
        
            foreach (Gracz g in ListaGraczy)
            {
                for (int i = 0; i < 13; i++)
                {
                    Karta karta = talia.WezKarte();
                    g.DobierzKarte(karta);
                }
            }
        }

        public void Wypisz()
        {
            foreach (Gracz g in ListaGraczy)
            {
                g.WypiszReke();
            }
        }
    }

    class Gracz
    {
        private string Nazwa { get; set; }
        private List<Karta> Reka { get; set; }

        public Gracz(int indeks)
        {
            Reka = new List<Karta>();
            Nazwa = indeks.ToString();
        }

        public void DobierzKarte(Karta karta)
        {
            Reka.Add(karta);
        }

        public void WypiszReke()
        {
            Console.WriteLine(String.Format("\nReka gracza {0}. Ma kart {1}", Nazwa, Reka.Count));
            foreach (Karta karta in Reka)
            {
                Console.WriteLine(karta.Nazwa);
            }
        }
    }
}
