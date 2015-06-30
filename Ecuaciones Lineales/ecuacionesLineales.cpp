#include<iostream>
#include<stdlib.h>
#include "VprimeraOpcion.cpp"
#include "VsegundaOpcion.cpp"

using namespace std;

int main()
{
	int opcion=0;
	
	do{
		
		system("cls");
		cout<<endl;
		cout<<endl<<"\tEste programa determina la convergencia entre ecuaciones lineales."<<endl<<endl;
		cout<< " \t\t1. y=mx+b	2. X1+X2+X3=D1	   3.Salir"<< endl;
		cout<<"\n\n Selecciona una opcion: ";
		  cin>> opcion;
		
		switch(opcion)
		{
			case 1:
				primeraOpcion();
			break;
			
			case 2:
				segundaOpcion();
			break;
		}
	}
	while(opcion != 3);	
	system("pause");
	return 0;
}
