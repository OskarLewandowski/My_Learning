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
            int dana = 200;
            var miernik = new System.Diagnostics.Stopwatch();
            miernik.Start();
            int suma = Suma(dana);
            miernik.Stop();
            string wiadomosc = String.Format("Suma {0} liczb parzystych wynosi: {1} Czas: {2}.", dana, suma, miernik.Elapsed);
            Console.WriteLine(wiadomosc);
            Console.Read();
        }

        public static int Suma(int limit)
        {
            int suma = 0;
            int skladnik = limit;
            int licznik = 0;            
            for(licznik = 0; licznik < limit; licznik +=2)
            {
                suma += skladnik;         
                skladnik -= 2;
            }
            return suma;
        }
    }
}
