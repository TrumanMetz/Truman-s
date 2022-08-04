class Program
{ 
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
        Console.WriteLine(" The Max number is " + max + " The Min number is " + min + " The Mean Number is " + mean);  
    }
}
