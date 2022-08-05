class Program
{ 
 // Make Median method.
    public static double findMedian(double[] intarr, int n)
    {
      //Sort array
        Array.Sort(intarr);
      // See if n is even.
        if (n % 2 != 0)
            return (double)intarr[n];
      // If not even then odd.
        return (double)(intarr[(n - 1) / 2] + intarr[n / 2]) / 2.0;
    }


    public static void Main(string[] args)
    {
        Random rnd = new Random();
        double[] intarr = new double[100]; //Makes empty array 

        for (int i = 0; i < intarr.Length; i++) // Appends random values to array
        {
            intarr[i] = rnd.Next();
            Console.WriteLine(intarr[i]);
        }
        Console.WriteLine();
        // Get values from array 
        double max = intarr.Max();
        double min = intarr.Min();
        double mean = intarr.Average();
        //Print values to console
        Console.WriteLine(" The Max number is " + max + " The Min number is " + min + " The Mean number is " + mean + " The Median number is " + findMedian(intarr,100));  
    }
}
