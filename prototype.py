#!/usr/bin/env python
# coding: utf-8

# In[32]:


import random

class Board:
    
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    zeros = []
    
    def __init__(self):
        self.board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.zeros = []
    
    def change(self, row, column, value):
        self.board[row][column] = value
        
    def reset(self):
        for i in range(4):
            for j in range(4):
                self.board[i][j] = 0
    
    def printBoard(self):
        for i in range(4):
            for j in range(4):
                print(str(self.board[i][j]) + " ",end = "")
            print("\n")
        print("\n")
    
    def countEmpty(self):
        for i in range(4):
            for j in range(4):
                if (self.board[i][j] == 0):
                    self.zeros.append([i,j])      
    
    def newNum(self):
        self.clearZero()
        self.countEmpty()
        z = len(self.zeros)
        i = self.zeros[random.randint(0,z-1)]
        n = 2*(random.randint(1,2))
        self.change(i[0],i[1],n)
        
    def clearZero(self):
        t = len(self.zeros)
        for i in range(t):
            self.zeros.pop()
        


# In[33]:


class Game:
    
    B = Board()
    L = ["LEFT","RIGHT","UP","DOWN"]
    
    def __init__(self):
        self.B = Board()
    
    def takeTurn(self):
        for i in range(4):
            self.B.newNum()
            self.shift(L[random.randint(0,3)])
            self.B.printBoard()
    
    def shift(self, direction):
        if(direction == "LEFT"):
            for row in range(1,4):
                


# In[34]:


G = Game()
G.takeTurn()


# In[ ]:




