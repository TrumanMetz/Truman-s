#include <iostream>
#define MAX 100
using namespace std;

// Function to find median.
double median(int a[], int n) {
	if (n % 2 != 0)
		return (double)a[n / 2];
	return (double)(a[(n - 1) / 2] + a[n / 2]) / 2.0;
}

// Function to find the mean.
double mean(int arr[], int n) {
	int sum = 0;
	for (int i = 0; i < n; i++)
		sum += arr[i];
	return (double)sum / (double)n;
}


int main()
{
    // Declare variables and objects.
	int arrayV[MAX];
	int n, i, j;
	int temp;
    n = 100;
	
	// Fill array with random numbers.
	for (int i = 0; i < 100; i++)
	{
		arrayV[i] = rand() % 100;
		
	}

	cout << "Unsorted Array elements:" << endl;
	for (i = 0; i < n; i++)
		cout << arrayV[i] << "\t";
	cout << endl;

	// Sorts array. If the neighbor is smaller then, they swap positions.
	for (i = 0; i < n; i++)
	{
		for (j = i + 1; j < n; j++)
		{
			if (arrayV[i] > arrayV[j])
			{
				temp = arrayV[i];
				arrayV[i] = arrayV[j];
				arrayV[j] = temp;
			}
		}
	}
	
	//print sorted array elements
	cout << "Sorted (Ascending Order) Array elements:" << endl;
	for (i = 0; i < n; i++)
		cout << arrayV[i] << "\t";
	cout << endl;
	cout << "The minimum value is: " << arrayV[0] << endl;
	cout << "The maximum value is: " << arrayV[99] << endl;
	cout << "The median value is: " << median(arrayV, n) << endl;
	cout << "The mean value is: " << mean(arrayV, n) << endl;


	return 0;

}
