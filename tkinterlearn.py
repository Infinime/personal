from tkinter import *

num1=0
num2=0
worker=''

def test1(number):
    entry.insert(len(entry.get()),number)

def test2(fun):
    global num1
    global num2
    global worker
    if fun=='=':
        num2=int(entry.get())
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
        num1=int(entry.get())
        entry.delete(0,END)

root = Tk()

entry=Entry(root)
entry.grid(row=0,column=0,columnspan=5,sticky=W+E+N+S)

b9=Button(root,text='9', command=lambda: test1('9'))
b9.grid(row=1,column=0)

b8=Button(root,text='8', command=lambda: test1('8'))
b8.grid(row=1,column=1)

b7=Button(root,text='7', command=lambda: test1('7'))
b7.bind(test1)
b7.grid(row=1,column=2)

bb=Button(root,text='<--', command=lambda: entry.delete(len(entry.get())-1,END))
bb.bind(test1)
bb.grid(row=1,column=3)

bplus=Button(root,text='+', command=lambda: test2('+'))
bplus.bind(test1)
bplus.grid(row=2,column=3,rowspan=3,sticky=W+E+N+S)

b6=Button(root,text='6', command=lambda: test1('6'))
b6.bind(test1)
b6.grid(row=2,column=0)

b5=Button(root,text='5', command=lambda: test1('5'))
b5.bind(test1)
b5.grid(row=2,column=1)

b4=Button(root,text='4', command=lambda: test1('4'))
b4.bind(test1)
b4.grid(row=2,column=2)

bmin=Button(root,text='-', command=lambda: test2('-'))
bmin.bind(test1)
bmin.grid(row=1,column=4)

b3=Button(root,text='3', command=lambda: test1('3'))
b3.bind(test1)
b3.grid(row=3,column=0)

b2=Button(root,text='2', command=lambda: test1('2'))
b2.bind(test1)
b2.grid(row=3,column=1)

b1=Button(root,text='1', command=lambda: test1('1'))
b1.bind(test1)
b1.grid(row=3,column=2)

btim=Button(root,text='*', command=lambda: test2('*'))
btim.bind(test1)
btim.grid(row=2,column=4)

b0=Button(root,text='0', command=lambda: test1('0'))
b0.bind(test1)
b0.grid(row=4,column=0)

bdot=Button(root,text='.', command=lambda: test1('.'))
bdot.bind(test1)
bdot.grid(row=4,column=1)

bclear=Button(root,text='AC', command=lambda: entry.delete(0,END))
bclear.bind(test1)
bclear.grid(row=4,column=2)

bd=Button(root,text='/', command=lambda: test2('/'))
bd.bind(test1)
bd.grid(row=3,column=4)

beq=Button(root,text='=', command=lambda: test2('='))
beq.grid(row=4,column=4)

buttarr=[b1, b2, b3, b4, b5, b6, b7, b8 , b9, b0, bdot, bd, bmin, bplus, btim, bclear,bb,beq]
for butt in buttarr:
    butt['width']=int(entry['width']/4)

root.mainloop()
