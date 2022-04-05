
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Sprawozdanie_2
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

            //var osobowy2 = new Osobowy(5, 1997, "Toyota");
            //Console.WriteLine(osobowy2);


            //Samochod.Marka” jest niedostępny z powodu swojego poziomu ochrony
            //Samochod.Rocznik” jest niedostępny z powodu swojego poziomu ochrony

            Osobowy testWnuk = new Osobowy(2007, "Opel");
            Console.WriteLine("Przed " + testWnuk.ToString());

            testWnuk.Marka = "Dodge";
            testWnuk.Rocznik = 2018;
            testWnuk.IloscOsob = 5;

            Console.WriteLine("Po " + testWnuk.ToString());
            Console.Read();
        }


    }
    //pradziadek pojazd
    class Pojazd
    {
    }

    //class Statek : Pojazd
    //{
    //}

    //Dziadek samochod
    class Samochod : Pojazd
    {
        //pola protected 
        protected int Rocznik { get; set; }
        protected string Marka { get; set; }

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
    //wnuk osobowy dziadka samochod
    class Osobowy : Samochod
    {
        public int IloscOsob { get; set; }

        public Osobowy(int iloscosob, int rocznik, string marka) : base(rocznik, marka)
        {
                
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

    //class Ciezarowy
    //{
    //    public int Ladownosc { get; set; }
    //}

}
