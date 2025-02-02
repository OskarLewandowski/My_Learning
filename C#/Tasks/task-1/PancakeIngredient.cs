using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sygeon
{
    internal class PancakeIngredient
    {
        public PancakeIngredient(double flour, double groat, double milk, int egg)
        {
            Flour = flour;
            Groat = groat;
            Milk = milk;
            Egg = egg;
        }

        public double Flour { get; set; }
        public double Groat { get; set; }
        public double Milk { get; set; }
        public int Egg{ get; set; }

        public override string ToString()
        {
            return $"Flour: {Flour}, Groat: {Groat}, Milk: {Milk}, Egg: {Egg}";
        }
    }


    internal class PancakeIngredientRecord : PancakeIngredient
    {
        public PancakeIngredientRecord(DateTimeOffset timestamp, double flour, double groat, double milk, int egg) : base(flour, groat, milk, egg)
        {
            Timestamp = timestamp;
        }

        public DateTimeOffset Timestamp { get; set; }


        public override string ToString()
        {
            return $"Timestamp: {Timestamp.ToString("yyyy-MM-dd HH:00:00zzz")}, Flour: {Flour}, Groat: {Groat}, Milk: {Milk}, Egg: {Egg}";
        }
    }
}
