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
		void update_attack(int x){
			attack=x;};
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
int fight(USER user){

    //static fight sequence, will only ever be against goblin, could be cloned for hunt, no loot or stat augmentation other than loss of health. To apply generally see python prototype.
    //Health of the user is not returned.

	cout<<"RUN FIGHT SEQUENCE"<<endl;
    USER goblin("Goblin",5,1,1.50);

    cout<<user.get_name()<<" fights "<<goblin.get_name()<<endl;
    cout<<"------------------------------------------------"<<endl;

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
    }


    //could use switch statements here.

    if (user.get_health()<0){
        cout<<user.get_name()<<" was killed."<<endl;
    }
    else{
        cout<<goblin.get_name()<<" was killed."<<endl;
    }
    return user.get_health();//returning altered variable does not work,
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

string UserIn;
void  menu(USER user)
{
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
			}

	else if (UserIn=="s"){
		cout<<"SHOP"<<endl;
		shop(user);
		user.change_money(0.01);
			}

	else if (UserIn=="e"){
		cout<<"EXIT"<<endl;
			}

	else if (UserIn=="h"){
		cout<<"HUNT"<<endl;
		hunt(user);
		user.change_health(1);
			}
	else{
		cout<<"INVALID INPUT"<<endl;
			}
}

int main(){

string Username;//User picks his name which is passed to the USER class, user should be checked in database to see if it exists, if so it should assume those stats.
cout<<"What is your Username? ";
cin>>Username;
cout<<"\nUsername is: "<<Username<<endl;

USER user(Username, 10,2,0.01);

do{
    menu(user);
}while (UserIn!="e");
exit();

//save user stats to database?

return 0;
}
