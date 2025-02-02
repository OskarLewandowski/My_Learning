using NodaTime;
using System.Diagnostics;
using System.Globalization;
using System.Runtime.CompilerServices;
using System.Text.RegularExpressions;
using System.Xml.Linq;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Sygeon
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string dataPath = @"C:\Users\Oskar\Desktop\Data\data_task_2.txt";
            bool dataHasHeaders = true;

            GenerateReport(dataPath, dataHasHeaders);


            Console.ReadLine();
        }

        static void GenerateReport(string dataPath, bool dataHasHeaders)
        {
            var ingredientRecords = GetIngredientRecords(dataPath, dataHasHeaders);

            //DisplayIngredientRecords(ingredientRecords);

            var processedIngredients = ProcessIngredients(ingredientRecords);

            DisplayResult(processedIngredients);
        }


        static List<PancakeIngredientRecord> GetIngredientRecords(string path, bool dataHasHeaders)
        {
            List<PancakeIngredientRecord> ingredientList = new List<PancakeIngredientRecord>();
            string[] data = null;

            if (dataHasHeaders)
            {
                data = File.ReadAllLines(path).Skip(1).ToArray(); //skip headers
            }
            else
            {
                data = File.ReadAllLines(path).ToArray();
            }

            foreach (var line in data)
            {
                var lineSplit = line.Split();

                DateTimeOffset timestamp = DateTimeOffset.Parse(lineSplit[0] + " " + lineSplit[1]);
                var flour = double.Parse(lineSplit[2]);
                var groat = double.Parse(lineSplit[3]);
                var milk = double.Parse(lineSplit[4]);
                var egg = int.Parse(lineSplit[5]);

                var newRecord = new PancakeIngredientRecord(timestamp, flour, groat, milk, egg);

                ingredientList.Add(newRecord);
            }

            return ingredientList;
        }


        static Dictionary<DateTimeOffset, PancakeIngredient> ProcessIngredients(List<PancakeIngredientRecord> ingredientRecords)
        {
            Dictionary<DateTimeOffset, PancakeIngredient> ingredients = new Dictionary<DateTimeOffset, PancakeIngredient>();
            DateTimeZone polishTimeZone = DateTimeZoneProviders.Tzdb["Europe/Warsaw"];


            foreach (var ingredientRecord in ingredientRecords)
            {
                Instant instant = Instant.FromDateTimeOffset(ingredientRecord.Timestamp);
                ZonedDateTime polishDateTimeZoned = instant.InZone(polishTimeZone);

                var polishTimestamp = TruncateDateToFullHour(polishDateTimeZoned);
                //Console.WriteLine(polishTimestamp);

                if (ingredients.ContainsKey(polishTimestamp))
                {
                    ingredients[polishTimestamp].Flour += ingredientRecord.Flour;
                    ingredients[polishTimestamp].Groat += ingredientRecord.Groat;
                    ingredients[polishTimestamp].Milk += ingredientRecord.Milk;
                    ingredients[polishTimestamp].Egg += ingredientRecord.Egg;
                }
                else
                {
                    ingredients[polishTimestamp] = new PancakeIngredient(ingredientRecord.Flour, 
                        ingredientRecord.Groat, ingredientRecord.Milk, ingredientRecord.Egg);
                }
            }

            return ingredients;
        }


        static void DisplayResult(Dictionary<DateTimeOffset, PancakeIngredient> ingredients)
        {
            Console.WriteLine(new string('-', 80));

            //string[] headers = ["TIMESTAMP", "FLOUR", "GROAT", "MILK", "EGG"];
            string[] headers = ["ZNACZNIK CZASU", "MĄKA(kg)", "KASZA(kg)", "MLEKO(l)", "JAJKA(szt)"];


            Console.WriteLine("{0,-30}{1,-13}{2,-13}{3,-13}{4,-13}",
                headers[0], headers[1], headers[2], headers[3], headers[4]);


            foreach (var ingredient in ingredients)
            {
                var timestamp = ingredient.Key.ToString("yyyy-MM-dd HH:00:00zzz");
                var flour = Math.Round(ingredient.Value.Flour * 0.01, 2);
                var groat = Math.Round(ingredient.Value.Groat * 0.001, 2);
                var milk = Math.Round(ingredient.Value.Milk * 0.001, 2);
                var egg = ingredient.Value.Egg;

                Console.WriteLine("{0,-30}{1,-13}{2,-13}{3,-13}{4,-13}",
                    timestamp, flour, groat, milk, egg);
            }
            Console.WriteLine(new string('-', 80));
        }


        static DateTimeOffset TruncateDateToFullHour(ZonedDateTime timestamp)
        {
            DateTimeOffset date = timestamp.ToDateTimeOffset();

            string formattedDate = date.ToString("yyyy-MM-dd HH:00:00zzz");

            return DateTimeOffset.Parse(formattedDate);
        }


        static void DisplayIngredientRecords(List<PancakeIngredientRecord> ingredientRecords)
        {
            Console.WriteLine(new string('-', 80));
            foreach (var ingredientRecord in ingredientRecords)
            {
                Console.WriteLine(ingredientRecord);
            }
            Console.WriteLine(new string('-', 80));
        }
    }
}


