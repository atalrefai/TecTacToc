#!/usr/bin/env python
# coding: utf-8

# In[15]:


import random


# In[16]:


board=[0,1,2,
       3,4,5,
       6,7,8]


# In[17]:


def TecTakToe_draw():
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])
    print()


# In[18]:


TecTakToe_draw()


# In[19]:


def Player_1():
    print("Please enter your location")
    location=int(input())
    if board[location]!='X' and board[location]!='0':
        board[location]='X'
    else:
        print("this spot is paken")


# In[20]:


Player_1()
TecTakToe_draw()


# In[21]:


def Player_2():
    print("Please enter your location")
    location=int(input())
    if board[location]!='X' and board[location]!='0':
        board[location]='O'
    else:
        print("this spot is paken")


# In[22]:


Player_2()
TecTakToe_draw()


# In[26]:


def check_winer(X_or_O):
    if board[0]==X_or_O and board[1]==X_or_O and board[2]==X_or_O:
        return True
    if board[3]==X_or_O and board[4]==X_or_O and board[5]==X_or_O:
        return True
    if board[6]==X_or_O and board[7]==X_or_O and board[8]==X_or_O:
        return True
    if board[0]==X_or_O and board[3]==X_or_O and board[6]==X_or_O:
        return True
    if board[1]==X_or_O and board[4]==X_or_O and board[7]==X_or_O:
        return True
    if board[2]==X_or_O and board[5]==X_or_O and board[8]==X_or_O:
        return True
    if board[0]==X_or_O and board[4]==X_or_O and board[8]==X_or_O:
        return True
    if board[2]==X_or_O and board[4]==X_or_O and board[6]==X_or_O:
        return True


# In[27]:


while True:
    Player_1()
    TecTakToe_draw()
    if check_winer('X')==True:
        print("Player 1 is winer")
        break;
    Player_2()
    TecTakToe_draw()
    if check_winer('O')==True:
        print("Player 1 is winer")
        break;


# In[ ]:




