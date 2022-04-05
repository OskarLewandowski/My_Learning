
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Sprawozdanie_3
{
    public class Program
    {
        public static void Main(String[] args)
        {
            //var sam = new Samochod(2000, "Opel");
            //Console.WriteLine(sam.ToString());
            //sam.Jedz();
            //sam.Stoj();
            //sam.Rocznik = 1999;
            //sam.Marka = "O";


            //var osobowy = new Osobowy(1999, "BMW");
            //osobowy.IloscOsob = 5;
            //Console.WriteLine(osobowy);
            //osobowy.Jedz();
            //osobowy.Stoj();
            //Console.WriteLine(osobowy.IloscOsob);

            Osobowy testKonstruktor = new Osobowy(5, 2019, "Dodge");
            Console.WriteLine(testKonstruktor.ToString());

            //Osobowy testKonstruktor2 = new Osobowy(2,2019, "Dodge");
            //Console.WriteLine(testKonstruktor2.ToString());
            //testKonstruktor2.IloscOsob = 4;
            //Console.WriteLine(testKonstruktor2.ToString());

            Console.Read();
        }


    }

    class Pojazd
    {
    }

    class Statek : Pojazd
    {
    }

    class Samochod : Pojazd
    {
        private int Rocznik { get; set; }
        private string Marka { get; set; }

        public Samochod()
        {
        }

        public Samochod(int rocznik, string marka)
        {
            Rocznik = rocznik;
            Marka = marka;
        }

        public virtual void Jedz()
        {
            Console.WriteLine("Jedzie");
        }

        public void Stoj()
        {
            Console.WriteLine("Stoi");
        }

        public override string ToString()
        {
            return String.Format("Marka:{0}, Rocznik:{1}", Marka, Rocznik);
        }

    }

    class Osobowy : Samochod
    {
        public int IloscOsob { get; set; }

        //konstruktor ustawia ilosc osob
        public Osobowy(int iloscosob, int rocznik, string marka) : base(rocznik, marka)
        {
            IloscOsob = iloscosob;
        }

        public Osobowy(int rocznik, string marka) : base(rocznik, marka)
        {
        }
        
        public override void Jedz()
        {
            base.Jedz();
            Console.WriteLine("Osobowy");
        }

        public override string ToString()
        {
            return String.Format("{0}, IloscOsob:{1}", base.ToString(), IloscOsob);
        }
    }

    class Ciezarowy : object 
    {
        public int Ladownosc { get; set; }
    }
}
