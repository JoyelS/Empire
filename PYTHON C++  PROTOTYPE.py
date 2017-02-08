#FESH, acronym for four options accesible form main menu (Fight,Exit,Shop,Hunt)
#Python 3 mockup, demonstration of concepts.
#██████████ Health Visualisation
#███████▒▒▒
# °º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,
#ADD TIME DELAY FOR ATTACK SEQUENCE
#ADD OPTION TO BUY MULTIPLE RINGS AT ONCE AND/OR MAKE EACH MORE EXPENSIVE THAN THE LAST
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
    print('*'*50)
    print('[CHOOSE]')
    print('[F]ight   ---   ▬▬ι═══════> ')
    print('[E]xit   ---   ')
    print('[S]hop   ---   ')
    FESH=str(input('[H]unt?   ---   ˁ˚ᴥ˚ˀ\n')).lower()
    print('*'*50)
    if FESH[0]=='f':
        Fight()
    
    elif FESH[0]=='e':
        sys.exit()

    elif FESH[0]=='s':
        Item.Sell_Inventory()

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

class Item:
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
                    Player.Money-=Item.Inventory[BuyWhat][2]
                    Player.Attack+=Item.Inventory[BuyWhat][3]#Evaluate type to determine multiply or add.
                    Player.MaxHealth+=Item.Inventory[BuyWhat][4]
                    Player.Health+=Item.Inventory[BuyWhat][4]
                    Item.Inventory[BuyWhat][1]-=1
                    print(Player.Name,'BOUGHT the',Item.Inventory[BuyWhat][0],'for £',Item.Inventory[BuyWhat][2])

                    print('*'*50,'\n --- +',Item.Inventory[BuyWhat][3],'Attack!')
                    print(' --- +',Item.Inventory[BuyWhat][4],'Health!')
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
        




def Fight():
    
    Enemy=Monster('Goblin')#should be random, perhaps a dictionary or list.
    print('LOOKING FOR A FIGHT',USER.Name,'FINDS A',Enemy.Name.upper(),'!!!\n'+'*'*50)
    Loot=random.randint(3,17)*Monster.Level#Random between primes to determine how much loot the monster drops.
    #print(Enemy.Health)#Test
    #print(USER.Health)#Test
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

#STORE

Rings=Item('Magical Ring',5,10,3,1)#make bonuses from rings random


   
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


