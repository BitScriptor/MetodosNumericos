#include<iostream>
#include<stdlib.h>

using namespace std;
	
	
	float area( float a, float itera, int rec)
	{
		float total=0.0;
		
	  
	  if(rec == itera)
	  
	  	return total;
	  	
	  else
	  {
			total = (a * ((rec*a)*(rec*a)));
			
			return total+= area(a, itera, rec+1);
			
	  }
	}
	
int main()
{
	float itera = 0.0;
	float dist=0.0;
	int rec=0;
	
		cout<< " Que distancia es la base total?: ";
	  cin>> dist;
	  
	  cout << endl;
	  
	cout<< " En cuantas iteraciones se dividira? : ";
	  cin>> itera;
	  
	  
	  cout << endl << endl << "El area es: "<< area(dist/itera, itera, rec) << endl << endl<< endl;
	  
	  system("pause");
	  return 0;
}
