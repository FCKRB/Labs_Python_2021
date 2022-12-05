using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lab5
{
    class Matrix
    {
        private readonly double[] upperDiagonal;
        private readonly double[] mainDiagonal;
        private readonly double[] lowerDiagonal;

        public Matrix(int dimension)
        {
            upperDiagonal = new double[dimension - 1];
            lowerDiagonal = new double[dimension - 1];
            mainDiagonal = new double[dimension];

            for (int i = 0; i < dimension - 1; ++i)
            {
                upperDiagonal[i] = i;
                lowerDiagonal[i] = i;
                mainDiagonal[i] = i*i*i * mainDiagonal[i];
            }
            mainDiagonal[dimension - 1] = dimension*dimension*dimension
                * mainDiagonal[dimension - 2];
        }

        public Matrix(double[] upperDiagonal, double[] mainDiagonal, double[] lowerDiagonal)
        {
            int upperDiagonalDimension = upperDiagonal.Length;
            if (upperDiagonalDimension != lowerDiagonal.Length)
                throw new ArgumentException("upper and lower diagonals' size does not match");
            if (upperDiagonalDimension != mainDiagonal.Length - 1)
                throw new ArgumentException("upper and main diagonals' size does not match");

            this.upperDiagonal = upperDiagonal;
            this.mainDiagonal = mainDiagonal;
            this.lowerDiagonal = lowerDiagonal;
        }

        public void Solve(double[] result, double[] constantTerms)
        {
            int n = result.Length;
            double[] b = new double[n -1];
            double[] g = new double[n];

            b[0] = upperDiagonal[0] / mainDiagonal[0];
            g[0] = constantTerms[0] / mainDiagonal[0];

            for (int i = 1; i < n - 1; ++i)
            {
                b[i] = upperDiagonal[i] / (mainDiagonal[i] - b[i - 1] * lowerDiagonal[i - 1]);
                g[i] = (constantTerms[i] - lowerDiagonal[i - 1] * g[i - 1])
                    / (mainDiagonal[i] - b[i - 1] * lowerDiagonal[i - 1]);
            }

            result[n - 1] = g[n - 1] = (constantTerms[n - 1] - lowerDiagonal[n - 2] * g[n - 2])
                    / (mainDiagonal[n - 1] - b[n - 2] * lowerDiagonal[n - 2]);

            for (int i = n - 2; i >= 0; --i)
                result[i] = g[i] - b[i] * result[i + 1];
        }

        public override string ToString()
        {
            StringBuilder stringBuilder = new StringBuilder();
            int dimension = mainDiagonal.Count();
            for (int i = 0; i < dimension; ++i)
            {
                for (int j = 0; j < dimension; ++j)
                {
                    switch (i - j)
                    {
                        case -1:
                            stringBuilder.Append(string.Format("{:0.00}", upperDiagonal[i]));
                            break;

                        case 0:
                            stringBuilder.Append(string.Format("{:0.00}", mainDiagonal[i]));
                            break;

                        case 1:
                            stringBuilder.Append(string.Format("{:0.00}", lowerDiagonal[j]));
                            break;

                        default:
                            stringBuilder.Append("0.00");
                            break;
                    }
                }
                stringBuilder.AppendLine();
            }
            return stringBuilder.ToString();
        }
    }
}
