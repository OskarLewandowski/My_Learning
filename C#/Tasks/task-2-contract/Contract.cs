using NodaTime;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sygeon2
{
    internal class Contract
    {
        public Contract(ZonedDateTime start, ZonedDateTime end)
        {
            Start = start;
            End = end;
        }

        public ZonedDateTime Start { get; set; }
        public ZonedDateTime End { get; set; }

        public override string ToString()
        {
            return $"Start: {Start.ToDateTimeOffset().ToString("yyyy-MM-dd'T'HH:mm:sszzz")} |" +
                $" End: {(End == default ? "-" : End.ToDateTimeOffset().ToString("yyyy-MM-dd'T'HH:mm:sszzz"))}";
        }
    }
}
