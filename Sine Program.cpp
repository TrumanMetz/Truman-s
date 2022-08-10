#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int arrayV[37];
	for (int i = 0; i <= 360; i = i + 10) {
		arrayV[i] = i;
		cout << " , " << arrayV[i];
	}
	float arrayS[37];
	for (int i = 0; i <= 360; i = i + 10) {
		arrayS[i] = sin(i);
		cout << " , " << arrayS[i];
	}
}
