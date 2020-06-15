
import random
import os

#import plugin named random


colors=["red", "green", "cross", "caro"] 
numbers=["seven","eight","nine","ten","J","Q","K","A"]
#This lists define values of cards


class Card :
    def __init__(self,color:"",number :"") :
        self.color = color
        self.number = number

    def show(self):
        print(self.color, self.number)

    def showWithIndex(self,i):
        print("    ", i, self.color, self.number)
#This functions are important to compare card to play    
    def isSameColor(self, card):
        if self.color==card.color:
            return True
        return False 
    def isSameNumber(self, card):
        if self.number==card.number:
            return True
        return False	        
class Player:
    def __init__(self,name:"") :
        self.name = name
        if self.name == "" :
            self.name = input("Whats is players name?  ")
        self.cards = []
    
#This function shows player his cards
    def show(self) :
        i = 0 
        for card in self.cards :
            card.showWithIndex(i)
            i = i + 1 
#This functions give player card
    def receive(self,card) : 
        self.cards.append(card)

    def play(self,binCard) :
        return none

class Human(Player) : 
    def __init__(self,name:"") :
        Player.__init__(self, name)

   
    def receive(self,card) : 
        Player.receive(self, card)

#This function define players play. 
    def play(self,binCard) :
        print(self.name, "> Your cards are:")
        Player.show(self)
        
        index = input("Which card do you want do play? : ")

#Here is program comparing players card and card in bin

        if 0 <= int(index) and int(index) < len(self.cards):  
            card = self.cards[int(index)]
            if card.isSameNumber(binCard) :
                self.cards.remove(card)
                return card
            elif card.isSameColor(binCard) :
                self.cards.remove(card)
                return card
        return None
class Computer(Player) :
    def __init__(self,name:"") :
        Player.__init__(self, name)
        if self.name == "" :
            self.name = input("Whats is bots name?  ")
    def receive(self,card) : 
        Player.receive(self, card)

# Here is program comparing bots card and card in bin
    def play(self,binCard) :
        for card in self.cards :
            if card.isSameNumber(binCard) :
                self.cards.remove(card)
                return card
            elif card.isSameColor(binCard) :
                self.cards.remove(card)
                return card
        return None
    
class Package :
#Program here is making game package, from which in the game will programm take cards
    def __init__(self) :
        self.cards=[]
        for num in range(0,8) :
            for col in range (0,4) :
                self.cards.append(Card(numbers[num], colors[col]))

    def show(self):
        for i in range (0,len(self.cards)) :
            self.cards[i].show()

class Bin :

#To the bin will players give their cards
    def __init__ (self) :
        self.cards=[]
    def getLast(self) :
        return self.cards[len(self.cards) - 1 ]
#This gives cards to bin/bin.push
    def push(self,card) :
        self.cards.append(card)

class Game :

#Class game is defining whole game process.

    def __init__ (self) :
        self.players=[]
        self.package=Package()
        self.bin=Bin()
    #Function addPlayer adds player to player list
    def addPlayer(self,player) :
        self.players.append(player)
    
#Function dealCards deal card to everyone
    def dealCards(self) :
        random.shuffle(self.package.cards)
        for i in range(0,4) :
            for player in self.players :
                card=self.package.cards.pop()
                player.receive(card)
        card=self.package.cards.pop()
        self.bin.push(card)
    def takeCard(self) :
        self = None
   
       

    def play(self) :

        while True :
            player = self.players.pop()
            binCard = self.bin.getLast()
            print("Top card in bin is :", end =" ")
            binCard.show()
            print("---------------------------------------")
            card=player.play(binCard)

            # player has proper card
            if card != None : 
                print("Player: ", player.name, "plays ...", end=" ")
                card.show()
                print("---------------------------------------")
                self.bin.push(card)
                #return a winner if he has no more cards
                if len(player.cards) <= 0 :
                    return player
            # player has not a proper card ...
            else :
                # in package no card, then is tie
                if len(self.package.cards) <= 0 :
                    return None

                # player gets card from package
                card=self.package.cards.pop()
                player.receive(card)
            #next player
            self.players.insert(0, player)
def Main():
    #Basic info about game
    print("   Welcome to my game")
    print("   In this game you have to throw into bin card with same value or color as in the bin.")
    print("   Who has no card in hand WINS.")
    print("   This game can be played from 2 to 5 players")
    howmanyHumans = input("How many players will play?  ")
    howmanyBots = input("How many bots do you want?  ")
    if int(howmanyBots) + int(howmanyHumans) > 5 :
        print("You cant have so many players")
        return 

    #add players
    game = Game()
    for count in range(0, int(howmanyHumans)) :
        game.addPlayer(Human(""))
    for count in range(0,int(howmanyBots)):
        game.addPlayer(Computer("Bot "+str(count)))

    print("-----------------------------------------")


    game.dealCards()

    result=game.play()
    #print the result
    if result== None :
        print("Tie!!!")
    else :
        os.system('color 4')
        print("The winner is " + result.name )

Main()


