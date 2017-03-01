//Potential database tables for user stats, shop inventory and enemies (animals and monsters) - Ideally one table for each on the same database.
//Contains 'main menu' function, fight, exit, shop and hunt modules can be localised or even better made in other files. To localise them, simply elaborate on the respective void functions.

#include "user.h"

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

USER::USER (string,int,int,double){
	this->name = "test";
	this->attack = 7;
	this->health = 10;
	this->money = 0;

}

void USER::display() {

cout<<this->health<<endl;

}

void fight(){

	cout<<"RUN FIGHT SEQUENCE"<<endl;
}

void exit(){

	cout<<"RUN EXIT SEQUENCE"<<endl;
}

void hunt(){

	cout<<"RUN HUNT SEQUENCE"<<endl;
}

void shop(){//Changed int for void

	cout<<"RUN SHOP SEQUENCE"<<endl;
}

void menu(){
string UserIn;

cout<<"[F]ight"<<endl<<"[E]xit"<<endl
<<"[S]hop"<<endl<<"[H]unt"<<endl;

cin>>UserIn;

//transform(UserIn.begin(),UserIn.end(),UserIn.begin(),::tolower);


UserIn=UserIn[0];
UserIn=tolower(UserIn[0]);

	if (UserIn=="f"){
		cout<<"FIGHT"<<endl;
		fight();
		menu();
			}

	else if (UserIn=="s"){
		cout<<"SHOP"<<endl;
		shop();
		menu();
			}

	else if (UserIn=="e"){
		cout<<"EXIT"<<endl;
		exit();
			}

	else if (UserIn=="h"){
		cout<<"HUNT"<<endl;
		hunt();
		menu();
			}
	else{
		cout<<"INVALID INPUT"<<endl;
		menu();
			}
}

int main()
{
USER user;
user.display();
menu();
return 0;
}
