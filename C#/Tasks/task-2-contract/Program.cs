using NodaTime;
using NodaTime.Text;

namespace Sygeon2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string timeInterval = "2023-02-09T00:00:00+01:00 - 2024-01-18T00:00:00+01:00 (Europe/Warsaw)";

            string dataPath = @"C:\Users\Oskar\Desktop\Data\data_task_3.txt";

            bool dataHasHeaders = true;
            
            GenerateReport(timeInterval, dataPath, dataHasHeaders);

            Console.ReadLine();
        }


        static void GenerateReport(string timeInterval, string dataPath, bool dataHasHeaders)
        {
            var contracts = GetContracts(dataPath, dataHasHeaders);

            //DisplayContracts(contracts);

            var timeIntervalContract = GetTimeInterval(timeInterval);

            var result = ProcessContracts(timeIntervalContract, contracts);

            //DisplayContracts(result);

            DisplayResult(result);
        }


        static void DisplayResult(List<Contract> contracts)
        {
            Console.WriteLine(new string('-', 80));

            string[] headers = ["POCZĄTEK", "KONIEC"];

            Console.WriteLine("{0,-30}{1,-30}", headers[0], headers[1]);

            foreach (var contract in contracts)
            {
                var start = contract.Start.ToDateTimeOffset().ToString("yyyy-MM-dd'T'HH:mm:sszzz");
                var end = contract.End.ToDateTimeOffset().ToString("yyyy-MM-dd'T'HH:mm:sszzz");

                Console.WriteLine("{0,-30}{1,-30}", start, end);
            }

            if (contracts.Count == 1)
            {
                Console.WriteLine("\nBrak kontraktów w podanym przedziale czasowym\n");
            }

            Console.WriteLine(new string('-', 80));
        }


        static List<Contract> ProcessContracts(Contract timeInterval, List<Contract> contracts)
        {
            List<Contract> resultContracts = new List<Contract>();
            var timeZone = timeInterval.Start.Zone;

            //DisplayContracts(contracts);

            var contractDates = ExtractContractDatesWithoutDefaultValue(contracts);
            contractDates.Add(timeInterval.End);

            var actualStartDate = timeInterval.Start;

            foreach (var nextStartDate in contractDates)
            {
                if (nextStartDate.ToInstant() > actualStartDate.ToInstant())
                {
                    resultContracts.Add(new Contract(actualStartDate.WithZone(timeZone), nextStartDate.WithZone(timeZone)));
                    actualStartDate = nextStartDate;
                }
            }

            return resultContracts;
        }


        static List<ZonedDateTime> ExtractContractDatesWithoutDefaultValue(List<Contract> contracts)
        {
            HashSet<ZonedDateTime> dates = new HashSet<ZonedDateTime>(contracts.SelectMany(c => new[] { c.Start, c.End }));

            dates.Remove(default);

            return dates.OrderBy(d => d.ToInstant()).ToList();
        }


        static Contract GetTimeInterval(string timeInterval)
        {
            var lineSplit = timeInterval.Replace(" - ", " ").Split();

            var startOffsetDateTime = OffsetDateTimePattern.ExtendedIso.Parse(lineSplit[0]).Value;
            var endOffsetDateTime = OffsetDateTimePattern.ExtendedIso.Parse(lineSplit[1]).Value;

            Instant startInstant = startOffsetDateTime.ToInstant();
            Instant endInstant = endOffsetDateTime.ToInstant();

            DateTimeZone preferedTimeZone = DateTimeZoneProviders.Tzdb[lineSplit[2].Trim('(', ')')];

            ZonedDateTime start = startInstant.InZone(preferedTimeZone);
            ZonedDateTime end = endInstant.InZone(preferedTimeZone);

            return new Contract(start, end);
        }


        static List<Contract> GetContracts(string path, bool dataHasHeaders = true)
        {
            List<Contract> contract = new List<Contract>();
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
                //Console.WriteLine(line);

                var lineSplit = line.Split();

                ZonedDateTime start = OffsetDateTimePattern.ExtendedIso.Parse(lineSplit[0]).Value.InFixedZone();
                ZonedDateTime end = default;

                if (lineSplit[1] != "-")
                {
                    end = OffsetDateTimePattern.ExtendedIso.Parse(lineSplit[1]).Value.InFixedZone();
                }

                var newRecord = new Contract(start, end);

                contract.Add(newRecord);
            }

            return contract;
        }


        static void DisplayContracts(List<Contract> contracts)
        {
            Console.WriteLine(new string('-', 80));
            foreach (var contract in contracts)
            {
                Console.WriteLine(contract);
            }
            Console.WriteLine(new string('-', 80));
        }
    }
}
