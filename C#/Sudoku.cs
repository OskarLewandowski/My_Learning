using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Sudoku
{
    class Program
    {
        static void Main(string[] args)
        {
            int ileGier = 1;
            while (true)
            {
                NowaGra sudoku = new NowaGra();

                if (ileGier == 1)
                {
                    sudoku.Powitanie();
                    sudoku.WyborGry();
                    Console.WriteLine("To twoja {0} runda!", ileGier);
                }
                else
                {
                    Thread.Sleep(250);
                    sudoku.WyborGry();
                    Console.WriteLine("To twoja {0} runda!", ileGier);
                }
                ileGier++;
            }
        }
    }

    /// <summary>
    /// Zawiera metody dotyczące tworzenia, edytowania, rozwiązywania siatki Sudoku
    /// </summary>
    class Siatka
    {
        public int PoleX { get; private set; }
        public int PoleY { get; private set; }
        public int WartoscPola { get; private set; }
        public string Przechowaj { get; private set; }

        //Domyślna siatka
        private int[,] siatkaStart = new int[9, 9]
        {
            {5,3,0,0,7,0,0,0,0},
            {6,0,0,1,9,5,0,0,0},
            {0,9,8,0,0,0,0,6,0},
            {8,0,0,0,6,0,0,0,3},
            {4,0,0,8,0,3,0,0,1},
            {7,0,0,0,2,0,0,0,6},
            {0,6,0,0,0,0,2,8,0},
            {0,0,0,4,1,9,0,0,5},
            {0,0,0,0,8,0,0,7,9}
        };

        /// <summary>
        /// Wyzerowanie zawartości siatkaStart
        /// </summary>
        public void CzyscSiatke()
        {
            for (int i = 0; i < siatkaStart.GetLength(0); i++)
            {
                for (int j = 0; j < siatkaStart.GetLength(1); j++)
                {
                    siatkaStart[i, j] = 0;
                }
            }
        }
        /// <summary>
        /// Zapisuje wprowadzone zmiany w siatkaStart na podanym X - PoleX oraz Y - PoleY oraz wartość pola - WartoscPola
        /// </summary>
        /// <param name="PoleX"></param>
        /// <param name="PoleY"></param>
        /// <param name="WartoscPola"></param>
        public void WypelnijSiatke(int PoleX, int PoleY, int WartoscPola)
        {
            this.PoleX = PoleX;
            this.PoleY = PoleY;
            this.WartoscPola = WartoscPola;
            siatkaStart[PoleX, PoleY] = WartoscPola;
        }
        /// <summary>
        /// Rysuje zformatowaną siatkę z zapisanym wartościami
        /// </summary>
        public void Rysuj()
        {
            int liczDlugosc = 0;
            int liczWysokosc = 0;
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.WriteLine("------------ SUDOKU ------------");
            Console.ForegroundColor = ConsoleColor.White;
            for (int PoleX = 0; PoleX < siatkaStart.GetLength(0); PoleX++)
            {
                liczWysokosc++;
                for (int PoleY = 0; PoleY < siatkaStart.GetLength(1); PoleY++)
                {
                    liczDlugosc++;
                    if (liczDlugosc == 1)
                    {
                        Console.ForegroundColor = ConsoleColor.DarkGreen;
                        Console.Write(" | ");
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        Console.Write(siatkaStart[PoleX, PoleY] + " ");
                        Console.ForegroundColor = ConsoleColor.White;
                    }
                    else if (liczDlugosc == 3)
                    {
                        Console.ForegroundColor = ConsoleColor.Cyan;
                        Console.Write(siatkaStart[PoleX, PoleY]);
                        Console.ForegroundColor = ConsoleColor.DarkGreen;
                        Console.Write(" | ");
                        Console.ForegroundColor = ConsoleColor.White;
                        liczDlugosc = 0;
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.White;
                        Console.Write(siatkaStart[PoleX, PoleY] + " ");
                    }
                }
                if (liczWysokosc == 3)
                {
                    Console.WriteLine("\n");
                    liczWysokosc = 0;
                }
                else
                {
                    Console.WriteLine();
                }
            }
        }

        /// <summary>
        /// Mozliwosć ręcznego uzupełnienia siatkaStart
        /// </summary>
        public void UstawZawartoscSiatki()
        {
            bool czyDobrze = true;
            for (int poleX = 0; poleX < siatkaStart.GetLength(0); poleX++)
            {
                for (int poleY = 0; poleY < siatkaStart.GetLength(1); poleY++)
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("W pola do wyliczenia wprowadz '0'\nPozostale uzupelnij 1-9\nAby wyjść wpisz 'q'\nAby cofnąć wpisz 'e'");
                    Console.ForegroundColor = ConsoleColor.White;
                    Console.Write("Podaj wartość dla pola [{0},{1}]: ", poleX, poleY);
                    Przechowaj = Console.ReadLine();
                    Console.Clear();
                    if (Przechowaj == "q")
                    {
                        System.Environment.Exit(0);
                    }
                    else if (Przechowaj == "e")
                    {
                        Console.WriteLine("Cofniecie...");
                        if (poleX != 0 && poleY == 0)
                        {
                            poleX = poleX - 1;
                            poleY = 7;
                        }
                        else if (poleY < 1)
                        {
                            poleY = 0;
                        }
                        else
                        {
                            poleY = poleY - 2;
                        }
                    }
                    else
                    {
                        try
                        {
                            WartoscPola = int.Parse(Przechowaj);
                        }
                        catch (Exception e)
                        {
                            if (poleY <= 0)
                            {
                                czyDobrze = false;
                                Console.WriteLine(e.Message);
                            }
                            else
                            {
                                czyDobrze = true;
                                poleY = poleY - 1;
                                Console.WriteLine(e.Message);
                            }
                        }
                        finally
                        {
                            if (WartoscPola <= 9)
                            {
                                WypelnijSiatke(poleX, poleY, WartoscPola);
                            }
                            else if (WartoscPola > 9)
                            {
                                poleY = poleY - 1;
                                Console.WriteLine("Wprowadzona niedozwoloną wartość - {0}", WartoscPola);
                            }
                            else
                            {
                                Console.WriteLine("Stan został zapisany...");
                            }
                        }
                    }
                    if (czyDobrze == false)
                    {
                        poleY = -1;
                        Console.WriteLine("Nie można rozpoznać polecenia - '{0}'!\nSpróbuj ponownie:", Przechowaj);
                    }
                    czyDobrze = true;
                    Rysuj();
                }
            }
        }

        //Do Rozwiaz
        private bool MoznaWstawic(int poleX, int poleY, int wartosc)
        {
            for (int i = 0; i < 9; i++)
            {
                if (wartosc == siatkaStart[poleX, i] || wartosc == siatkaStart[i, poleY] ||
                    wartosc == siatkaStart[poleX / 3 * 3 + i % 3, poleY / 3 * 3 + i / 3])
                {
                    return false;
                }
            }
            return true;
        }

        //Do Rozwiaz
        private bool Nastepny(int poleX, int poleY)
        {
            if (poleX == 8 && poleY == 8)
            {
                return true;
            }
            else if (poleX == 8)
            {
                return Rozwiazanie(0, poleY + 1);
            }
            else
            {
                return Rozwiazanie(poleX + 1, poleY);
            }
        }

        //Do Rozwiaz
        private bool Rozwiazanie(int x, int y)
        {
            if (siatkaStart[x, y] == 0)
            {
                for (int i = 1; i <= 9; i++)
                {
                    if (MoznaWstawic(x, y, i))
                    {
                        siatkaStart[x, y] = i;
                        if (Nastepny(x, y)) return true;
                    }
                }
                siatkaStart[x, y] = 0; return false;
            }
            return Nastepny(x, y);
        }

        /// <summary>
        /// Rozwiazuje siatkę oraz rysuje uzupełniną siatkę 
        /// </summary>
        public void Rozwiaz()
        {
            if (Rozwiazanie(0, 0))
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("Da sie rozwiązać...");
                Console.ForegroundColor = ConsoleColor.White;
                Rysuj();
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Niemożliwe do rozwiązania!!!");
                Console.ForegroundColor = ConsoleColor.White;
            }
        }
    }

    /// <summary>
    /// Menu głowne
    /// </summary>
    class NowaGra : Siatka
    {
        /// <summary>
        /// Informacja powitalna o rozpoczęciu gry
        /// </summary>
        public void Powitanie()
        {
            Console.WriteLine("Witaj!");
            Thread.Sleep(1000);
            Console.WriteLine("Oto przed tobą najwspanialsza gra Świata Sudoku!\n");
            Thread.Sleep(1500);
            //Console.Clear();
        }
        /// <summary>
        /// Menu wyboru
        /// </summary>
        public void WyborGry()
        {
            string wybor;
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Wybierz Proszę opcję która Ciebie najbardziej interesuje:");
            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("--------------------------------------------------");
            Console.ForegroundColor = ConsoleColor.DarkCyan;
            Console.WriteLine("Wpisz '1' aby wybrać domyślną plansze.");
            Console.WriteLine("Wpisz '2' aby stworzyć własną plansze.");
            Console.WriteLine("Wpisz '3' aby wyczyścić okno konsoli");
            Console.WriteLine("Wpisz '4' aby wyjść z gry.");
            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("--------------------------------------------------");
            Console.ForegroundColor = ConsoleColor.White;
            Console.Write("Twój wybór: ");

            wybor = Console.ReadLine();

            Siatka nowagra = new Siatka();
            switch (wybor)
            {
                case "1":
                    {
                        Console.WriteLine("Wybrałeś domyślną planszę.");
                        nowagra.Rysuj();
                        nowagra.Rozwiaz();
                        break;
                    }
                case "2":
                    {
                        Console.WriteLine("Wybrałeś stworzenie własnej planszy.");
                        nowagra.CzyscSiatke();
                        nowagra.Rysuj();
                        nowagra.UstawZawartoscSiatki();
                        nowagra.Rozwiaz();
                        break;
                    }
                case "3":
                    {
                        Console.Clear();
                        break;
                    }
                case "4":
                    {
                        Console.Clear();
                        Console.WriteLine("Dziękuję za gre!");
                        Thread.Sleep(1500);
                        System.Environment.Exit(0);
                        break;
                    }
                default:
                    {
                        Console.WriteLine("Niestety nie ma takiej opcji!\nSpróbuj ponownie!");
                        break;
                    }
            }
        }
    }
}
