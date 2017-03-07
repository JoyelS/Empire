#include <iostream>
#include <string>

#include <unistd.h>//for sleep ability


using namespace std;

//unsigned int pause = 600000; //pause time in microseconds for engagement functions.

class CHARACTER{//CHARACTER CLASS, CAN BE USED GENERICALLY FOR ANIMALS, USERS, MONSTERS, ETC.
public:
    //default constructor.
    CHARACTER(string N="Default name", int H=10, int A=1, double M=0.01){
        name=N;
        health=H;
        attack=A;
        money=M;
    }

    void get_status()
    {cout<<name<<" has "<<health<<" health, "<<attack<<" attack & £"<<money<<endl;}

    void change_name(string new_name){
        name=new_name;
    }

    void change_health(int x){ //specified as non void in case it will be useful to produce a return.
        health+=x;
    }
    void change_attack(int x){ //specified as non void in case it will be useful to produce a return.
        attack+=x;
    }
    void change_money(double x){ //specified as non void in case it will be useful to produce a return.
        money+=x;
    }

    //variables to view private attributes.
    string get_name(){
        return name;
    }
    int get_health(){
        return health;
    }
    int get_attack(){
        return attack;
    }
    double get_money(){
        return money;
    }

private:
    string name;
    int health;
    int attack;
    double money;
};

//---------------------------------- END OF CHARACTER CLASS ----------------------------------
//Test creations of character objects.
CHARACTER user("a", 100,3,0.01);
CHARACTER goblin("GOBLIN",10,2,3.50);

//MENU FUNCTION:
string UserIn;//Declaration of user input for menu function.

void  menu()
{
user.get_status();

cout<<"[F]ight"<<endl<<"[E]xit"<<endl
<<"[S]hop"<<endl<<"[H]unt"<<endl;

cin>>UserIn;

UserIn=UserIn[0];
UserIn=tolower(UserIn[0]);

	if (UserIn=="f"){
		cout<<"FIGHT"<<endl;
		//SIMPLE FIGHT NEEDS ELABORATION. No loot, No max health etc.
		//Random loot would be good.
		cout<<user.get_name()<<" fights "<<goblin.get_name()<<endl;
        cout<<"------------------------------------------------"<<endl;
        goblin.get_status();

        cout<<"------------------------------------------------"<<endl;
        while (user.get_health()>0 &&goblin.get_health()>0){
            cout<<user.get_name()<<" attacks "<<goblin.get_name()<<" for "<<user.get_attack()<<endl;
            goblin.change_health(-1*user.get_attack());
            goblin.get_status();
            cout<<"------------------------------------------------"<<endl;

            if (goblin.get_health()>0){
                cout<<goblin.get_name()<<" attacks "<<user.get_name()<<" for "<<goblin.get_attack()<<endl;
                user.change_health(-1*goblin.get_attack());
                user.get_status();
                }
            usleep(600000);
            }
	}

	else if (UserIn=="s"){
		cout<<"SHOP"<<endl;

		user.change_money(1.00);
			}

	else if (UserIn=="e"){
		cout<<"EXIT"<<endl;
			}

	else if (UserIn=="h"){
		cout<<"HUNT"<<endl;
		user.change_health(1);
			}
	else{
		cout<<"INVALID INPUT"<<endl;
			}
}
//---------------------------------- END OF MENU FUNCTION ----------------------------------


int main(){

string Username;//User picks his name which is passed to the USER class, user should be checked in database to see if it exists, if so it should assume those stats.
cout<<"What is your Username? ";
cin>>Username;
cout<<"\nUsername is: "<<Username<<endl;
user.change_name(Username);

do{
    menu();
}while (UserIn!="e");
//exit();
return 0;
}
