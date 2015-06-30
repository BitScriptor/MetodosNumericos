#include<iostream>
#include<stdlib.h>

using namespace std;
	
	
	float area( float a, float itera, int rec) //FUNCION QUE HACE LAS ITERACIONES
	{
		float total=0.0; // DECLARACION DE VARIABLES LOCALES
		
	  
	  if(rec == itera) //CONDICION POR SI EL NUMERO DE ITERACIONES ES IGUAL A 0
	  
	  	return total;
	  	
	  else
	  {
			total = (a * ((rec*a)*(rec*a)));//FORMULA QUE DETERMINA EL AREA B*H
			
			return total+= area(a, itera, rec+1);//USO DE RECURSIVIDAD PARA GENERAR N ITERACIONES
			
	  }
	}
	
int main()
{
	float itera = 0.0;//DECLARACION DE VARIABLES GLOBALES
	float dist=0.0;
	int rec=0;
	
		cout<< " Que distancia es la base total?: ";//PETICON DE LA BASE
	  cin>> dist;
	  
	  cout << endl;
	  
	cout<< " En cuantas iteraciones se dividira? : ";//PETICION DE LAS ITERACIONES
	  cin>> itera;
	  
	  
	  cout << endl << endl << "El area es: "<< area(dist/itera, itera, rec) << endl << endl<< endl;//IMPRESION DEL RESULTADO OTORGANDO LOS ARGUMENTOS A LA FUNCION
	  
	  system("pause");
	  return 0;
}
