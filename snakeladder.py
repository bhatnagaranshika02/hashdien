import random
import time
from os import system,name
class player:
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2
        self.pos1=0
        self.pos2=0

    def clear(self):
        if name == "nt":
            _ = system("cls")

    def cls(self):
        print("\n"*100)

    def roll_dice(self):
        die = random.choice([1,2,3,4,5,6])
        return die

    def Turn1(self):
        answer = self.roll_dice()
        if self.pos1+answer>100:
            print("MOve not possible")
            return self.pos1
        self.pos1 += answer
        if self.pos1 in snakes:
            print(player1," beaten by snake at position:",self.pos1)
            self.pos1 = snakes[self.pos1]
        if self.pos1 in ladders:
            print("Congratulations!!",player1,", found a ladder at position:",self.pos1)
            self.pos1 = ladders[self.pos1]
        return self.pos1

    def Turn2(self):
        answer = self.roll_dice()
        if self.pos2+answer>100:
            print("Move not possible.")
            return self.pos2
        self.pos2 += answer
        if self.pos2 in snakes:
            print(player2, " beaten by snake at position:",self.pos2)
            self.pos2 = snakes[self.pos2]
        if self.pos2 in ladders:
            print("Congratulations!!",player2, " found a ladder at position:",self.pos2)
            self.pos2 = ladders[self.pos2]
        return self.pos2 
    
    def solution(self,snakes,ladders):
        value=value1=0
        while value!=100 or value!=100:
            time.sleep(5)
            #For commandPrompt self.clear()
            self.cls()
            print("*********************************************************\nWaiting for ",player1)
            value = self.Turn1()
            if value != 100:
                print(f"player1 is at position:{value}")
            else:
                print(player1," is the winner")
                break
            print("Waiting for ",player2)
            value2=self.Turn2()
            if value2 !=100:
                print(f"player2 is at position:{value2}")
            else:
                print(player2," is the winner.")
                break
        return None

player1=input()
player2=input()
snakes={}
y=int(input())
for i in range(y):
    m,n=map(int,input().split())
    snakes[m]=n
ladders={}
z=int(input())
for i in range(z):
    m,n=map(int,input().split())
    ladders[m]=n


obj1 = player(player1,player2)
obj1.solution(snakes,ladders)
















