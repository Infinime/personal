from tkinter import *

#Working variables
num1=0
num2=0
worker=''

#Function to insert number into entry
def insNum(number):
    entry.insert(len(entry.get()),number)

#Function to calculate all the operations
def test2(fun):
    global num1
    global num2
    global worker
    if fun=='=':
        num2=float(entry.get())
        entry.delete(0,END)
        if worker=='+':
            entry.insert(0,str(num1+num2))
    
        if worker=='-':
            entry.insert(0,str(num1-num2))

        if worker=='*':
            entry.insert(0,str(num1*num2))

        if worker=='/':
            entry.insert(0,str(num1/num2))
    else:
        worker=fun
        num1=float(entry.get())
        entry.delete(0,END)

#Division binder function        
def tdiv(self):
    entry.delete(len(entry.get())-1,END)
    test2('/')

#Equals-to binder
def teq(self):
    test2('=')

#Times binder    
def ttim(self):
    entry.delete(len(entry.get())-1,END)
    test2('*')

#Minus binder    
def tmin(self):
    entry.delete(len(entry.get())-1,END)
    test2('-')

#Plus binder    
def tplus(self):
    entry.delete(len(entry.get())-1,END)
    test2('+')

#--------------------------------GUI----------------------------------------#

root = Tk()
root.title("Calculator")

#Main Form to type in
entry=Entry(root)
entry.grid(row=0,column=0,columnspan=5,sticky=W+E+N+S)
entry.focus()

#  InfiniNote:In this section, all the numbers are given names based
#  on their function. i.e. the 9 button is called b9
b9=Button(root,text='9', command=lambda: insNum('9'))
b9.grid(row=1,column=0)
b8=Button(root,text='8', command=lambda: insNum('8'))
b8.grid(row=1,column=1)
b7=Button(root,text='7', command=lambda: insNum('7'))
b7.grid(row=1,column=2)
b6=Button(root,text='6', command=lambda: insNum('6'))
b6.grid(row=2,column=0)
b5=Button(root,text='5', command=lambda: insNum('5'))
b5.grid(row=2,column=1)
b4=Button(root,text='4', command=lambda: insNum('4'))
b4.grid(row=2,column=2)
b3=Button(root,text='3', command=lambda: insNum('3'))
b3.grid(row=3,column=0)
b2=Button(root,text='2', command=lambda: insNum('2'))
b2.grid(row=3,column=1)
b1=Button(root,text='1', command=lambda: insNum('1'))
b1.grid(row=3,column=2)
b0=Button(root,text='0', command=lambda: insNum('0'))
b0.grid(row=4,column=0)
bdot=Button(root,text='.', command=lambda: insNum('.'))
bdot.grid(row=4,column=1)

#Clear all button
bclear=Button(root,text='AC', command=lambda: entry.delete(0,END))
bclear.grid(row=4,column=2)

#Backspace button
bb=Button(root,text='<--', command=lambda: entry.delete(len(entry.get())-1,END))
bb.grid(row=1,column=3)

#Plus button
bplus=Button(root,text='+', command=lambda: test2('+'))
root.bind('<+>',tplus)
bplus.grid(row=2,column=3,rowspan=3,sticky=W+E+N+S)

#Minus button
bmin=Button(root,text='-', command=lambda: test2('-'))
root.bind('<minus>',tmin)
bmin.grid(row=1,column=4)

#Times button
btim=Button(root,text='*', command=lambda: test2('*'))
root.bind('<*>',ttim)
btim.grid(row=2,column=4)

#Divide button
bd=Button(root,text='/', command=lambda: test2('/'))
root.bind('</>',tdiv)
bd.grid(row=3,column=4)

#Equals-to button
beq=Button(root,text='=', command=lambda: test2('='))
root.bind('<Return>',teq)
beq.grid(row=4,column=4)

buttarr=[b1, b2, b3, b4, b5, b6, b7, b8 , b9, b0, bdot, bd, bmin,
         bplus, btim, bclear, bb, beq]
for butt in buttarr:
    butt['width']=int(entry['width']/4)

root.mainloop()
