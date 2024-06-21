using System;

namespace SumTwoNumbers
{
    class Program
    {
        static void Main(string[] args)
        {
            .("Enter the first number:");
            string input1 = .ReadLine();
            if (!double.TryParse(input1, out double number1))
            {
                Console.WriteLine("Invalid input. Please enter a valid number.");
                return;
            }

            Console.WriteLine("Enter the second number:");
            string input2 = Console.ReadLine();
            if (!double.TryParse(input2, out double number2))
            {
                Console.WriteLine("Invalid input. Please enter a valid number.");
                return;
            }

            double sum = AddTwoNumbers(number1, number2);
            Console.WriteLine($"The sum of {number1} and {number2} is: {sum}");
        }

        static double AddTwoNumbers(double num1, double num2)
        {
            return num1 + num2;
        }
    }
}
 using System;

namespace ProductOfNumbersInRange
{
    class Program
    {
        static void Main(string[] args)
        {
            .("Enter the first number:");
            string input1 = .ReadLine();
            if (!int.TryParse(input1, out int number1))
            {
                .("Invalid input. Please enter a valid integer.");
                return;
            }

            .("Enter the second number:");
            string input2 = .ReadLine();
            if (!int.TryParse(input2, out int number2))
            {
                .("Invalid input. Please enter a valid integer.");
                return;
            }

            long product = CalculateProductInRange(number1, number2);
            .($"The product of all numbers between {number1} and {number2} (inclusive) is: {product}");
        }

        static long CalculateProductInRange(int num1, int num2)
        {
            int start = Math.Min(num1, num2);
            int end = Math.Max(num1, num2);
            long product = 1;

            for (int i = start; i <= end; i++)
            {
                product *= i;
            }

            return product;
        }
    }
}
