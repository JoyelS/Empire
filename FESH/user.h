#pragma once
#include <iostream>
#include <string>

class USER {

	public:
	
	USER(std::string name ="name",int attack=1,int health=10,double money=0);


	std::string name;
	int attack;
	int health;
	double money;
	void display();
	
	private: //- I don't know if the user needs private attirbues.
	
	/*std::string Name;
	int Attack;
	int Health;
	double Money;*/
	};





