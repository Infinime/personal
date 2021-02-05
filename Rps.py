from tkinter import *
from random import randint as ri
import random
#Some general variables for the whole program... Might be seen
#scattered throughout the rest of the program as globals for my functions...

#Defines what will beat what... Keys are the better of the pair...
possmoves={'rock':'scissors','paper':'rock','scissors':'paper'}
#Same as the above... Values are the better of the pair...
movesposs={'rock':'paper','paper':'scissors','scissors':'rock'}
#Array of all of the possibly playable moves
possimoves=['rock', 'paper', 'scissors']
#Player's Score
playerscore=0
#Computer's Score
compuscore=0
playermove=''
compmove=''
#Difficulty
diff=''
#Array of the player's past moves... For the medium and hard difficulties
playerpastmoves=[]
#Number of turns
played=0
#Dictionary... For Medium and Hard
dict1={'rock':0,'paper':0,'scissors':0}

#This section defines the entire gameplay environment
def comp(level):
    global diff, playerscore,compuscore,score,result,moves
    again=0
    diff=level
    choose.grid_forget()
    beasy.grid_forget()
    bmed.grid_forget()
    bhard.grid_forget()
    score.pack()
    moves.pack()
    result.pack()

#This section defines the functions for all the levels
def playe(move):
    global playermove,playermoves,compmove, playerscore,compuscore
    global score,result,moves, dict1, diff,played, playerpastmoves, possimoves
    move=move.lower()
    dict1['rock']=0
    dict1['paper']=0
    dict1['scissors']=0
    for x in playerpastmoves:
        dict1[x]+=1;

    #Moves
    if move=='r': playermove='rock'
    elif move=='p': playermove='paper'
    else: playermove='scissors'

    #-----------------------Levels-------------------------------#
    #Easy
    if diff=='easy': compmove=possimoves[ri(0,len(possimoves)-1)]
    
    #Medium
    elif diff=='medium':
        if played==1:
            compmove=possimoves[ri(0,len(possimoves)-1)]
            played+=1
            playerpastmoves+=[playermove]
        else:
            if len(playerpastmoves)<3:
                playerpastmoves+=[playermove]
            else:
                playerpastmoves.pop(0)
                playerpastmoves+=[playermove]
            chosen=max(zip(dict1.values(),dict1.keys()))[1]
            compmove=movesposs[chosen]
            played+=1
            print(played, end=',')
            
    #Hard
    else:
        if not played%ri(1,5)==0:
            if playermove=='rock':
                compmove=random.choice(['paper','rock'])
            if playermove=='scissors':
                compmove=random.choice(['rock','scissors'])
            if playermove=='paper':
                compmove=random.choice(['paper','scissors'])
        else:
            compmove=random.choice(['rock','paper','scissors'])
        played+=1

    #Checks who won; player or computer
    mover=[compmove,playermove]
    res=winner(compmove,playermove)
    moves['text']=playermove.title()+' '*40+compmove.title()
    if res!='Draw':
        if mover.index(res)==0:
            compuscore+=1
        else:
            playerscore+=1
        score['text']='Player'+' '*6+str(playerscore)+'  -  '+str(compuscore)+'    Computer'

#These functions are the ones called by the bindings later on in the code
def playeR(self):
    playe('r')
def playeP(self):
    playe('p')
def playeS(self):
    playe('s')
    
#Main validator function...
def winner(move1,move2):
    move1=move1.lower()
    move2=move2.lower()
    if possmoves[move1]==move2:
        won=move1
    elif move1==move2:
        won='Draw'
    else:
        won=move2
    return won

#-------------------------------------------GUI---------------------------------------------------#
root=Tk()
root.title('Rock, Paper, Scissors')
root.bind('<r>',playeR)
root.bind('<p>',func=playeP)
root.bind('<s>',func=playeS)
root.bind('<R>',func=playeR)
root.bind('<P>',func=playeP)
root.bind('<S>',func=playeS)

#Main body/frame... Mainly to just set the size of the window
frame=Frame(root,width=300,height=270,bg='White')
frame.pack()

choose=Label(frame, text='Choose Your Destiny',font=('Lucida Bright',13,'bold'),bg='White')
choose.grid(columnspan=3)

beasy=Button(frame, text='Easy',bg='Green',font=('Lucida Bright',13,'bold'), command=lambda:comp('easy'))
bmed=Button(frame, text='Medium',bg='Yellow',font=('Lucida Bright',13,'bold'),command=lambda:comp('medium'))
bhard=Button(frame, text='Hard',bg='Red',font=('Lucida Bright',13,'bold'),command=lambda:comp('hard'))
beasy.grid(columnspan=3,sticky='EW')
bmed.grid(columnspan=3,sticky='EW')
bhard.grid(columnspan=3,sticky='EW')

moves=Label(frame,bg='White',font=('Lucida Bright',13,'bold'))
result=Label(frame,bg='White',text='Use the Keyboard to play; Press R for Rock,\nP for Paper and S for Scissors',font=('Lucida Bright',13,'bold'))
score=Label(frame,bg='White',text='Player'+' '*6+str(playerscore)+'  -  '+str(compuscore)+'    Computer',font=('Lucida Bright',15,'bold'))

root.mainloop()
