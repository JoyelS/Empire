#FESH, acronym for four options accesible form main menu (Fight,Exit,Shop,Hunt)
#Python 3 mockup, demonstration of concepts.
#██████████ Health Visualisation
#███████▒▒▒
# °º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,

import sys
import random

DeathScreen="""
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     -YOU LOST FESH-
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`"""


def main():
    
    USER.status()
    print('[CHOOSE]')
    print('[F]ight   ---   ▬▬ι═══════> ')
    print('[E]xit   ---   ')
    print('[S]hop   ---   ')
    FESH=str(input('[H]unt?   ---   ˁ˚ᴥ˚ˀ\n')).lower()
    if FESH[0]=='f':
        Fight()
    
    elif FESH[0]=='e':
        sys.exit()

    elif FESH[0]=='s':
        pass#Shop()

    elif FESH[0]=='h':
        pass#Hunt()
    
    else:
        print("'",FESH,"'",' is an INVALID command')
        main()

class Player:
    def __init__(self,name,health,attack,money):
        self.Name=name
        self.Health=health
        self.MaxHealth=health
        self.Attack=attack
        self.Money=money

    def status(self):
        print('---',self.Name,' has ', self.Health,'/',self.MaxHealth,' Health, ',self.Attack,' Attack, and £',self.Money,'...')

    def Fight_Status(self):
        print('---',self.Name,' has ',self.Health,'/',self.MaxHealth,' Health')
        
class Monster:
    Level=1
    def __init__(self,name):#add population? subclasses to add more exciting monsters.
        self.Name=name
        self.Health=5*Monster.Level
        self.Attack=Monster.Level
        Monster.Level+=1

    def status(self):
        print('---',self.Name,' has ', self.Health,' Health... ')
        

def Fight():
    
    Enemy=Monster('Goblin')#should be random, perhaps a dictionary or list.
    print('LOOKING FOR A FIGHT',USER.Name,'FINDS A',Enemy.Name.upper(),'!!!\n'+'*'*50)
    Loot=random.randint(3,17)*Monster.Level#Random between primes to determine how much loot the monster drops.
    print(Enemy.Health)#Test
    print(USER.Health)#Test
    while Enemy.Health>0 and USER.Health>0:
        
        Enemy.status()
        Enemy.Health-=USER.Attack
        if Enemy.Health<=0:
            print('*'*50)
            print(USER.Name,'ATTACKS and KILLs the ', Enemy.Name,'...')
            print(USER.Name,'finds £'+str(Loot),'by the',Enemy.Name+'!!!')
            USER.Money+=Loot
            
            main()#BACK to main after a victory
            break
        print(USER.Name, ' ATTACKS...') 
        Enemy.status()
        print('\n')
        
        USER.Fight_Status()
        print('The ',Enemy.Name,' Attacks...')
        USER.Health-=Enemy.Attack
        if USER.Health<=0:
            print('The ', Enemy.Name,' ATTACKS and KILLS ', USER.Name,'...')
            print('*'*50)
            print('RIP in Pieces',USER.Name)
            print(DeathScreen)
            print('*'*50)
            #while Replay!='y' and Replay!='n':

            break#Terminate code, script runs to end as game is over, USER is dead.

        USER.Fight_Status()
        print('\n')

    
def Start():
    print('---F-E-S-H---')
    Username=str(input('What is your name? \n '))
    USER=Player(Username,10,1,0)
    print('*'*50)
    
    return(USER)
    #main()

    

Play='Yes'
while Play.lower()[0]=='y':
    USER=Start()
    Monster.Level=1#This may cause problems for event driven.
    main()
    
    Play=str(input('Play Again? [Y]es/[N]o \n '))
    if Play.lower()[0]!='y':
        sys.exit
#reursive, put four options in main funciton and then call it.
#menu()

#CLASS WOULD ALLOW ATTRIBUTES TO BE EDITED. EVENT DRIVEN WITHOUT A GUI
'''
#A CLASS


class Dog:

    nameList = []

    def __init__(self, name, age):
        if name in Dog.nameList:
            raise ValueError('That name is already taken')
        self.__name = name
        self.age = age
        Dog.nameList.append(name)

    def readCollar(self):
        return(self.__name)

    def speakAge(self):
        print('Woof '*self.age)

    def howManyDogs():
        return( len(Dog.nameList) )'''

