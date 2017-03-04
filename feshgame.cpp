#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class USER{
	public:
	
		//Default constructor
		USER(string name, int h, int a, double m){
			change_name(name);
			health=h;
			attack=a;
			money=m;
			/*change_health(health);
			change_attack(attack);
			change_money(money);*/
			
			}

		//Methods to change and retreive/view name.
		void change_name(string NewName){
			name=NewName;
			}
		string get_name(){
			return name;
			}
		//Methods to change and retreive attack.
		void change_attack(int x){//made an int to test method to permanantly modify value.
			this->attack+=x;
			//return this->attack;
		
			}

		void update_attack(){
			attack=1;};
		int get_attack(){
			return attack;
			}
		//Methods to change and retreive health.
		void change_health(int x){
			health+=x;
			}
		int get_health(){
			return health;
			}
		//Methods to change and retreive money value.
		void change_money(double x){
			money+=x;
			}
		double get_money(){
			return money;
			}
		//Method to get status of USER.
		void get_status(){
			cout<<name<<" has "<<health<<" health, "<<attack<<" attack & £"<<money<<endl;
}
	private:
		string name;
		int health;
		int attack;
		double money;

};
void fight(USER user){

	cout<<"RUN FIGHT SEQUENCE"<<endl;
	
	user.change_attack(1);
}

void exit(){
//User details should be committed to database here.
	cout<<"RUN EXIT SEQUENCE"<<endl;
}

void hunt(USER user){
	
	cout<<"RUN HUNT SEQUENCE"<<endl;
	user.get_status();
	user.change_health(1);
//testing, as user attributes can not be changed from these functions for some reason.
//DOES CHANGE JUST DOESN'T PERMANANTLY MODIFY VALUE, PERHAPS THE CHANGE NEEDS TO BE RETURNED? 
	//return user; ---What type of funciton could return an object? or do they need to be methods of user?
	user.get_status();
}

void shop(USER user){//Changed int for void

	cout<<"RUN SHOP SEQUENCE"<<endl;
}

void  menu(USER user)
{
string UserIn;

user.get_status();

cout<<"[F]ight"<<endl<<"[E]xit"<<endl
<<"[S]hop"<<endl<<"[H]unt"<<endl;

cin>>UserIn;

//transform(UserIn.begin(),UserIn.end(),UserIn.begin(),::tolower);


UserIn=UserIn[0];
UserIn=tolower(UserIn[0]);

	if (UserIn=="f"){
		cout<<"FIGHT"<<endl;
		fight(user);//Fight and other modules should return values which are used to alter user stats.
	
		//user.update_attack(); - update_attack can be used to set attack to a specific value, change_attack is used to alter it by the agument.
		//user.get_status(); - for testing.

		user.change_attack(1);//for example here attack is increased by 1.
		menu(user);
			}

	else if (UserIn=="s"){
		cout<<"SHOP"<<endl;
		shop(user);
		user.change_money(0.01);
		menu(user);
			}

	else if (UserIn=="e"){
		cout<<"EXIT"<<endl;
		exit();
			}

	else if (UserIn=="h"){
		cout<<"HUNT"<<endl;
		hunt(user);
		user.change_health(1);
		menu(user);
			}
	else{
		cout<<"INVALID INPUT"<<endl;
		menu(user);
			}
}

int main(){

string Username;//User picks his name which is passed to the USER class, user should be checked in database to see if it exists, if so it should assume those stats.
cout<<"What is your Username? ";
cin>>Username;
cout<<"\nUsername is: "<<Username<<endl;

USER user(Username, 10,5,0.01);

menu(user);
return 0;
}
