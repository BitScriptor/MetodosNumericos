#include<iostream>
#include<stdlib.h>

using namespace std;
	
	
	float area( float a, float contador)
	{
		float total=0.0;
	  contador=contador-1;
	  
	  if(contador == 0)
	  	return total;
	  	
	  else
	  {
			total = (a * ((contador*a)*(contador*a)));
	
	  	
	  		
	  		total=total+area(a, contador);
	       return total;
	  }
	}
	
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
	  
	  
	  
	  cout << area(dist/itera, itera) << endl;
	  
	  system("pause");
	  return 0;
}
