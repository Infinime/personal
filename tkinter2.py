from tkinter import *

def doNothing():
     print('ok, ok i won\'t...')

root=Tk()

# ************ Creates the main horizontal menu **************
menu=Menu(root)
root.config(menu=menu)

#File Menu... 
file = Menu(menu)
menu.add_cascade(label='File',menu=file)
file.add_command(label='New File', command=doNothing)
file.add_command(label='Open...', command=doNothing)
file.add_command(label='Open Module...', command=doNothing)
file.add_command(label='Recent Files', command=doNothing)
file.add_command(label='Module Browser', command=doNothing)
file.add_command(label='Path Browser', command=doNothing)
file.add_separator()#adds that horizontal separator
file.add_command(label='Save', command=doNothing)
file.add_command(label='Save As...', command=doNothing)
file.add_command(label='Save Copy As...', command=doNothing)
file.add_separator()
file.add_command(label='Print Window', command=doNothing)
file.add_separator()
file.add_command(label='Close', command=doNothing)
file.add_command(label='Exit', command=doNothing)

#Edit menu
edit=Menu(menu)
menu.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Undo',command=doNothing)
edit.add_command(label='Redo',command=doNothing)
edit.add_separator()
edit.add_command(label='Cut',command=doNothing)
edit.add_command(label='Copy',command=doNothing)
edit.add_command(label='Paste',command=doNothing)
edit.add_command(label='Select All',command=doNothing)
edit.add_separator()
edit.add_command(label='Find...',command=doNothing)
edit.add_command(label='Find Again',command=doNothing)
edit.add_command(label='Find Selection',command=doNothing)
edit.add_command(label='Find In Files...',command=doNothing)
edit.add_command(label='Replace...',command=doNothing)
edit.add_command(label='Go to line',command=doNothing)
edit.add_command(label='Show Completions',command=doNothing)
edit.add_command(label='Expand Word',command=doNothing)
edit.add_command(label='Show Call Tip',command=doNothing)
edit.add_command(label='Show Surrounding Parens',command=doNothing)

#Format menu
form=Menu(menu)
menu.add_cascade(label='Format', menu=form)
form.add_command(label='Indent Region', command=doNothing)
form.add_command(label='Dedent Region', command=doNothing)
form.add_command(label='Comment Out Region', command=doNothing)
form.add_command(label='Uncomment Region', command=doNothing)
form.add_command(label='Tabify Region', command=doNothing)
form.add_command(label='Untabify Region', command=doNothing)
form.add_command(label='Toggle Tabs', command=doNothing)
form.add_command(label='New Indent Width', command=doNothing)
form.add_command(label='Format Paragraph', command=doNothing)
form.add_command(label='Strip Trailing Whitespace', command=doNothing)

#Run menu
run=Menu(menu)
menu.add_cascade(label='Run', menu=run)
run.add_command(label='Python Shell', command=doNothing)
run.add_command(label='Check Module', command=doNothing)
run.add_command(label='Run Module', command=doNothing)

#Options menu
options=Menu(menu)
menu.add_cascade(label='Options', menu=options)
options.add_command(label='Configure IDLE', command=doNothing)
options.add_command(label='Code Context', command=doNothing)

#Window menu
window=Menu(menu)
menu.add_cascade(label='Window', menu=window)
window.add_command(label='Zoom Height', command=doNothing)

#Help menu
hel=Menu(menu)
menu.add_cascade(label='Help', menu=hel)
hel.add_command(label='About Infinime', command=doNothing)
hel.add_separator()
hel.add_command(label='Infinime Help', command=doNothing)
hel.add_command(label='Python Docs', command=doNothing)
hel.add_command(label='Turtle Demo', command=doNothing)

# ********************* The toolbar ************************
toolbar=Frame(root, bg='Blue')
insertButt = Button(toolbar, text='Insert Image', command=doNothing)
insertButt.pack(side=LEFT,padx=2,pady=2)
printButt=Button(toolbar, text='Print', command=doNothing)
printButt.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)

#Main body
label=Label(text='Created by Infinime',width=30)
label.pack()

# ********************* The statusbar ************************
status=Label(root,text='Preparing to do nothing...', bd=1, relief=SUNKEN, anchor=W)

status.pack(fill=X, side=BOTTOM)

root.mainloop()
