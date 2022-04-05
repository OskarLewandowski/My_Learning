using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lekcja02
{
    class Program
    {
        public static void Main(string[] args)
        {
            Employee pracownik = new Employee();

            //SET INFORAMCJE_O_PRACOWNIKU
            pracownik.setImie("Jan");
            pracownik.setNazwisko("Kowalski");
            pracownik.setStanowisko("ABC");
            pracownik.setWiek(37);
            pracownik.setLatPracy(7);

            Console.WriteLine("GET:");
            Console.WriteLine("Imie: " + pracownik.getImie());
            Console.WriteLine("Nazwisko: " + pracownik.getNazwisko());
            Console.WriteLine("Stanowisko: " + pracownik.getStanowisko());
            Console.WriteLine("Wiek: " + pracownik.getWiek());
            Console.WriteLine("Lat pracy: " + pracownik.getLatPracy());

            Console.WriteLine("\nMETODA:");
            pracownik.KonwertujNaNapis();

            Console.Read();
        }

        public class Employee
        {
            private string imie;
            private string nazwisko;
            private string stanowisko;
            private int wiek;
            private int latPracy;

            //METODA KONWERTUJ_NA_NAPIS
            public void KonwertujNaNapis()
            {
                Console.WriteLine("Imie: {0}\nNazwisko: {1}\nStanowisko: {2}",this.imie,this.nazwisko,this.stanowisko);
                Console.WriteLine("Wiek: {0}\nLat pracy: {1}",this.wiek, this.latPracy);
            }
            //SET IMIE
            public void setImie(string wartoscImie)
            {
                imie = wartoscImie;
            }
            //GET IMIE
            public string getImie()
            {
                return imie;
            }
            //SET NAZWISKO
            public void setNazwisko(string wartoscNazwisko)
            {
                nazwisko = wartoscNazwisko;
            }
            //GET NAZWISKO
            public string getNazwisko()
            {
                return nazwisko;
            }
            //SET STANOWISKO
            public void setStanowisko(string wartoscStanowisko)
            {
                stanowisko = wartoscStanowisko;
            }
            //GET STANOWISKO
            public string getStanowisko()
            {
                return stanowisko;
            }
            //SET WIEK
            public void setWiek(int wartoscWiek)
            {
                wiek = wartoscWiek;
            }
            //GET WIEK
            public int getWiek()
            {
                return wiek;
            }
            //SET LAT_PRACY
            public void setLatPracy(int wartoscLatPracy)
            {
                latPracy = wartoscLatPracy;
            }
            //GET LATPRACY
            public int getLatPracy()
            {
                return latPracy;
            }
        }
    }
}