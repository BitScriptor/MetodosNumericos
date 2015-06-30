#include<iostream>
#include<stdlib.h>

using namespace std;

void primeraOpcion()
{	
	system("cls");
	int ecuaciones=0;
	
		cout<<endl;			
		cout<<"\t\tCuantas ecuaciones ingresaras?: ";
			cin>> ecuaciones;
		if(ecuaciones == 1)
			cout<<"Debes ingresar al menos dos ecuaciones para realizar la evaluacion" << endl;
						
		else if(ecuaciones == 2)//se determina cuantas ecuaciones se ingresaran
		{
			float m1=0, b1=0, m2=0, b2=0, x=0, y=0;
						
			cout<<endl<<endl<<"\t\tIntroduce los valores de m1, b1, m2, b2"<<endl<<endl;
			cout<<"\t\t\t\tm1: ";
				cin>>m1;
			cout<<"\t\t\t\tb1: ";
				cin>>b1;
			cout<<"\t\t\t\tm2: ";
				cin>>m2;
			cout<<"\t\t\t\tb2: ";
				cin>>b2;
			cout<<endl<<endl<<"\t\t\tTus ecuaciones son: " << endl << endl << "\t\t\t\t y="<<m1<<"x+"<<b1<<endl<<endl;
			cout<<"\t\t\t\t y="<<m2<<"x+"<<b2<<endl<<endl<<endl;
						
			if(m1==m2 && b1==b2)//se evaluan las ecuaciones y las condiciones
			{
				cout<<"\t    Son la misma recta, por lo tanto tiene infinidad de soluciones."<<endl<<endl<<endl;
			}
			else if(m1==m2)
			{
				cout<<"\t    Las rectas son paralelas, por lo tanto no hay convergencia"<<endl<<endl<<endl;
			}
			else
			{
				/*IGUALAMOS LAS DOS ECUACIONES
					 m1x + b2 = m2x + b2
							    
				DESPEJAMOS
					 m1x - m2x = b2 - b1
							   
					 x = (b2 - b1) / (m1 - m2)
							     
				SUSTITUIMOS EN CUALQUIERA DE LAS ECUACIONES ORIGINALES
					 y = m1((b2 - b1)/(m1 - m2) + b1	*/
				x = (b2 - b1)/(m1 - m2);
				y = (m1*(x))+ b1;
							
				cout<<"\t\tEl punto de convergencia es en ("<<x<<","<<y<<")"<<endl<<endl<<endl;
			}
		}
		else if(ecuaciones == 3)
		{
				float m1=0, b1=0, m2=0, b2=0, m3=0, b3=0, x=0, y=0;
				float x1=0, y1=0, x2=0, y2=0, x3=0, y3=0;
						
				cout<<endl<<endl<<"\t\tIntroduce los valores de m1, b1, m2, b2, m3, b3"<<endl<<endl;
				cout<<"\t\t\t\tm1: ";
					cin>>m1;
				cout<<"\t\t\t\tb1: ";
					cin>>b1;
				cout<<"\t\t\t\tm2: ";
				    cin>>m2;
				cout<<"\t\t\t\tb2: ";
					cin>>b2;
				cout<<"\t\t\t\tm3: ";
					cin>>m3;
				cout<<"\t\t\t\tb3: ";
					cin>>b3;
						 	  
				cout<<endl<<endl<<"\t\t\tTus ecuaciones son: " << endl << endl;
				cout<<"\t\t\t\t y="<<m1<<"x+"<<b1<<endl;
				cout<<"\t\t\t\t y="<<m2<<"x+"<<b2<<endl;
				cout<<"\t\t\t\t y="<<m3<<"x+"<<b3<<endl<<endl<<endl;
						
				if((m1==m2 && b1==b2) || (m2 == m3 && b2 == b3) || (m1==m3 && b1==b3))//se evaluan las ecuaciones y las condiciones
				{
					cout<<"Dos o mas ecuaciones son la misma recta, por lo tanto no hay convergencia entre las tres rectas."<<endl;
					cout<<endl<<endl;
				}
				else if((m1==m2) || (m2 == m3) || (m1==m3))
				{
					cout<<"Una de las rectas es paralela a otra, por lo tanto no hay convergencia"<<endl<<"   entre las tres rectas."<<endl;
					cout<<endl<<endl;
				}
				else
				{
					/*IGUALAMOS LAS DOS ECUACIONES
						 m1x + b2 = m2x + b2
							    
					DESPEJAMOS
						 m1x - m2x = b2 - b1
							   
						x = (b2 - b1) / (m1 - m2)
							     
					SUSTITUIMOS EN CUALQUIERA DE LAS ECUACIONES ORIGINALES
						y = m1((b2 - b1)/(m1 - m2) + b1	*/
					x1 = (b2 - b1)/(m1 - m2);
					y1 = (m1*(x))+ b1;
								
					x2 = (b3 - b2)/(m2 - m3);
					y2 = (m2*(x2))+b2;
								
					x3 = (b3 - b1)/(m1 - m3);
					y3 = (m1*(x3))+b1;
								
					if(x1==x2 && x2==x3 && x1==x3)
					{
						x = x1;
						y = y1;
						cout<<"\t\tEl punto de convergencia de las tres rectas es en: ("<<x<<","<<y<<")"<<endl<<endl<<endl;	
					}
					else
					{
						cout<<"\t\t  Las tres rectas no convergen en el mismo punto"<<endl<<endl;
					}
							
				}
						 
		}
		system("pause");
		system("cls");
}
