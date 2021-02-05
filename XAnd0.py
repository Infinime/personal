from tkinter import *
import random

moves=['X','0']
moved=0
won=''
player1Score=0
player2Score=0
turn='0'
gamemode=''

#Arguably the most important variable throughout the whole program...
#Stores the states of the grids, saves it for the validator
gri={ 't':['','',''],
      'm':['','',''],
      'b':['','','']
    }
b=['t0','t1','t2','m0','m1','m2','b0','b1','b2']
r=random.choice(b)

#lines variable for the single player... helps the program understand
#what is a win
lines=[ [gri['t'][0],gri['t'][1],gri['t'][2]],
        [gri['m'][0],gri['m'][1],gri['m'][2]],
        [gri['b'][0],gri['b'][1],gri['b'][2]],
        [gri['t'][0],gri['m'][0],gri['b'][0]],
        [gri['t'][1],gri['m'][1],gri['b'][1]],
        [gri['t'][2],gri['m'][2],gri['b'][2]],
        [gri['t'][0],gri['m'][1],gri['b'][2]],
        [gri['b'][0],gri['m'][1],gri['t'][2]],
      ]
lineHelp=[ ['t0','t1','t2'],
           ['m0','m1','m2'],
           ['b0','b1','b2'],
           ['t0','m0','b0'],
           ['t1','m1','b1'],
           ['t2','m2','b2'],
           ['t0','m1','b2'],
           ['b0','m1','t2'],
         ]
#Choose your destiny... Single or MultiPlayer
def destiChoose(chosen):
    global frame, label, b1, b2, canvas, moved, turn, gamemode
    
    #This is for multiplayer... As it was easier to code,
    #it is the first of the two modes.
    if chosen=='two':
        gamemode='multiplayer'
        frame.destroy()
        label2.destroy()
        single.destroy()
        multi.destroy()
        root.geometry('300x300')
        root.resizable(0,0)
        root.pack_propagate(0)
        canvas.pack()

        t0.place(x=0,y=0,relwidth=0.3,relheight=0.30)
        t1.place(x=96,y=0,relwidth=0.3,relheight=0.30)
        t2.place(x=196,y=0,relwidth=0.3,relheight=0.30)
        m0.place(x=0,y=101,relwidth=0.3,relheight=0.30)
        m1.place(x=96,y=101,relwidth=0.3,relheight=0.30)
        m2.place(x=196,y=101,relwidth=0.3,relheight=0.30)
        b0.place(x=0,y=191,relwidth=0.3,relheight=0.30)
        b1.place(x=96,y=191,relwidth=0.3,relheight=0.30)
        b2.place(x=196,y=191,relwidth=0.3,relheight=0.30)
        label.place(x=0,y=240)
        
        t0.bind('<Button-1>',t0f)
        t1.bind('<Button-1>',t1f)
        t2.bind('<Button-1>',t2f)

        m0.bind('<Button-1>',m0f)
        m1.bind('<Button-1>',m1f)
        m2.bind('<Button-1>',m2f)

        b0.bind('<Button-1>',b0f)
        b1.bind('<Button-1>',b1f)
        b2.bind('<Button-1>',b2f)
    
    #Single Player
    if chosen=='one':
        gamemode='singleplayer'
        frame.destroy()
        label2.destroy()
        single.destroy()
        multi.destroy()
        root.geometry('300x300')
        root.resizable(0,0)
        root.pack_propagate(0)
        canvas.pack()

        t0.place(x=0,y=0,relwidth=0.3,relheight=0.30)
        t1.place(x=96,y=0,relwidth=0.3,relheight=0.30)
        t2.place(x=196,y=0,relwidth=0.3,relheight=0.30)
        m0.place(x=0,y=101,relwidth=0.3,relheight=0.30)
        m1.place(x=96,y=101,relwidth=0.3,relheight=0.30)
        m2.place(x=196,y=101,relwidth=0.3,relheight=0.30)
        b0.place(x=0,y=191,relwidth=0.3,relheight=0.30)
        b1.place(x=96,y=191,relwidth=0.3,relheight=0.30)
        b2.place(x=196,y=191,relwidth=0.3,relheight=0.30)
        label.place(x=0,y=240)
        
        t0.bind('<Button-1>',t0f)
        t1.bind('<Button-1>',t1f)
        t2.bind('<Button-1>',t2f)

        m0.bind('<Button-1>',m0f)
        m1.bind('<Button-1>',m1f)
        m2.bind('<Button-1>',m2f)

        b0.bind('<Button-1>',b0f)
        b1.bind('<Button-1>',b1f)
        b2.bind('<Button-1>',b2f)

def compuPlay():
    global turn, moves, moved, won, player1Score, player2Score, gamemode
    global gri, lines, lineHelp
    lineRef=[ [t0,t1,t2],
              [m0,m1,m2],
              [b0,b1,b2],
              [t0,m0,b0],
              [t1,m1,b1],
              [t2,m2,b2],
              [t0,m1,b2],
              [b0,m1,t2],
            ]
    lines=[ [gri['t'][0],gri['t'][1],gri['t'][2]],
        [gri['m'][0],gri['m'][1],gri['m'][2]],
        [gri['b'][0],gri['b'][1],gri['b'][2]],
        [gri['t'][0],gri['m'][0],gri['b'][0]],
        [gri['t'][1],gri['m'][1],gri['b'][1]],
        [gri['t'][2],gri['m'][2],gri['b'][2]],
        [gri['t'][0],gri['m'][1],gri['b'][2]],
        [gri['b'][0],gri['m'][1],gri['t'][2]],
      ]
    for x in lines:
        #print('xinline')
        #print(x[0])
        if x[0]==x[1]=='X' and x[2]=='':
            print(10)
            griChange(lineHelp[lines.index(x)][2],lineRef[lines.index(x)][2])
            print(gri)
            break
        elif x[0]==x[2]=='X' and x[1]=='':
            print(20)
            griChange(lineHelp[lines.index(x)][1],lineRef[lines.index(x)][1])
            print(gri)
            break
        elif x[2]==x[1]=='X' and x[0]=='':
            print(21)
            griChange(lineHelp[lines.index(x)][0],lineRef[lines.index(x)][0])
            print(gri)
            break
        else:
            compuAttack()

emptyArr=[]

def compuAttack():
    global turn, moves, moved, won, player1Score, player2Score, gamemode
    global gri, lines, lineHelp, emptyArr
    lineRef=[ [t0,t1,t2],
              [m0,m1,m2],
              [b0,b1,b2],
              [t0,m0,b0],
              [t1,m1,b1],
              [t2,m2,b2],
              [t0,m1,b2],
              [b0,m1,t2],
            ]

    for x in lines:
        if x[0]==x[1]=='0' and x[2]=='':
            print('A10')
            griChange(lineHelp[lines.index(x)][2],lineRef[lines.index(x)][2])
            print(gri)
            break
        elif x[0]==x[2]=='0' and x[1]=='':
            print('A20')
            griChange(lineHelp[lines.index(x)][1],lineRef[lines.index(x)][1])
            print(gri)
            break
        elif x[2]==x[1]=='0' and x[0]=='':
            print('A21')
            griChange(lineHelp[lines.index(x)][0],lineRef[lines.index(x)][0])
            print(gri)
            break
        else:
            compuIdle()
            break

def compuIdle():
    global r,b,turn
    vaToLine={'t0':t0,'t1':t1,'t2':t2,'m0':m0,
    'm1':m1,'m2':m2,'b0':b0,'b1':b1,'b2':b2}
    pair = [(v, k) for (k, v) in vaToLine.items()]
    pairs=dict(pair)
    a=[t0,t1,t2,m0,m1,m2,b0,b1,b2]
    print(r,'compuIdle',vaToLine[r]['text'])
    if vaToLine[r]['text']=='':
        griChange(r,vaToLine[r])
    elif turn=='0':
        for x in a:
            if x['text']=='':
                griChange(pairs[x],x,'i')
                r=random.choice(b)
                break

#Changes the grid according to the input 
def griChange(square,move,i=''):
    '''square refers to the string, while move refers to it without apostrophes
    ; e.g. for move t1, the square would be "t1", and the move would be t1. 
    This is because I saved the grid as an array of arrays of labels, so it 
    makes some sense'''
    global gri, moved, lines, emptyArr, turn, gamemode
    if moved%2==0:
        turn='X'
    else:
        turn='0'
    if gri[str(square)[0]][int(str(square)[1])]=='':
        move['text']=turn
        gri[str(square)[0]][int(str(square)[1])]=turn
        wonCheck()
        moved+=1
        lines=[ [gri['t'][0],gri['t'][1],gri['t'][2]],
                [gri['m'][0],gri['m'][1],gri['m'][2]],
                [gri['b'][0],gri['b'][1],gri['b'][2]],
                [gri['t'][0],gri['m'][0],gri['b'][0]],
                [gri['t'][1],gri['m'][1],gri['b'][1]],
                [gri['t'][2],gri['m'][2],gri['b'][2]],
                [gri['t'][0],gri['m'][1],gri['b'][2]],
                [gri['b'][0],gri['m'][1],gri['t'][2]],
              ]

        if gamemode=='singleplayer' and turn=='X':
            compuPlay()

#Functions to call the griChange from the GUI
def t0f(self):
    griChange('t0',t0)
def t1f(self):
    griChange('t1',t1)
def t2f(self):
    griChange('t2',t2)
def m0f(self):
    griChange('m0',m0)
def m1f(self):
    griChange('m1',m1)
def m2f(self):
    griChange('m2',m2)
def b0f(self):
    griChange('b0',b0)
def b1f(self):
    griChange('b1',b1)
def b2f(self):
    griChange('b2',b2)
        
#Checks who won
def wonCheck():
    global won, gri
    global player1Score, player2Score
    if gri['t'][0]==gri['t'][1]==gri['t'][2]!='':
        won=gri['t'][0]

    elif gri['m'][0]==gri['m'][1]==gri['m'][2]!='':
        won=gri['m'][0]

    elif gri['b'][0]==gri['b'][1]==gri['b'][2]!='':
        won=gri['b'][0]

    elif gri['t'][0]==gri['m'][0]==gri['b'][0]!='':
        won=gri['t'][0]

    elif gri['t'][1]==gri['m'][1]==gri['b'][1]!='':
        won=gri['t'][1]

    elif gri['t'][2]==gri['m'][2]==gri['b'][2]!='':
        won=gri['t'][2]

    elif gri['t'][0]==gri['m'][1]==gri['b'][2]!='':
        won=gri['t'][0]

    elif gri['t'][2]==gri['m'][1]==gri['b'][0]!='':
        won=gri['t'][2]

    if won=='X':
        player1Score+=1
        t0['text']=''
        t1['text']=''
        t2['text']=''
        m0['text']=''
        m1['text']=''
        m2['text']=''
        b0['text']=''
        b1['text']=''
        b2['text']=''
        gri={'t':['','',''],
             'm':['','',''],
             'b':['','','']
            }
        won=''
    elif won=='0':
        player2Score+=1
        t0['text']=''
        t1['text']=''
        t2['text']=''
        m0['text']=''
        m1['text']=''
        m2['text']=''
        b0['text']=''
        b1['text']=''
        b2['text']=''
        gri={'t':['','',''],
             'm':['','',''],
             'b':['','','']}
        won=''
    label['text']='  X: '+str(player1Score)+' '*12+' O: '+str(player2Score)

    if gri['t'][0]!='' and gri['t'][1]!='' and gri['t'][2]!='' and gri['m'][0]!='' and gri['m'][1]!='' and gri['m'][2]!='' and gri['b'][0]!='' and gri['b'][1]!='' and gri['b'][2]!='':
        t0['text']=''
        t1['text']=''
        t2['text']=''
        m0['text']=''
        m1['text']=''
        m2['text']=''
        b0['text']=''
        b1['text']=''
        b2['text']=''
        gri={'t':['','',''],
             'm':['','',''],
             'b':['','','']}
        won=''
    turn='X'
        
#-----------------GUI------------------#
root=Tk()
root.title('X And 0')
root.resizable(0,0)

frame=Frame(root,background="White")
frame.pack()
label2=Label(frame,text='Choose Your Destiny',font=('Lucida Bright',20),
    background="White")
single=Button(frame,text='Single Player',font=('Lucida Calligraphy',30),
    background="Blue",command=lambda:destiChoose('one'))
multi=Button(frame, text='Multiplayer',font=('Lucida Calligraphy',30),
    background="Green",command=lambda:destiChoose('two'))
label2.pack()
single.pack(anchor='w',fill='x')
multi.pack(anchor="w",fill='x')

canvas=Canvas(root)
canvas.create_line(0,100,300,100)
canvas.create_line(0,190,300,190)
canvas.create_line(95,0,95,400)
canvas.create_line(195,0,195,400)

t0=Label(canvas,text=gri['t'][0],font=('Lucida Calligraphy',35))
t1=Label(canvas,text=gri['t'][1],font=('Lucida Calligraphy',35))
t2=Label(canvas,text=gri['t'][2],font=('Lucida Calligraphy',35))

m0=Label(canvas,text=gri['m'][0],font=('Lucida Calligraphy',35))
m1=Label(canvas,text=gri['m'][1],font=('Lucida Calligraphy',35))
m2=Label(canvas,text=gri['m'][2],font=('Lucida Calligraphy',35))

b0=Label(canvas,text=gri['b'][0],font=('Lucida Calligraphy',35))
b1=Label(canvas,text=gri['b'][1],font=('Lucida Calligraphy',35))
b2=Label(canvas,text=gri['b'][2],font=('Lucida Calligraphy',35))
label=Label(root,text='  X: '+str(player1Score)+' '*12+' O: '+str(player2Score)
            ,font=('Lucida Bright',20))

root.mainloop()
