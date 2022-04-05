using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace Lekcja01
{
    class Program
    {
        public static void Main(string[] args)
        {
            decimal dana = 2000000000;
            var miernik = new System.Diagnostics.Stopwatch();
            miernik.Start();
            decimal suma = Suma(dana);
            miernik.Stop();
            string wiadomosc = String.Format("Suma {0} liczb wynosi: {1} Czas: {2}.", dana, suma, miernik.Elapsed);
            Console.WriteLine(wiadomosc);
            Console.Read();
        }

        public static decimal Suma(decimal limit)
        {
            decimal suma = ((1 + limit) / 2) * limit;
            return suma;
        }
    }
}

