using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Zadanie_1
{
    class Program
    {
        static void Main(string[] args)
        {
            double wpisanyX1 = 0;
            double wpisanyX2 = 0;
            double przechowalnia = 0;

            const double a = 1;
            double b = 0;
            double c = 0;

            double zVietaB = 0;
            double zVietaC = 0;

            double sgn = 0;
            double optyWzoru = 0;
            double optyWzoruDelta = 0;

            double wyliczonyX1 = 0;
            double wyliczonyX2 = 0;

            double bladX1 = 0;
            double bladX2 = 0;
        
            try
            {
                Console.Write("Podaj pierwszy pierwiastek (X1): ");
                wpisanyX1 = double.Parse(Console.ReadLine());
            }
            catch (Exception e)
            {
                Console.WriteLine("Bledne dane!\nSprobuj ponownie:");
                wpisanyX1 = double.Parse(Console.ReadLine());
            }

            try
            {
                Console.Write("Podaj drugi pierwiastek (X2): ");
                wpisanyX2 = double.Parse(Console.ReadLine());
            }
            catch (Exception e)
            {
                Console.WriteLine("Bledne dane!\nSprobuj ponownie:");
                wpisanyX2 = double.Parse(Console.ReadLine());
            }
            
            if (wpisanyX1 > wpisanyX2)
            {
                przechowalnia = wpisanyX1;
                wpisanyX1 = wpisanyX2;
                wpisanyX2 = przechowalnia;
                Console.WriteLine("\nZamiana kolejnosci!\nWpisane pierwiastki:\nX1 = {0}\nX2 = {1}", wpisanyX1, wpisanyX2);
            }
            else
            {
                Console.WriteLine("\nWpisane pierwiastki:\nX1 = {0}\nX2 = {1}", wpisanyX1, wpisanyX2);
            }

            zVietaB = -1 * (wpisanyX1 + wpisanyX2);
            zVietaC = wpisanyX1 * wpisanyX2;

            b = zVietaB;
            c = zVietaC;
            //Console.WriteLine("\nWspolczynniki:\nA = {0}\nB = {1}\nC = {2}",a,b,c);

            //Obliczamy pierwiastki z https://pl.qwertyu.wiki/wiki/Loss_of_significance

            //Obliczamy funkcje znak
            if (b >= 0)
            {
                sgn = 1;
            }
            else
            {
                sgn = -1;
            }

            //Pierwiastki wyliczone
            optyWzoruDelta = Math.Sqrt((b * b) - 4 * a * c);
            optyWzoru = (-(b) - (sgn) * (optyWzoruDelta));

            wyliczonyX1 = optyWzoru / 2 * a;
            wyliczonyX2 = c / (a * wyliczonyX1);

            if (wyliczonyX1 > wyliczonyX2)
            {
                przechowalnia = wyliczonyX1;
                wyliczonyX1 = wyliczonyX2;
                wyliczonyX2 = przechowalnia;
                Console.WriteLine("\nZamiana kolejnosci!\nWyliczone pierwiastki:\nX1 = {0}\nX2 = {1}", wyliczonyX1, wyliczonyX2);
            }
            else
            {
                Console.WriteLine("\nWyliczone pierwiastki:\nX1 = {0}\nX2 = {1}", wyliczonyX1, wyliczonyX2);
            }

            bladX1 = ((wpisanyX1 - wyliczonyX1) / wpisanyX1);
            bladX2 = ((wpisanyX2 - wyliczonyX2) / wpisanyX2);

            Console.WriteLine("\nWyliczone bledy:");
            if(bladX1 >= 0 && bladX2 >= 0)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("X1 = {0}%\nX2 = {1}% ", (bladX1 / 1) * 100, (bladX2 / 1) * 100);
                Console.ForegroundColor = ConsoleColor.White;
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("X1 = {0}%\nX2 = {1}% ", (bladX1 / 1) * 100, (bladX2 / 1) * 100);
                Console.ForegroundColor = ConsoleColor.White;
            }

            Console.ReadKey();
        }
    }
}
