#include<iostream>
#include<stdlib.h>

using namespace std;

void segundaOpcion()
{
	system("cls");
	
	int ecuaciones=0, variables=0;
	
	cout<< "\t\tCuantas ecuaciones y variables ingresaras?"<<endl<<endl;
	cout<< "\t\t\tEcuaciones:";
	  cin>>ecuaciones;
	cout<< "\t\t\tVariables:";
	  cin>>variables;
	
	if(ecuaciones == 1 || variables == 1)
		cout<<"\tDebes ingresar al menos dos escuaciones o mas de dos variables."<<endl<<endl;
		
	else if(ecuaciones==2 && variables==2)
	{
		float a1=0, a2=0, b1=0, b2=0, r1=0, r2=0, determinante =0, x=0, y=0;
		
		cout<<endl<<endl<<"\t\tIngresa los valores de: a1, a2, b1 y b2."<<endl<<endl;
		cout<<"\t\t\t\ta1: ";
		  cin>>a1;
		cout<<"\t\t\t\ta2: ";
		  cin>>a2;
		cout<<"\t\t\t\tr1: ";
		  cin>>r1;
		cout<<"\t\t\t\tb1: ";
		  cin>>b1;
		cout<<"\t\t\t\tb2: ";
		  cin>>b2;
		cout<<"\t\t\t\tr2: ";
		  cin>>r2;
		cout<<endl<<endl<<"\t\tLas ecuaciones son las siguientes: "<<endl<<endl;
		cout<<"\t\t\t\t"<<a1<<"x+"<<a2<<"x2="<<r1<<endl<<endl;
		cout<<"\t\t\t\t"<<b1<<"x+"<<b2<<"x2="<<r2<<endl<<endl;		
		
		determinante = (a1*b2)-(a2*b1);
		
		if(determinante != 0)
		{
			cout<<"\tSi tienen convergencia pues el determinante es diferente de 0"<<endl<<endl;
			cout<<"\t\t\tEl determinante es: "<< determinante<<endl<<endl;
			
			x = ((r1*b2)-(a2*r2))/determinante;
			
			y = ((a1*r2)-(r1*b1))/determinante;
			
			cout<< "\t\t    Convergen en: ("<<x<<","<<y<<")"<<endl<<endl<<endl;
		}
		else
		{
			cout<<"\t\t  El sistema no tiene solucion."<<endl<<endl;
			cout<<"\t\t\tEl determinante es: "<<determinante<<endl<<endl;
		}
	}
	else if(ecuaciones==3 && variables==3)
	{
		float a1=0, a2=0, a3=0, b1=0, b2=0, b3=0, c1=0, c2=0, c3=0, r1=0, r2=0, r3=0, determinante=0, x=0, y=0, z=0;
		
		cout<<endl<<endl<<"\t\tIngresa los valores de: a1, a2, b1 y b2."<<endl<<endl;
		cout<<"\t\t\t\ta1: ";
		  cin>>a1;
		cout<<"\t\t\t\ta2: ";
		  cin>>a2;
		cout<<"\t\t\t\ta3: ";
		  cin>>a3;
		cout<<"\t\t\t\tr1: ";
		  cin>>r1;
		cout<<"\t\t\t\tb1: ";
		  cin>>b1;
		cout<<"\t\t\t\tb2: ";
		  cin>>b2;
		cout<<"\t\t\t\tb3: ";
		  cin>>b3;
		cout<<"\t\t\t\tr2: ";
		  cin>>r2;
		cout<<"\t\t\t\tc1: ";
		  cin>>c1;
		cout<<"\t\t\t\tc2: ";
		  cin>>c2;
		cout<<"\t\t\t\tc3: ";
		  cin>>c3;
		cout<<"\t\t\t\tr3: ";
		  cin>>r3;
		cout<<endl<<endl<<"\t\tLas ecuaciones son las siguientes: "<<endl<<endl;
		cout<<"\t\t\t\t"<<a1<<"x+"<<a2<<"x2+"<<a3<<"x3="<<r1<<endl<<endl;
		cout<<"\t\t\t\t"<<b1<<"x+"<<b2<<"x2+"<<b3<<"x3="<<r2<<endl<<endl;
		cout<<"\t\t\t\t"<<c1<<"x+"<<c2<<"x2+"<<c3<<"x3="<<r3<<endl<<endl;
		
		determinante = (a1*((b2*c3)-(b3*c2)))-(a2*((b1*c3)-(b3*c1)))+(a3*((b1*c2)-(b2*c1)));
		
		if(determinante!=0)
		{
			cout<<"\tSi tienen convergencia pues el determinante es diferente de 0"<<endl<<endl;
			cout<<"\t\t\tEl determinante es: "<< determinante<<endl<<endl;
			
			x = ((r1*((b2*c3)-(b3*c2)))-(a2*((r2*c3)-(b3*r3)))+(a3*((r2*c2)-(b2*r3))))/determinante;
			
			y = ((a1*((r2*c3)-(b3*r3)))-(r1*((b1*c3)-(b3*c1)))+(a3*((b1*r3)-(r2*c1))))/determinante;
			
			z = ((a1*((b2*r3)-(r2*c2)))-(a2*((b1*r3)-(r2*c1)))+(r1*((b1*c2)-(b2*c1))))/determinante;
			
			cout<<"\t\tLas rectas convergen en: ("<<x<<","<<y<<","<<z<<")"<<endl<<endl;
		}
		else
		{
			cout<<"\t\t  El sistema no tiene solucion."<<endl<<endl;
			cout<<"\t\t\tEl determinante es: "<<determinante<<endl<<endl;
		}
					
	}
	else
		cout<<"El sistema ingresado tiene infinidad de soluciones o no tiene solucion."<<endl<<endl;

	
	system("pause");
}
