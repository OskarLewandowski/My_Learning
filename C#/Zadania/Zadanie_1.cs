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
            var silniaLiczba = 10;
            Console.WriteLine(silniaLiczba + "! = " + SilniaRekurencyjnie(silniaLiczba));
            Console.Read();
        }

        public static long SilniaRekurencyjnie(long dana)
        {
            if (dana <= 1)
            {
                return 1;
            }
            else
            {
                return dana * SilniaRekurencyjnie(dana - 1);
            }
        }
    }
}
