using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Zycie
{
    class Program
    {
        static void Main(string[] args)
        {
            int ile = 0;
            Zwierzeta gra = new Zwierzeta();
            gra.NowaPlansza();
            gra.umiescLwy();
            gra.umiescKrokodyle();
            gra.umiescSlonie();
            gra.umiescAntylopy();
            gra.Rysuj();
            while (ile <= 9)
            {
                gra.Tura();
                gra.Rysuj();
                //Thread.Sleep(2000);
                ile++;
            }
            Console.ReadKey();
        }
    }

    class Zwierzeta : Plansza
    {
        public int LosoweX { get; set; }
        public int LosoweY { get; set; }

        public void LosujPolozenie()
        {
            Random losuj = new Random();
            int poleX = losuj.Next(0, WymiarPlanszyX());
            int poleY = losuj.Next(0, WymiarPlanszyY());
            //Console.WriteLine("X: {0} Y:{1}",poleX,poleY);
            LosoweX = poleX;
            LosoweY = poleY;
            //Console.WriteLine("X: {0} Y:{1}", LosoweX, LosoweY);
        }

        public void umiescLwy()
        {
            bool jestDobrze = true;
            string lewOn = "L";
            string lewOna = "l";
            bool dwaLwy = false;

            LosujPolozenie();

            while (jestDobrze == true)
            {

                if (CzyMozna(LosoweX, LosoweY) == false)
                {
                    if (dwaLwy == false)
                    {
                        PlanszaZmiana(LosoweX, LosoweY, lewOn);
                        dwaLwy = true;
                    }
                    else if (dwaLwy == true)
                    {
                        PlanszaZmiana(LosoweX, LosoweY, lewOna);
                        jestDobrze = false;
                    }
                }
                else
                {
                    LosujPolozenie();
                }
            }
        }

        public void umiescKrokodyle()
        {
            bool jestDobrze = true;
            string krokodylOn = "K";
            string krokodylOna = "k";
            bool dwaLwy = false;

            LosujPolozenie();

            while (jestDobrze == true)
            {
                if (CzyMozna(LosoweX, LosoweY) == false)
                {
                    if (dwaLwy == false)
                    {
                        PlanszaZmiana(LosoweX, LosoweY, krokodylOn);
                        dwaLwy = true;
                    }
                    else if (dwaLwy == true)
                    {
                        PlanszaZmiana(LosoweX, LosoweY, krokodylOna);
                        jestDobrze = false;
                    }
                }
                else
                {
                    LosujPolozenie();
                }
            }
        }

        public void umiescSlonie()
        {
            bool jestDobrze = true;
            string slonOn = "S";
            string slonOna = "s";
            bool dwaLwy = false;

            LosujPolozenie();

            while (jestDobrze == true)
            {

                if (CzyMozna(LosoweX, LosoweY) == false)
                {
                    if (dwaLwy == false)
                    {
                        PlanszaZmiana(LosoweX, LosoweY, slonOn);
                        dwaLwy = true;
                    }
                    else if (dwaLwy == true)
                    {
                        PlanszaZmiana(LosoweX, LosoweY, slonOna);
                        jestDobrze = false;
                    }
                }
                else
                {
                    LosujPolozenie();
                }
            }
        }

        public void umiescAntylopy()
        {
            bool jestDobrze = true;
            string antylopaOn = "A";
            string antylopaOna = "a";
            bool dwaLwy = false;

            LosujPolozenie();

            while (jestDobrze == true)
            {

                if (CzyMozna(LosoweX, LosoweY) == false)
                {
                    if (dwaLwy == false)
                    {
                        PlanszaZmiana(LosoweX, LosoweY, antylopaOn);
                        dwaLwy = true;
                    }
                    else if (dwaLwy == true)
                    {
                        PlanszaZmiana(LosoweX, LosoweY, antylopaOna);
                        jestDobrze = false;
                    }
                }
                else
                {
                    LosujPolozenie();
                }
            }
        }
    }

    class Plansza
    {
        public int PoleX { get; set; }
        public int PoleY { get; set; }
        public string WartoscPola { get; set; }
        public string Przechowaj { get; set; }
        public int Licz = 0;
        private char znak;
        //L
        private bool czyBylaZamiana = false;
        private bool czyByloPrzekroczenie = false;
        private bool czyKtosByl = false;
        //l
        private bool czyBylaZamiana1 = false;
        private bool czyByloPrzekroczenie1 = false;
        private bool czyKtosByl1 = false;
        //K
        private bool czyBylaZamiana2 = false;
        //k
        private bool czyBylaZamiana3 = false;
        //A
        private bool czyBylaZamiana4 = false;
        private bool czyByloPrzekroczenie4 = false;
        //a
        private bool czyBylaZamiana5 = false;
        private bool czyByloPrzekroczenie5 = false;
        //S
        private bool czyByloGora = false;
        private bool czyByloPrawo = false;
        private bool czyByloDol = false;
        private bool czyByloLewo = false;
        //s
        private bool czyByloGora1 = false;
        private bool czyByloPrawo1 = false;
        private bool czyByloDol1 = false;
        private bool czyByloLewo1 = false;

        private string[,] planszaStart = new string[9, 9];

        /// <summary>
        /// Zwraca ilosć kolumn - X
        /// </summary>
        /// <returns></returns>
        public int WymiarPlanszyX()
        {
            return planszaStart.GetLength(0);
        }

        /// <summary>
        /// Zwraca ilość wierszy - Y
        /// </summary>
        /// <returns></returns>
        public int WymiarPlanszyY()
        {
            return planszaStart.GetLength(1);
        }

        public string ZwrocWartoscPola(int x, int y)
        {
            return planszaStart[x, y];
        }

        /// <summary>
        /// Do wprowadzania zmian na planszy
        /// </summary>
        /// <param name="PoleX"></param>
        /// <param name="PoleY"></param>
        /// <param name="WartoscPola"></param>
        public void PlanszaZmiana(int PoleX, int PoleY, string WartoscPola)
        {
            this.PoleX = PoleX;
            this.PoleY = PoleY;
            this.WartoscPola = WartoscPola;
            planszaStart[PoleX, PoleY] = WartoscPola;
        }

        public bool CzyMozna(int PoleX, int PoleY)
        {
            if (planszaStart[PoleX, PoleY] != "-")
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        /// <summary>
        /// Do inicjalizacji zawartości planszy
        /// </summary>
        public void NowaPlansza()
        {
            for (int i = 0; i < planszaStart.GetLength(0); i++)
            {
                for (int j = 0; j < planszaStart.GetLength(1); j++)
                {
                    planszaStart[i, j] = "-";
                }
            }
        }

        /// <summary>
        /// Do rysowania planszy
        /// </summary>
        public void Rysuj()
        {
            if (Licz == 0)
            {
                Console.WriteLine("Plansza startowa");
            }
            else
            {
                Console.WriteLine("Tura: {0}", Licz);
            }

            for (int i = 0; i < planszaStart.GetLength(0); i++)
            {
                for (int j = 0; j < planszaStart.GetLength(1); j++)
                {
                    Console.Write("\t" + planszaStart[i, j]);
                }
                Console.WriteLine();
            }
            Licz++;
        }

        public void Tura()
        {
            for (int kolumna = 0; kolumna < planszaStart.GetLength(0); kolumna++)
            {
                for (int wiersz = 0; wiersz < planszaStart.GetLength(1); wiersz++)
                {

                    Przechowaj = planszaStart[kolumna, wiersz];
                    znak = char.Parse(Przechowaj);

                    switch (znak)
                    {
                        case 'L':
                            {
                                //Console.WriteLine("Znak: {0} K: {1} W: {2}", znak, kolumna, wiersz);

                                if (wiersz != 0 && wiersz != WymiarPlanszyY() - 1 && ZwrocWartoscPola(kolumna, wiersz + 1) != "-" && czyKtosByl == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz - 1, "-");
                                    PlanszaZmiana(kolumna, wiersz, "L");
                                    czyKtosByl = true;
                                }
                                else if (czyKtosByl == true)
                                {
                                    if (wiersz == 0)
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna, WymiarPlanszyY() - 1, "L");
                                        czyKtosByl = false;
                                        czyBylaZamiana = false;
                                    }
                                    else
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna, wiersz - 1, "L");
                                        czyKtosByl = false;
                                        czyBylaZamiana = false;
                                    }
                                }
                                else if (wiersz == 0 && ZwrocWartoscPola(kolumna, wiersz + 1) != "-")
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna, WymiarPlanszyY() - 1, "L");
                                }
                                else if (wiersz == WymiarPlanszyY() - 1 && czyByloPrzekroczenie == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz - 1, "-");
                                    PlanszaZmiana(kolumna, wiersz, "L");
                                    czyByloPrzekroczenie = true;
                                }
                                else if (wiersz == WymiarPlanszyY() - 1 && ZwrocWartoscPola(kolumna, wiersz) == "L" && czyByloPrzekroczenie == true)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna, 0, "L");
                                    czyByloPrzekroczenie = false;
                                    czyBylaZamiana = false;
                                }
                                else if (wiersz != WymiarPlanszyY() - 1 && czyBylaZamiana == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna, wiersz + 1, "L");
                                    czyBylaZamiana = true;
                                }
                                else if (czyBylaZamiana == true)
                                {
                                    czyBylaZamiana = false;
                                }

                                break;
                            }
                        case 'l':
                            {
                                //Console.WriteLine("Znak: {0} K: {1} W: {2}", znak, kolumna, wiersz);

                                if (wiersz != 0 && wiersz != WymiarPlanszyY() - 1 && ZwrocWartoscPola(kolumna, wiersz + 1) != "-" && czyKtosByl1 == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz - 1, "-");
                                    PlanszaZmiana(kolumna, wiersz, "l");
                                    czyKtosByl1 = true;
                                }
                                else if (czyKtosByl1 == true)
                                {
                                    if (wiersz == 0)
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna, WymiarPlanszyY() - 1, "l");
                                        czyKtosByl1 = false;
                                        czyBylaZamiana1 = false;
                                    }
                                    else
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna, wiersz - 1, "l");
                                        czyKtosByl1 = false;
                                        czyBylaZamiana1 = false;
                                    }
                                }
                                else if (wiersz == 0 && ZwrocWartoscPola(kolumna, wiersz + 1) != "-")
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna, WymiarPlanszyY() - 1, "l");
                                }
                                else if (wiersz == WymiarPlanszyY() - 1 && czyByloPrzekroczenie1 == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz - 1, "-");
                                    PlanszaZmiana(kolumna, wiersz, "l");
                                    czyByloPrzekroczenie1 = true;
                                }
                                else if (wiersz == WymiarPlanszyY() - 1 && ZwrocWartoscPola(kolumna, wiersz) == "l" && czyByloPrzekroczenie1 == true)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna, 0, "l");
                                    czyByloPrzekroczenie1 = false;
                                    czyBylaZamiana1 = false;
                                }
                                else if (wiersz != WymiarPlanszyY() - 1 && czyBylaZamiana1 == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna, wiersz + 1, "l");
                                    czyBylaZamiana1 = true;
                                }
                                else if (czyBylaZamiana1 == true)
                                {
                                    czyBylaZamiana1 = false;
                                }

                                break;
                            }
                        case 'K':
                            {
                                //Console.WriteLine("Znak: {0} K: {1} W: {2}", znak, kolumna, wiersz);
                                if (kolumna == WymiarPlanszyX() - 1 && czyBylaZamiana2 == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "K");
                                    PlanszaZmiana(0, wiersz, "-");
                                    czyBylaZamiana2 = true;
                                }
                                else if (czyBylaZamiana2 == false && kolumna != 0 && (ZwrocWartoscPola(kolumna - 1, wiersz) == "-" ||
                                    ZwrocWartoscPola(kolumna - 1, wiersz) == "A" ||
                                    ZwrocWartoscPola(kolumna - 1, wiersz) == "a"))
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna - 1, wiersz, "K");
                                    czyBylaZamiana2 = true;
                                }
                                else if (kolumna == 0 && (ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "-" ||
                                    ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "A" ||
                                    ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "a"))
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(WymiarPlanszyX() - 1, wiersz, "K");
                                    czyBylaZamiana2 = false;
                                }
                                else if (kolumna != 0)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna - 1, wiersz, "K");
                                    czyBylaZamiana2 = true;
                                }

                                break;
                            }
                        case 'k':
                            {
                                //Console.WriteLine("Znak: {0} K: {1} W: {2}", znak, kolumna, wiersz);
                                if (kolumna == WymiarPlanszyX() - 1 && czyBylaZamiana3 == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "k");
                                    PlanszaZmiana(0, wiersz, "-");
                                    czyBylaZamiana3 = true;
                                }
                                else if (czyBylaZamiana3 == false && kolumna != 0 && (ZwrocWartoscPola(kolumna - 1, wiersz) == "-" ||
                                    ZwrocWartoscPola(kolumna - 1, wiersz) == "A" ||
                                    ZwrocWartoscPola(kolumna - 1, wiersz) == "a"))
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna - 1, wiersz, "k");
                                    czyBylaZamiana3 = true;
                                }
                                else if (kolumna == 0 && (ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "-" ||
                                    ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "A" ||
                                    ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "a"))
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(WymiarPlanszyX() - 1, wiersz, "k");
                                    czyBylaZamiana3 = false;
                                }
                                else if (kolumna != 0)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna - 1, wiersz, "k");
                                    czyBylaZamiana3 = true;
                                }
                                break;
                            }
                        case 'S':
                            {

                                try
                                {
                                    if (kolumna != 0 && ZwrocWartoscPola(kolumna - 1, wiersz) == "-" && czyByloGora == false)
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna - 1, wiersz, "S");
                                        czyByloGora = true;
                                    }
                                    else if (wiersz != WymiarPlanszyY() - 1 && wiersz != 0 && czyByloGora == true && ZwrocWartoscPola(kolumna, wiersz + 1) == "-" && czyByloLewo == false)
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna, wiersz - 1, "S");
                                        czyByloLewo = true;
                                    }
                                    else if (kolumna != WymiarPlanszyX() - 1 && czyByloDol == false && czyByloLewo == true && czyByloGora == true &&
                                        ZwrocWartoscPola(kolumna + 1, wiersz) == "-")
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna + 1, wiersz, "S");
                                        czyByloDol = true;
                                    }


                                    else if (kolumna != 0 && kolumna != WymiarPlanszyY() - 1 && czyByloGora == true && czyByloDol == true && czyByloLewo == true && czyByloPrawo == false &&
                                        ZwrocWartoscPola(kolumna, wiersz + 1) == "-")
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna, wiersz + 1, "S");
                                        czyByloGora = false;
                                        czyByloLewo = false;
                                        czyByloDol = false;
                                        czyByloPrawo = false;
                                    }
                                    else
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "S");
                                    }
                                }
                                catch (Exception)
                                {


                                }

                                break;
                            }
                        case 's':
                            {
                                try
                                {
                                    if (kolumna != 0 && ZwrocWartoscPola(kolumna - 1, wiersz) == "-" && czyByloGora1 == false)
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna - 1, wiersz, "s");
                                        czyByloGora1 = true;
                                    }
                                    else if (wiersz != WymiarPlanszyY() - 1 && wiersz != 0 && czyByloGora1 == true && ZwrocWartoscPola(kolumna, wiersz + 1) == "-" && czyByloLewo1 == false)
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna, wiersz - 1, "s");
                                        czyByloLewo1 = true;
                                    }
                                    else if (kolumna != WymiarPlanszyX() - 1 && czyByloDol1 == false && czyByloLewo1 == true && czyByloGora1 == true
                                        )
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna + 1, wiersz, "s");
                                        czyByloDol1 = true;
                                    }
                                    else if (kolumna != WymiarPlanszyY() - 1 && czyByloGora1 == true && czyByloDol1 == true && czyByloLewo1 == true && czyByloPrawo1 == false &&
                                        ZwrocWartoscPola(kolumna, wiersz + 1) == "-")
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "-");
                                        PlanszaZmiana(kolumna, wiersz + 1, "s");
                                        czyByloGora1 = false;
                                        czyByloLewo1 = false;
                                        czyByloDol1 = false;
                                        czyByloPrawo1 = false;
                                    }
                                    else
                                    {
                                        PlanszaZmiana(kolumna, wiersz, "s");
                                    }
                                }
                                catch (Exception)
                                {


                                }

                                break;
                            }
                        case 'A':
                            {
                                if (wiersz == WymiarPlanszyY() - 1 && czyByloPrzekroczenie4 == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz - 1, "-");
                                    PlanszaZmiana(kolumna, WymiarPlanszyY() - 1, "A");
                                    czyByloPrzekroczenie4 = true;
                                }
                                else if (czyByloPrzekroczenie4 == true)
                                {
                                    PlanszaZmiana(kolumna, WymiarPlanszyY() - 1, "-");
                                    PlanszaZmiana(kolumna, 0, "A");
                                    czyByloPrzekroczenie4 = false;
                                }
                                else if (wiersz != WymiarPlanszyY() - 1 && czyBylaZamiana4 == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna, wiersz + 1, "A");
                                    czyBylaZamiana4 = true;
                                }
                                else if (wiersz == 0)
                                {
                                    PlanszaZmiana(kolumna, 0, "-");
                                    PlanszaZmiana(kolumna, wiersz + 1, "A");
                                }
                                else if (wiersz != WymiarPlanszyY() - 1 && czyBylaZamiana4 == true)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "A");
                                    czyBylaZamiana4 = false;
                                }
                                break;
                            }
                        case 'a':
                            {
                                if (wiersz == WymiarPlanszyY() - 1 && czyByloPrzekroczenie5 == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz - 1, "-");
                                    PlanszaZmiana(kolumna, WymiarPlanszyY() - 1, "a");
                                    czyByloPrzekroczenie5 = true;
                                }
                                else if (czyByloPrzekroczenie5 == true)
                                {
                                    PlanszaZmiana(kolumna, WymiarPlanszyY() - 1, "-");
                                    PlanszaZmiana(kolumna, 0, "a");
                                    czyByloPrzekroczenie5 = false;
                                }
                                else if (wiersz != WymiarPlanszyY() - 1 && czyBylaZamiana5 == false)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "-");
                                    PlanszaZmiana(kolumna, wiersz + 1, "a");
                                    czyBylaZamiana5 = true;
                                }
                                else if (wiersz == 0)
                                {
                                    PlanszaZmiana(kolumna, 0, "-");
                                    PlanszaZmiana(kolumna, wiersz + 1, "a");
                                }
                                else if (wiersz != WymiarPlanszyY() - 1 && czyBylaZamiana5 == true)
                                {
                                    PlanszaZmiana(kolumna, wiersz, "a");
                                    czyBylaZamiana5 = false;
                                }
                                break;
                            }
                        default:
                            {
                                break;
                            }
                    }
                }
            }
        }
    }

    //public void WczytajRozmiar()
    //{
    //    int poleX = 0;
    //    int poleY = 0;
    //    Console.WriteLine("Wprowadz rozmiar planszy X:");
    //    Przechowaj = Console.ReadLine();
    //    poleX = int.Parse(Przechowaj);

    //    Console.WriteLine("Wprowadz rozmiar planszy Y:");
    //    Przechowaj = Console.ReadLine();
    //    poleY = int.Parse(Przechowaj);
    //    NowaPlansza(poleX, poleY);        
    //}













    //    else if (wiersz == 8 && czyByloPrzekroczenie == false)
    //{
    //    Console.WriteLine("Lew doszedł do miejsca w którym diabeł mówi dobranoc!");
    //    planszaStart[kolumna, przechowajWiersz] = "L";
    //    czyByloPrzekroczenie = true;

    //}

    //if(ZwrocWartoscPola(kolumna, wiersz + 1) != "A"|| ZwrocWartoscPola(kolumna, wiersz + 1) != "a")

    //    if (czyBylaZamiana2 == false && kolumna == 0 && ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "-" ||
    //                                   ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "A" ||
    //                                   ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "a")
    //                                {
    //                                    Console.WriteLine("XS");
    //                                    PlanszaZmiana(kolumna, wiersz, "-");
    //PlanszaZmiana(WymiarPlanszyX()-1, wiersz, "K");
    //czyBylaZamiana2 = true;
    //                                }
    //                                else if (czyBylaZamiana2 == true && kolumna == 0 && ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "-" ||
    //                                    ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "A" ||
    //                                    ZwrocWartoscPola(WymiarPlanszyX() - 1, wiersz) == "a")
    //                                {
    //                                    Console.WriteLine("XD1");
    //                                    PlanszaZmiana(kolumna, wiersz, "-");
    //PlanszaZmiana(WymiarPlanszyX() - 1, wiersz, "K");
    //czyBylaZamiana2 = false;
    //                                }
    //                                else if (ZwrocWartoscPola(kolumna-1,wiersz)!="-")
    //                                {
    //                                    Console.WriteLine("XD2");
    //                                    PlanszaZmiana(kolumna+1, wiersz, "K");
    //                                    //  PlanszaZmiana(kolumna + 1, wiersz, "K");
    //                                }
    //                                else
    //                                {
    //                                    Console.WriteLine("XD3");
    //                                    PlanszaZmiana(kolumna, wiersz, "-");
    //PlanszaZmiana(kolumna - 1, wiersz, "K");
    //                                }



    //                                    if(wiersz==WymiarPlanszyY()-1)
    //                                {
    //                                    Console.WriteLine("Ostatnie");
    //                                    PlanszaZmiana(kolumna, WymiarPlanszyY() - 1, "-");
    //PlanszaZmiana(kolumna, 0, "A");
    //                                }
    //                                else if(wiersz != 8 && ZwrocWartoscPola(kolumna, wiersz + 1 )!="-")
    //                                {
    //                                    Console.WriteLine("Pelne");
    //                                    PlanszaZmiana(kolumna, wiersz, "A");
    //                                }
    //                                else
    //                                {
    //                                    Console.WriteLine("inne");
    //                                    PlanszaZmiana(kolumna, wiersz, "-");
    //PlanszaZmiana(kolumna, wiersz+1, "A");
    //                                }
}
