#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

int main()
{
	// Get values of angles.
	int arrayV[37];
	for (int i = 0; i <= 360; i = i + 10) {
		arrayV[i] = i;
		cout << arrayV[i] << ',';
	}
	// Get Sine of the angle.
	float arrayS[37];
	for (int i = 0; i <= 360; i = i + 10) {
		arrayS[i] = sin(i * (3.14159/180));
		cout << arrayS[i] << ','; 
	}
	std::ofstream myfile;
	myfile.open("Sine program c++.csv");
	for (int i = 0; i <= 37; i++) {
		myfile << arrayV[i] << "," << arrayS[i];
	}
	myfile.close();
}
