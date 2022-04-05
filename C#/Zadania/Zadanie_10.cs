using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Sprawozdanie_1
{
    /*kolejnosc wywolywania konstruktorow
     
      1] konstruktory klas bazowych w kolejności w jakiej są dziedziczone
      (na początku konstruktor klasy bazowej dla wszystkich pozostałych dziedziczących klas
      na końcu konstruktor naszej aktualnej klasy)
      2] konstruktory dla obiektów zadeklarowanych w ciele klasy
      3] konstruktor klasy
    */

    public class Program
    {
        public static void Main(String[] args)
        {         
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Pierwszy");
            Console.ForegroundColor = ConsoleColor.White;
            var sam = new Samochod(2000, "Opel",false,false,true);
            Console.WriteLine(sam.Napis());
            sam.Jedz();
            sam.Stoj();
            Console.WriteLine(sam.JakiJest());
            Console.WriteLine();

            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Drugi");
            Console.ForegroundColor = ConsoleColor.White;
            var sam2 = new Samochod();
            Console.WriteLine(sam2.Napis());
            sam2.Jedz();
            sam2.Stoj();
            Console.WriteLine(sam2.JakiJest()); 
            Console.WriteLine();

            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Trzeci");
            Console.ForegroundColor = ConsoleColor.White;
            var osobowy = new Osobowy(2004, "Gibbs Aquada", false,true,true);
            Console.WriteLine(osobowy.Napis());
            osobowy.IloscOsob = 3;
            osobowy.Jedz();
            osobowy.Stoj();
            osobowy.Plyn();
            Console.WriteLine(osobowy.IloscOsob);
            Console.WriteLine(osobowy.JakiJest());
            Console.WriteLine();

            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Czwarty");
            Console.ForegroundColor = ConsoleColor.White;
            var ciezarowy = new Ciezarowy(2011, "MAN",false,false,true);
            ciezarowy.Ladownosc = 50;
            Console.WriteLine(ciezarowy.Opis());
            Console.WriteLine(ciezarowy.JakiJest());
     
            Console.Read();
        }
    }

    class Pojazd
    {
        protected bool Wodny { get; set; }
        protected bool Powietrzny { get; set; }
        protected bool Ladowy { get; set; }

        public Pojazd()
        {
            Console.WriteLine("Konstruktor Pojazd #00 Pusty");
        }

        public Pojazd(bool wodny, bool powietrzny, bool ladowy)
        {
            Console.WriteLine("Konstruktor Pojazd #00");
            Wodny = wodny;
            Powietrzny = powietrzny;
            Ladowy = ladowy;
        }

        public string JakiJest()
        {
            return String.Format("Wodny: {0}, Powietrzny: {1}, Ladowy: {2}", Wodny, Powietrzny, Ladowy);
        }

        public void TestPojazd()
        {
            Console.WriteLine("Pojazd");
        }

        public void Jedz()
        {
            Console.WriteLine("Jedzie");
        }

        public void Stoj()
        {
            Console.WriteLine("Stoi");
        }

        public void Plyn()
        {
            Console.WriteLine("Plynie");
        }
        public void Lec()
        {
            Console.WriteLine("Lece");
        }
    }

    sealed class Statek : Pojazd
    {
        private int Wypornosc { get; set; }
        private int PredkoscMax { get; set; }

        public Statek(int wypornosc, int predkoscMax, bool wodny, bool powietrzny, bool ladowy) : base(wodny, powietrzny, ladowy) 
        {
            Wypornosc = wypornosc;
            PredkoscMax = predkoscMax;
        }
        public void TestStatek()
        {
            Console.WriteLine("Statek");
        }
    }

    //class Jacht : Statek
    //{
    //    public Jacht(int wypornosc, int predkoscMax) : base(wypornosc, predkoscMax)
    //    {

    //    }
    //}

    class Samochod : Pojazd
    {
        protected int Rocznik { get; set; }
        protected string Marka { get; set; }

        public Samochod()
        {
            Console.WriteLine("Konstruktor Samochod #01 Pusty");
        }

        public Samochod(bool wodny, bool powietrzny, bool ladowy) : base(wodny, powietrzny, ladowy)
        {
            Console.WriteLine("Konstruktor Samochod #01");
        }

        public Samochod(int rocznik, string marka, bool wodny, bool powietrzny, bool ladowy) : base(wodny, powietrzny, ladowy)
        {
            Console.WriteLine("Konstruktor Samochod #02");
            Rocznik = rocznik;
            Marka = marka;
        }     

        public string Napis()
        {
            return String.Format("Marka:{0}, Rocznik:{1}", Marka, Rocznik);
        }
    }

    class Osobowy : Samochod
    {
        public int IloscOsob { get; set; }

        public Osobowy(int rocznik, string marka, bool wodny, bool powietrzny, bool ladowy) : base(rocznik, marka, wodny, powietrzny, ladowy)
        {
            Console.WriteLine("Konstruktor Osobowy #03");
        }
    }

    class Ciezarowy : Samochod
    {
        public int Ladownosc { get; set; }

        public Ciezarowy(int rocznik, string marka, bool wodny, bool powietrzny, bool ladowy) : base(rocznik, marka, wodny, powietrzny, ladowy)
        {
            Console.WriteLine("Konstruktor Ciezarowy #04");
            Rocznik = rocznik;
            Marka = marka;
        }

        public string Opis()
        {
            return String.Format("Marka:{0}, Rocznik:{1}, Ładowność: {2} T", Marka, Rocznik, Ladownosc);
        }
    }
}
