from tkinter import *

root = Tk()
root.title('Simple Calculator')

scrl = Scrollbar(root, orient = HORIZONTAL)

e = Entry(root, bd = 3, justify= RIGHT, xscrollcommand= scrl.set)
e.place(relx=0 , relwidth = 1, relheight = 0.1)
def B(number):
    e.insert(END,number)

def add():
    e.insert(END, ' + ')
    
#vari = 0
def equal():
    vari=0
    y = e.get()
    x = y.split(' + ')
    for i in range(len(x)):
        vari = vari+ int(x[i])
    e.delete(0, END)
    e.insert(0, vari)
    
def clear():
    e.delete(0,END)
    
button7 = Button(root, text=7, command= lambda : B(7))
button7.place(relx = 0.025 , rely = 0.1 ,relwidth=0.3 , relheight = 0.18 )

button8 = Button(root, text=8, command= lambda : B(8))
button8.place(relx = 0.35, rely=0.1, relwidth=0.3,relheight = 0.18 )

button9 = Button(root, text=9,command= lambda : B(9) )
button9.place(relx = 0.675, rely=0.1, relwidth=0.3, relheight = 0.18 )

button4 = Button(root, text=4,command= lambda : B(4) )
button4.place(relx = 0.025, rely=0.28, relwidth=0.3, relheight = 0.18 )

button5 = Button(root, text=5,command= lambda : B(5))
button5.place(relx = 0.35, rely=0.28, relwidth=0.3, relheight = 0.18 )

button6 = Button(root, text=6,command= lambda : B(6) )
button6.place(relx = 0.675, rely=0.28, relwidth=0.3, relheight = 0.18 )

button1 = Button(root, text=1, command= lambda : B(1))
button1.place(relx = 0.025, rely=0.46, relwidth=0.3, relheight = 0.18 )

button2 = Button(root, text=2,command= lambda : B(2) )
button2.place(relx = 0.35, rely=0.46, relwidth=0.3, relheight = 0.18 )

button3 = Button(root, text=3,command=lambda : B(3)  )
button3.place(relx = 0.675, rely=0.46, relwidth=0.3, relheight = 0.18 )

button0 = Button(root, text=0,command= lambda : B(0))
button0.place(relx = 0.025, rely=0.64, relwidth=0.3, relheight = 0.18 )

button11 = Button(root, text='+', command = add)
button11.place(relx = 0.025, rely=0.82, relwidth=0.3, relheight = 0.18 )

button12 = Button(root, text='=', command= equal)
button12.place(relx = 0.35, rely=0.82, relwidth=0.625, relheight = 0.18 )

button10 = Button(root, text='clear', command= clear)
button10.place(relx =0.35, rely=0.64, relwidth=0.625, relheight = 0.18 )


root.mainloop()
