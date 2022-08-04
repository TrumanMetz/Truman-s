//Import needed libraries. 
#include <iostream> 
#include <time.h>
#include <stdlib.h>

using namespace std;

int main()
{ 
     int Array[100];
     srand(time(NULL));
     for(int s=0; s<100; s++)
     { 
        int no = rand();
        Array[s]= no;
     }
     for(int s=0; s<100; s++)

cout<<Array[s]<<" ";

cout<<endl;

return 0;
}