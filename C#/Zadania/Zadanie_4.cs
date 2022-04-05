using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lekcja01
{
    class Program
    {
        public static void Main(string[] args)
        {
            Employee Pracownik001 = new Employee();

            Pracownik001.imie = "Jan";
            Pracownik001.nazwisko = "Kowalski";
            Pracownik001.stanowisko = "ABC";
            Pracownik001.wiek = 37;
            Pracownik001.latPracy = 7;

            Pracownik001.InformacjaOPracowniku();
            Pracownik001.Pracuj();
            Pracownik001.Przerwa();
            Pracownik001.Awans();
            Pracownik001.Degradacja();


            Console.Read();
        }

        public class Employee
        {
            public string imie;
            public string nazwisko;
            public string stanowisko;
            public int wiek;
            public int latPracy;
            
            public void InformacjaOPracowniku()
            {
                Console.WriteLine("Imie: " + imie + "\nNazwisko: " + nazwisko + "\nWiek: " + wiek + "\nLat pracy: " + latPracy + "\nStanowisko: "+ stanowisko);
            }

            public void Pracuj()
            {
                Console.WriteLine("Pracuje");
            }

            public void Przerwa()
            {
                Console.WriteLine("Czas na przerwe");
            }

            public void Awans()
            {
                Console.WriteLine("\nAwansujesz na wyższe stanowsiko.\nZapraszam do biura.\nSzef");
            }

             public void Degradacja()
            {
                Console.WriteLine("\nZostajesz zdegradowany na niższe stanowisko.\nZapraszam do biura.\nSzef");
            }
        }

    }
}
