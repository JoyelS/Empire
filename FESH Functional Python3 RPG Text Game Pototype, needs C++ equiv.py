
#The Code Block Below is suggestions and notes.

#FESH, acronym for four options accesible form main menu (Fight,Exit,Shop,Hunt)
#Python 3 mockup, demonstration of concepts.
#██████████ Health Visualisation
#███████▒▒▒
# °º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,
#ADD TIME DELAY FOR ATTACK SEQUENCE
#ADD OPTION TO BUY MULTIPLE RINGS AT ONCE AND/OR MAKE EACH MORE EXPENSIVE THAN THE LAST
#IMPLEMENTATION OF SAVE CAPABILITIES (DataBase)
#Bugs out when inputting nothing, no string then enter hit enter without tpying anything.
#HUNT could include: Gather berries/ gain health, Find coin/ gain £, kill low level monster, pick up sellable item.
#Potential for Animal to inherit from monster or vice versa?
#When Hunting, Tally the meat in std:out

import sys
import random
import time

HuntDict={'Pig':[5,1,3],'Cow':[10,1,8],'Chicken':[3,1,1]}
#Dictionary of posisble huntable animals, the list value is [health, attack, meat] as integers, see the Animal and Monster classes.
MonsterDict={'Goblin':[5,1]}
#Dictionary of possible monsters, I've only put one in so far.

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

#This is just a long string piece of ASCII art, as our game is run on the command line, it's the closest we can get to graphics.


def main():
    '''IMPORTANT: This is the main game behaviour, as you can see the player is presented with four options, FIGHT, EXIT, SHOP & HUNT
    The player picks which module to run by typing the first letter, eg.) to Fight, a player inputs 'f'
    At-least programme a module, we can easily divide the workload like this. It will be easy to implement; If someone elses code does not work-
    IT WON'T effect yours or your grade'''
    
    USER.status()
    print('*'*50)
    print('[---PICK ONE---]')
    print('[F]ight   ---   ▬▬ι═══════> ')
    print('[E]xit   ---   ')
    print('[S]hop   ---   ')
    FESH=str(input('[H]unt?   ---   ˁ˚ᴥ˚ˀ\n')).lower()
    print('*'*50)
    if FESH[0]=='f':
        Fight(Monster)
    
    elif FESH[0]=='e':
        print('HAVE A GOOD DAY')
        sys.exit()

    elif FESH[0]=='s':
        Item.Sell_Inventory()

    elif FESH[0]=='h':
        Fight(Animal)
        
        
    
    else:
        print("'",FESH,"'",' is an INVALID command')
        main()

class Player:
    #A Player class, this will probably only be instantiated once as this is a single player game, Still - it is good to encapsulate things like this.
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
    #Simple Monster class, a new monster is Instantiated every time a player chooses to fight.
    #The class attribute LEVEL goes up by 1 every instantiation, the higher the level, the stronger the monster.
    Level=1
    def __init__(self):#add population? subclasses to add more exciting monsters.
        NAME=random.choice(list(MonsterDict.keys()))
        self.Name=NAME
        self.MaxHealth=(MonsterDict[NAME][0]*Monster.Level)
        self.Health=(MonsterDict[NAME][0]*Monster.Level)#Health scales linear
        self.Attack=(MonsterDict[NAME][1]+((Monster.Level-1)*(random.randint(0,3))))#Attack is a bit more volatile
        Monster.Level+=1

    def status(self):
        print('---',self.Name,' has ', self.Health,'/',self.MaxHealth,' Health... ')


class Animal:
    #Simple Animal Class, VERY SIMILAR to Monster, the class attribute Hunts has no bearing on the strength of the Animal though.
    #Hunts is just a recorded stat.
    Hunts=0
    def __init__(self):
        NAME=random.choice(list(HuntDict.keys()))#Random Key for animal dictionary
        self.Name=NAME
        self.Health=HuntDict[NAME][0]
        self.MaxHealth=HuntDict[NAME][0]
        self.Attack=HuntDict[NAME][1]
        self.Meat=HuntDict[NAME][2]
        Animal.Hunts+=1

    def status(self):
        print('---',self.Name,' has ', self.Health,'/',self.MaxHealth,' Health... ')
    

class Item:
    #This is essentially the SHOP module, It's more complicated, I don't really know how to explain it well in a breif comment.
    Inventory={}
    def __init__(self,name,quan,price,Att_Bonus,Health_Bonus):#If bonus evaluates as float, multiply, if int then add.
        self.Name=name
        self.Price=price
        self.Quan=quan#Quantity
        self.Att_Bonus=Att_Bonus
        self.Health_Bonus=Health_Bonus
        self.BuyKey=name[0].upper()

        Item.Inventory[self.BuyKey]=[self.Name,self.Quan,self.Price,
                                     self.Att_Bonus,self.Health_Bonus]#Add Item to inventory after Instantiation

    def Buy(Player):
        #This is not a pure function, it modifies attributes of objects outside of I/O
        #Adjusts Inventory Dictionary values and player stats if purchase is possible.
        BuyWhat0=str(input('What do you want to buy?'))#Preserve original for invalid commands
        BuyWhat=BuyWhat0[0].upper()
        #print(Item.Inventory[BuyWhat][2]) #Test to see it lands on price.
        if BuyWhat in Item.Inventory:
            if Player.Money>=(Item.Inventory[BuyWhat][2]):
                if Item.Inventory[BuyWhat][1]>0:
                    time.sleep(0.4)
                    
                    Player.Money-=Item.Inventory[BuyWhat][2]
                    Player.Attack+=Item.Inventory[BuyWhat][3]#Evaluate type to determine multiply or add.
                    Player.MaxHealth+=Item.Inventory[BuyWhat][4]
                    Player.Health+=Item.Inventory[BuyWhat][4]
                    Item.Inventory[BuyWhat][1]-=1
                    print(Player.Name,'BOUGHT the',Item.Inventory[BuyWhat][0],'for £',Item.Inventory[BuyWhat][2])

                    print('*'*50,'\n --- +',Item.Inventory[BuyWhat][3],'Attack!')
                    print(' --- +',Item.Inventory[BuyWhat][4],'Health!')
                    time.sleep(0.4)
                    main()
                else:
                    print(Item.Inventory[BuyWhat][0],'IS OUT OF STOCK')
                    main()
            else:
                print('*'*50)
                print(Player.Name,'can NOT AFFORD',Item.Inventory[BuyWhat][0])
                print('---',Player.Name,'HAS £',Player.Money,'---', Item.Inventory[BuyWhat][0],'COST £',Item.Inventory[BuyWhat][2],'---')
                print('*'*50,'\n')
                main()
        else:
            print('*'*50)
            print('Shop does not SELL',BuyWhat0)
            Item.Sell_Inventory()

    def BuyOrLeave():#Choose to Buy or Leave the shop.
        BuyOrLeave='x'
        while BuyOrLeave!='b' and BuyOrLeave!='l':
            BuyOrLeave=str(input('*'*50+'\n[B]uy or [L]eave?\n')).lower()[0]#could add sell.
            if BuyOrLeave=='l':
                print(USER.Name, 'LEFT the SHOP')
                main()
            elif BuyOrLeave=='b':
                #Go to Buy method in Item
                
                Item.Buy(USER)
            else:
                print('INVALID decision')
                Item.Sell_Inventory()
        

    def Sell_Inventory():#Creates a list/inventory of everything in the shop.
        print('---SHOP---')
        for KEY,VAL in Item.Inventory.items():   
            print('[',KEY,']','---',VAL[0],'---',VAL[1],'In STOCK --- £',VAL[2],'ea.')
        Item.BuyOrLeave()
        




def Fight(Foe):
    #The Fight Function/Module, this is called for both Hunt and Fight however Loot is handled differently for Animals and Monsters.
    Enemy=Foe()#should be random, perhaps a dictionary or list.
    print('LOOKING FOR A FIGHT',USER.Name,'FINDS A',Enemy.Name.upper(),'!!!\n'+'*'*50)
    Loot=random.randint(3,17)*Monster.Level#Random between primes to determine how much loot the monster drops.
    #print(Enemy.Health)#Test
    #print(USER.Health)#Test

    
    while Enemy.Health>0 and USER.Health>0:
        
        Enemy.status()
        Enemy.Health-=USER.Attack
        
        if Enemy.Health<=0:
            print('*'*50)
            print('▬▬ι══════════ﺤ',USER.Name,'ATTACKS and KILLs the ', Enemy.Name,'...')
            #Loots enemies, harvest animals, sells left over meat. Sort out USER.Status's
            if Foe==Monster:
                print('---',USER.Name,'finds £'+str(Loot),'by the',Enemy.Name+'!')
                USER.Money+=Loot
            elif Foe==Animal:#could append HuntsDict list to have 'egg', or 'beef' etc, which could be sold or eaten.
                MEAT=Enemy.Meat
                print(USER.Name,'harvests',str(Enemy.Meat),'LBs of meat from the',Enemy.Name)
                while USER.Health<USER.MaxHealth and MEAT>0:
                    time.sleep(0.4)
                    print(USER.Name,'Eats 1 pound of his',str(MEAT),'LBs of Meat..')#Could be random health, maybe even bad meat which is harmful
                    MEAT-=1
                    USER.Health+=1
                    if MEAT!=0:
                        USER.status()
                while MEAT>0 and USER.MaxHealth==USER.Health:
                    time.sleep(0.4)
                    MEAT-=1
                    print(USER.Name,'sells a pound of meat and gets £1!')
                    USER.Money+=1
                    if MEAT!=0:
                        USER.status()
            main()#BACK to main after a victory
            break
        print('▬▬ι═══════ﺤ',USER.Name, 'ATTACKS and does',USER.Attack,'damage.') 
        Enemy.status()
        print('\n')
        time.sleep(0.4)
        
        USER.Fight_Status()
        print('The ',Enemy.Name,' ATTACKS and does', Enemy.Attack,'damage. -═══════ι▬▬')
        USER.Health-=Enemy.Attack
        #THIS CALLS THE LARGE ASCII ART AT THE BEGGINING AND INITIATES A DEATH SEQUENCE
        if USER.Health<=0:
            print('The ', Enemy.Name,' ATTACKS and KILLS ', USER.Name,'...')
            print('*'*50)
            print('RIP in Pieces',USER.Name)
            print('---You Hunted',Animal.Hunts,'Animals---')
            print('---You DIED on level',Monster.Level-1,'---')
            print(USER.Name,'leaves behind £',USER.Money)
            print(DeathScreen)
            print('*'*50)
            break#Terminate code, script runs to end as game is over, USER is dead.

        USER.Fight_Status()
        print('\n')
        time.sleep(0.4)

#STORE
#Items in the SHOP are defined here, the do not neccessarily need to be defined here but they do need to be defined after the Item class.
Rings=Item('Magical Ring',5,10,random.randint(0,3),random.randint(0,3))#The numbers succeding Item name are STOCK,PRICE,ATTACK BONUS,HEALTH BONUS.
JackBoot=Item('Jack Boot',2,random.randint(5,25),2,random.randint(5,25))
Armour=Item('Armour',1,100,0,30)
Buckler=Item('Buckler',1,40,3,10)
Sword=Item('Sword',1,75,50,2)
Gauntlet=Item('Gauntlet',2,random.randint(5,25),2,random.randint(5,25))


#Similar Items such as armour or weapons can be easily defined here and should work
#make bonuses from rings random?


   
def Start():
    #RUN at the beggining of the game, called in the While loop immediatley below, this function queries for a username and the instantiated the USER as an object of the Player Class.
    print('---F-E-S-H---')
    Username=str(input('What is your name? \n '))
    USER=Player(Username,10,1,0)
    print('*'*50)
    
    return(USER)
    

    

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
