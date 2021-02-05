from tkinter import *

def oddCheck(n):
    if n%2==0:
        label.text=str(n)+'is even'
    else:
        label.text=str(n)+'is odd'
        
def oddCheck2():
    try:
        oddCheck(int(entry.get()))
    except ValueError:
        pass
    
##again='y'
##while again.lower()!='n':
##    try:
##        num=int(input('What\'s the number?\n'))
##        oddCheck(num)
##        again=input('Check again?\n')
##        while again.lower()!='y' and again.lower()!='n':
##            if again.lower()!='y' and again.lower()!='n':
##                again = input('Stop being a fool... Y or N\n')
##    except ValueError:
##        print('Come on, fool, think...\nIt checks numbers, not strings...')
##        again='y'
##********* GUI **********
        
root=Tk()

label=Label(root, text='Odd or even')
entry=Entry(root)
button=Button(root,text='Check whether its even', command=oddCheck2)
label.pack()
entry.pack()
button.pack()

root.mainloop()
