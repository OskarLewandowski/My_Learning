using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Lekcja02
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //var st= new Student();
            Student st = null;
            st = new Student();
            st.Imie = null;
            st.Studiuj();
            Console.WriteLine(st.CzyJestPoprawny());
            Console.WriteLine(SprawdzStudenta.CzyJestPoprawny(st));
            Console.WriteLine(SystemString.CzyJestNullemLubPustym(st));
            Console.Read();
        }
        public class Student
        {
            public string Imie { get; set; }

            public void Studiuj()
            {
                Console.WriteLine("{0} studiuje. ",Imie);
            }

            //public bool CzyJestPoprawny()
            //{
            //    return Imie != null;
            //}
        }

        public static class SprawdzStudenta
        {
            public static bool CzyJestPoprawny(Program.Student student)
            {
                return student.Imie != null;
            }
        }
    }

        public static class StudentExtension
        {
            public static bool CzyJestPoprawny(this Program.Student student)
            {
                //String imie = student.Imie;
                //return imie.CzyNull();
                return student.Imie != null;
            }
        }
        public static class StringExtension
        {
            public static bool CzyNull(this String tekst)
            {
                return tekst != null;
            }
        }
        public static class SystemExtension
        {
            public static bool IsNullOrEmpty(this String tekst)
            {
                return tekst == null;
            }
        }
        public static class SystemString
        {
            public static bool CzyJestNullemLubPustym(Program.Student student)
            {
                if (student.Imie == null)
                {
                    Console.Write("Czy jest nullem: ");
                    return student.Imie == null;
                }
                else if (student.Imie == "")
                {
                    Console.Write("Czy jest puste: ");
                    return student.Imie == "";
                }
                else if (student.Imie != "")
                {
                    Console.Write("Czy nie jest puste: ");
                    return student.Imie != "";
                }
                else
                {
                    Console.Write("Rozne od nulla: ");
                    return student.Imie != null;
                }
               
            }
        }
}