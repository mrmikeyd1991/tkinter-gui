from tkinter import *
#function to get grade
def Getgrade():
    Aresul= float(Sas.get()) + float(Sacf.get())
    Bresul = float(Sbs.get())+float(Sbcf.get())
    Midnum = (float(Aresul)+float(Bresul))/2
    Grade = (float(Mh.get()) - Midnum)/float(Dis.get())*100
    Text.set(Grade)
#window
root = Tk()
#string var to hold 
Text = StringVar()
#labels
Label(root, text="Manhole shot").grid(row=0,column=0)
Label(root, text="15 offset shot").grid(row=1,column=0)
Label(root, text="15 ft Cut/Fill").grid(row=2,column=0)
Label(root, text="25 ft offset").grid(row=3,column=0)
Label(root, text="25 ft Cut/Fill").grid(row=4,column=0)
Label(root, text="Distance").grid(row=5,column=0)
#Manhole shot
Mh = Entry(root)
Mh.grid(row=0,column=1)
#15ft
Sas = Entry(root)
Sas.grid(row=1, column=1)
#15ft cf
Sacf = Entry(root)
Sacf.grid(row=2, column=1)
#25ft
Sbs = Entry(root)
Sbs.grid(row=3, column=1)
Sbcf = Entry(root)
Sbcf.grid(row=4, column=1)
#Dist
Dis = Entry(root)
Dis.grid(row=5, column=1)
#button then label
Cal = Button(root, text="Get Grade!", command=Getgrade).grid(row=6,column=0)
Res = Label(root, text="", textvariable=Text).grid(row=6,column=1)
#root mainloop
root.mainloop()