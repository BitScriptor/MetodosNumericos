#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
	float itera = 0.0;
	float dist=0.0;
	float nitera = 0.0;
	float ap = 0.0;
	float total = 0.0;
	
	cout<< " Que distancia es la base total?: ";
	  cin>> dist;
	  
	cout<< " En cuantas iteraciones se dividira? : ";
	  cin>> itera;
	  
	nitera = dist/itera;
	
	for(float r=0.0; r<itera; r++)
	{
		ap=(nitera * ((r*nitera)*(r*nitera)));
		total+=ap;
	}
	
	
	
	cout<< total;
	
	system("Pause");
	return 0;
}
