#include <iostream>
#include <string>
#include <exception>
#include <ctime>
#include "libsqlite.hpp"
#include <unistd.h>//for sleep ability


using namespace std;

string scores="Stats.sqlite";

//Time function, uses ctime, returns the amount of seconds elapsed since jan 1, 1970 as an integer.
int time_int()
{
	time_t played = time(0);
	played = (int) played;//castiing time_t data structure as int.
	return played;
}

string date(){
// current date based on current system
	time_t played = time(0);

	tm *ltm = localtime(&played);

	string year= to_string(1900+(int)ltm->tm_year);
	string month=to_string(1+(int)ltm->tm_mon);
	string day=to_string((int)ltm->tm_mday);
	string date = year+"-"+month+"-"+day;//remove word year as seems to show as blob on sql.
	return date;
}

string time(){
//current time based on cuttent system
	time_t played = time(0);

	tm *ltm = localtime(&played);

	string hour = to_string(1+(int)ltm->tm_hour);
	string minute = to_string(1+(int)ltm->tm_min);
	string second = to_string(1+(int)ltm->tm_sec);
	string time = hour+":"+minute+":"+second;
	
	return time;
}


//---------------------------------- BEGGINING OF CHARACTER CLASS ----------------------------------

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

    void set_health(int x){  //Method to set value to same as in database. 
       health=x;
    }
    void set_attack(int x){ //Method to set value to same as in database.       
       attack=x;
    }
    void set_money(double x){  //specified as non void in case it will be useful to produce a return.
       money=x;
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

//Test creations of character objects. Objects should ideally be on a database. Use these o generate users, monsters, animals etc.
CHARACTER user("a", 100,3,0.01);
CHARACTER goblin("GOBLIN",10,2,3.50);

string UserIn;//Declaration of user input for menu function.

//---------------------------------- MENU FUNCTION  ----------------------------------
void  menu()
//allows user to dictate course of play with input (cin).
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
		CHARACTER goblin("GOBLIN",10,2,3.50);
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
            }//END OF FIGHT EXAMPLE CODE.

	}

	else if (UserIn=="s"){
		cout<<"SHOP"<<endl;
		//Tahmid Implement shop.
		user.change_money(1.00);
		//simple change money method, will increase relevant users money attribute.
			}

	else if (UserIn=="e"){
		cout<<"EXIT"<<endl;
			}

	else if (UserIn=="h"){
		cout<<"HUNT"<<endl;
		//Samuel and Joyel Implement fight and hunt.
		user.change_health(1);
		//simple health change method.
			}
	else{
		cout<<"INVALID INPUT"<<endl;
			}
}
//---------------------------------- END OF MENU FUNCTION ----------------------------------

//---------------------------------- DATA BASE FUNCTIONS  ----------------------------------

void LOG_play(CHARACTER x){//Log last game play.
	sqlite::sqlite db(scores);//Open database***
	
	auto cur = db.get_statement();
	try {
//	cur->reset();
	cur->set_sql("INSERT INTO game_LOG (chrono_int, date, time, username, user_action, att_save, hea_save, wea_save)"
	"VALUES(?,?,?,?,?,?,?,?);");
	cur->prepare();
	cur->bind(1,time_int());
	cur->bind(2,date());
	cur->bind(3,time());
	cur->bind(4,x.get_name());
	cur->bind(5,UserIn);
	cur->bind(6,x.get_attack());
	cur->bind(7,x.get_health());
	cur->bind(8,x.get_money());

	cur->step();
	cur->reset();
	}
	catch(std::exception& e) {
		std::cout << e.what() << std::endl;
	}
	//delete db;//Is this the corresponding close command***
}

void UPDATE_score(CHARACTER x){//Simple if/esle statement determines whether the user's username is in the database, if it is stats will be updated, if not the stats derived from the default constructor will be inserted as a new row.
	sqlite::sqlite db(scores);//Open database***
	
	auto cur = db.get_statement();
	try {
	cur->set_sql("SELECT count(*) FROM users where username=?;");
	cur->prepare();
	cur->bind(1,x.get_name());
	cur->step();
	if (cur->get_int(0) == 1) {
	//This first part uses the SQL to determine whethere this is a new user, if it is a user is created as an entry in the users table.
		cur->reset();
		cur->set_sql("UPDATE users SET attack=?,health=?,money=? where username=?");
		cur->prepare();
		cur->bind(1,x.get_attack());
		cur->bind(2,x.get_health());
		cur->bind(3,x.get_money());
		cur->bind(4,x.get_name());
		cur->step();
	} else {

		cur->reset();//CUR RESETS AFTER EACH QUERY.
		cur->set_sql("INSERT INTO users (username,health,attack,money)"
			"VALUES (?,?,?,?);");//Need 'or replace' type command, where identicle udernames are not enterred twice.

		cur->prepare();

		cur->bind(1,x.get_name());
		cur->bind(2,x.get_health());
		cur->bind(3,x.get_attack());
		cur->bind(4,x.get_money());

		cur->step();
	}
	}
	catch(std::exception& e) {
		std::cout << e.what() << std::endl;
	}
	//delete db;//Is this the corresponding close command***
}

int LOAD_user(CHARACTER * userValue) {//Load function, corresponding to update. If the username is in the database the user stats are ammended accordingly.
	int exists = 0;
	sqlite::sqlite db(scores);//Open database***
	auto cur = db.get_statement();
	cur->set_sql("SELECT count(*) FROM users where username=?;");
	
	cur->prepare();
	cur->bind(1,userValue->get_name());
	cur->step();
	exists = cur->get_int(0);
	cur->reset();
	
	if (exists == 1) {
		cout<<"	LOADING "<<userValue->get_name()<<"'s stats from the database..."<<endl;
		cur->set_sql("SELECT * FROM users WHERE username=?;");
		cur->prepare();
		cur->bind(1,userValue->get_name());
		cur->step();
		userValue->set_attack(cur->get_int(1));//0 reading? get_int, value (1) should be primary key username!?*****!!!!!!!!
		userValue->set_health(cur->get_int(2));
		userValue->set_money(cur->get_double(3));
		cur->reset();
	}
	else{
		cout<<"	CREATING: '"<<userValue->get_name()<<"' as a new user."<<endl;
	}

	return 0;
}

void PRINT_UserHis(CHARACTER x){
	//User Record, prints user record to screen.
	try{
	sqlite::sqlite db(scores);
	auto cur = db.get_statement();
	cur->set_sql("SELECT count(*) FROM game_LOG  WHERE username=?");

	cur->prepare();
	cur->bind(1, x.get_name());
	cur->step();
	int plays=cur->get_int(0);
	cout<<x.get_name()<< " has played "<<plays<<" actions."<<endl<<endl;
	cur->reset();
	//works fine to here.
	cur->set_sql("SELECT date,time,user_action FROM game_LOG where username=?");
	
	cur->prepare();
	cur->bind(1, x.get_name());
	cur->step();
	
	for (int PlayNum=1; PlayNum<=plays; PlayNum++){
		//string time = cur->get_text(1);
		string act = cur->get_text(2);
		
		
		if (act=="f"){act="fought";}
		else if (act=="e"){act="left the session";}
		else if (act=="s"){act="shopped";}
		else if (act=="h"){act="hunted";}
		cout<<"On : "<<cur->get_text(0)<<" at : "<<cur->get_text(1)<<" | ";
		cout<<" For Play "<<PlayNum<<", "<<x.get_name()<<" "<<act<<"."<<endl;
		cout<<" --- --- --- ---"<<endl;

		
/*		string date = cur->get_text(0);
		string time = cur->get_text(1);
		string action = cur->get_text(2);
		
		cout<<action<<endl; */
		//cout<<"On : "<<date<<", At : "<<time<<" --- "<<x.get_name()<<" "<<action<<"."<<endl;
		cur->step();
	}
	cur->reset();
	
	
	}
	catch(sqlite::exception e){
	std::cerr<<e.what()<<endl;
	}

}

//---------------------------------- END OF DATA BASE FUNCTIONS  ----------------------------------

int main(){

string Username;//User picks his name which is passed to the USER class, user should be checked in database to see if it exists, if so it should assume those stats.
cout<<"What is your Username? ";
cin>>Username;
cout<<"\nUsername is: "<<Username<<endl;
user.change_name(Username);
cout<<"Date: "<<date()<<", Time: "<<time()<<" UTC+1"<<endl;
LOAD_user(&user);
	
do{
	//do loop which keeps the game running unless the player has decided to exit.
	menu();
	UPDATE_score(user);
	LOG_play(user);
	usleep(1500000);
}while (UserIn!="e");
	
cout<<"Would you like to view "<<user.get_name()<<"'s game records?"<<endl;
cout<<"[Y]es/[N]o"<<endl;
string Viewd;
cin>>Viewd;

Viewd=Viewd[0];
Viewd=tolower(Viewd[0]);
if (Viewd=="y"){
	PRINT_UserHis(user);
	}
else{cout<<"Session ended."<<endl;}
cout<<"Continue Playing?"<<endl;
cout<<"[Y]es/[N]o"<<endl;
string Playd;
cin>>Playd;

Playd=Playd[0];
Playd=tolower(Playd[0]);
if (Viewd=="y"){
	main();
	}
else{cout<<"Game Ended."<<endl;}
//exit();
return 0;
}

