import random
import tkinter

ri=random.randint

#array that holds all the possible move ]s to make on a cube
sides=[('L', "L'", 'L2'),
       ('R', "R'", 'R2'),
       ('U', "U'", 'U2'),
       ('D', "D'", 'D2'),
       ('F', "F'", 'F2'),
       ('B', "B'", 'B2')]

#Main function... does all the work... generates the scrambles, etc...
def scrambler():
    global scramble
    scramble=''
    for i in range(0,20):
        global preva
        a=ri(0,len(sides)-1)
        if i ==10:
            scramble+='\n'
        if i!=0:
            if a!=preva:
                scramble+=sides[a][ri(0,2)]+' '
        else:
            scramble+=sides[a][ri(0,2)]+' '
        preva=a

#gui function... calls the main scrambler function, when the button is clicked...
def scrambler1():
    scrambler()
    label['text']=scramble

#gui function... calls the other gui function when <Enter> is pressed...
def scrambler2(event):
    scrambler1()
    
#*********** GUI **************
root=tkinter.Tk()

button=tkinter.Button(root,text='Scramble',command=scrambler1)
label=tkinter.Label(root,text='Click below or press \nEnter to get your scramble')
label.pack()
button.focus()
button.pack()
button.bind('<Return>',scrambler2)

root.mainloop()
