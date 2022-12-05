using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Runtime.InteropServices;
using System.Diagnostics;

namespace Lab5
{
	class Program
	{
		[DllImport("CppMatrixSolver.dll")]
		private static extern TimeSpan solve(int dimension, int repetitionCount);

		static void Main(string[] args)
		{
			/*TimesList timesList = new TimesList();
			timesList.Add(
				new TimeItem(1, 1, new TimeSpan(0, 0, 1), new TimeSpan(0, 0, 2)),
				new TimeItem(2, 2, new TimeSpan(0, 0, 2), new TimeSpan(0, 0, 2)),
				new TimeItem(3, 3, new TimeSpan(0, 0, 3), new TimeSpan(0, 0, 3))
			);

			Console.WriteLine("Original:");
			foreach (TimeItem timeItem in timesList)
				Console.WriteLine($"\t{timeItem}");

			TimesList.SaveToFile("result.txt", timesList);
			TimesList timesList1 = new TimesList();
			TimesList.LoadFromFile("result.txt", timesList1);

			Console.WriteLine("Copy:");
			foreach (TimeItem timeItem in timesList1)
				Console.WriteLine($"\t{timeItem}");*/

			TimeSpan time = solve(10000, 100);
			Console.WriteLine(time.Milliseconds);

			Console.ReadKey();
		}
	}
}
