#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

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

int main()
{
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
		main();
			}

	else if (UserIn=="s"){
		cout<<"SHOP"<<endl;
		shop();
		main();
			}

	else if (UserIn=="e"){
		cout<<"EXIT"<<endl;
		exit();
			}

	else if (UserIn=="h"){
		cout<<"HUNT"<<endl;
		hunt();
		main();
			}
	else{
		cout<<"INVALID INPUT"<<endl;
		main();
			}
}
