from tkinter import *
import random

ri=random.randint
a=ri(0,100)
insults=['If this were a matter of life and death, \nyou\'d be dead by now.',
         'Are you a special kind of stupid?',
         'You Idiot',
         'You b$*pping piece of bl@*ping b*#p',
         'I know a can of Coke with a higher IQ than you.']
tries=0
def validate(ans):
    label['fg']='black'
    global tries
    global a
    global entry
    tries+=1
    if ans>a:
        label['text']='Too Big!!! \nTries:'+str(tries)
    elif ans<a:
        label['text']='Too Small \nTries:'+str(tries)
    else:
        label['fg']='green'
        label['text']="You're Correct...\nYou got it in "+str(tries)+" tries.\nGuess the new number I just generated..."
        a=ri(0,100)
        tries=0
    entry.delete(0,END)
def validate1():
    try:
        validate(int(entry.get()))
    except ValueError:
        label['fg']='red'
        label['text']=insults[ri(0,len(insults)-1)]+'\nNumbers!!! Only Numbers!!!'
    entry.delete(0,END)
def validate2(event):
    validate1()

#**********GUI************

root = Tk()
root.title("Guess The Number")
label=Label(root, text='Guess The Number I Just Generated\n (Between 1 and 100)')
entry=Entry(root)
entry.focus()
button=Button(root, text='Guess', command=validate1)
entry.bind('<Return>', validate2)
label.pack()
entry.pack()
button.pack()
root.mainloop()
