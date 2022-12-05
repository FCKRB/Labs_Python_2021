using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Collections;

namespace Lab5
{
    class TimesList : IEnumerable<TimeItem>
    {
        private List<TimeItem> timesList;

        public TimesList()
        {
            timesList = new List<TimeItem>();
        }

        public void Add(params TimeItem[] timeItem)
        {
            if (timeItem is null) throw new NullReferenceException("parameter is null");
            if (timeItem.Any((_timeItem) => _timeItem is null))
                throw new ArgumentException("item is null");
            timesList.AddRange(timeItem);
        }

        public static void SaveToFile(string filename, TimesList source)
        {
            using (Stream stream = new FileStream(filename, FileMode.Create, FileAccess.Write))
            {
                var formatter = new BinaryFormatter();
                formatter.Serialize(stream, source.timesList);
            }
        }

        public static void LoadFromFile(string filename, TimesList target)
        {
            using (Stream stream = new FileStream(filename, FileMode.Open, FileAccess.Read))
            {
                var formatter = new BinaryFormatter();
                target.timesList = (List<TimeItem>)formatter.Deserialize(stream);
            }
        }

        public IEnumerator<TimeItem> GetEnumerator()
        {
            return timesList.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}
