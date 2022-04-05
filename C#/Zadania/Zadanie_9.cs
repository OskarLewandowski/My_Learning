using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Rextester
{
    public class Program
    {
        public static void Main(String[] args)
        {
            var liczbaX1 = 3;
            var liczbaY1 = 2.5;
            double liczbaX2 = -4, liczbaY2 = 5;
            double sumaX, sumaY;
            double wynikX = 5, wynikY = 1;

            Dodaj(liczbaX1, liczbaY1, liczbaX2, liczbaY2, out sumaX, out sumaY);
            Console.WriteLine(String.Format("[{0},{1}] + [{2},{3}] = [{4},{5}]", liczbaX1, liczbaY1, liczbaX2, liczbaY2, sumaX, sumaY));
            bool rowne = CzyRowne(sumaX, liczbaY2, wynikY, wynikX);
            Console.WriteLine(String.Format("[{0},{1}] == [{2},{3}] = {4}", sumaX, liczbaY2, wynikY, wynikX, rowne));

            var p1 = new Parametry(3, 2.5);
            var p2 = new Parametry(-4, 5);
            var p3 = p1.Dodaj(p2);

            var p4 = new Parametry(sumaX, liczbaY2);
            var p5 = new Parametry(wynikY, wynikX);
            bool rowne2 = p4.Rowne(p5);
 
            Console.WriteLine(String.Format("{0} + {1} = {2}", p1.KonwertujNaNapis(), p2.KonwertujNaNapis(), p3.KonwertujNaNapis()));
            Console.WriteLine(String.Format("[{0},{1}] == [{2},{3}] = {4}", sumaX, liczbaY2, wynikY, wynikX, rowne2));

            Console.WriteLine(String.Format("{0} == {1} = {2}", p1.KonwertujNaNapis(), p2.KonwertujNaNapis(), p1.Rowne(p2)));
            Console.WriteLine(String.Format("{0} == {1} = {2}", p1.KonwertujNaNapis(), p1.KonwertujNaNapis(), p1.Rowne(p1)));

            Console.Read();
        }

        private static void Dodaj(double a1, double b1, double a2, double b2, out double a3, out double b3)
        {
            a3 = a1 + a2;
            b3 = b1 + b2;
        }

        private static bool CzyRowne(double a1, double b1, double a2, double b2)
        {
            return a1 == a2 && b1 == b2;
        }
    }

    class Parametry
    {
        public double X { get; private set; }
        public double Y { get; private set; }

        public Parametry(double x, double y)
        {
            X = x;
            Y = y;
        }

        public Parametry Dodaj(Parametry nowy)
        {
            var wynik = new Parametry(X + nowy.X, Y + nowy.Y);
            return wynik;
        }

        public string KonwertujNaNapis()
        {
            return String.Format("[{0};{1}]", X, Y);
        }

        public bool Rowne(Parametry nowe)
        {
            bool wynik = (X == nowe.X)&&(Y == nowe.Y);
            //Console.WriteLine("\n[{0},{1}] == [{2},{3}] = {4}\n", X, Y, nowe.X, nowe.Y, wynik);
            return wynik;
        }
    }
}
