class Program
{ 
    public static void Main(string[] args)
    {
        Random rnd = new Random();
        int[] intarr = new int[100];

        for (int i = 0; i < intarr.Length; i++)
        {
            intarr[i] = rnd.Next();
            Console.WriteLine(intarr[i]);
        }
        Console.WriteLine();
        int maxNum = intarr.Max();
        Console.WriteLine("The Max number is " + maxNum);
        Console.ReadLine();
    }
}
