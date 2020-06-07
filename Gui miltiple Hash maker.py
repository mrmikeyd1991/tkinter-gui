#-------------------------------------------------------------------------------
# Name:        Mikeys simple hash maker
# Purpose:      what the title says
#
# Author:      owner
#
# Created:     16/04/2020
# Copyright:   (c) owner 2020
# Licence:     <Open source>
#-------------------------------------------------------------------------------

from tkinter import *
import hashlib as H
#function to get hash results
def Gethash():
    Tohash = E1.get().strip()

    if (var1.get() == 'md5'):
        Hashed = H.md5(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'sha1'):
        Hashed = H.sha1(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'sha224'):
        Hashed = H.sha224(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'sha256'):
        Hashed = H.sha256(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'sha384'):
        Hashed = H.sha384(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'sha512'):
        Hashed = H.sha512(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'blake2b'):
        Hashed = H.blake2b(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'blake2s'):
        Hashed = H.blake2s(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'sha3_224'):
        Hashed = H.sha3_224(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'sha3_256'):
        Hashed = H.sha3_256(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'sha3_384'):
        Hashed = H.sha3_384(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'sha3_512'):
        Hashed = H.sha3_512(Tohash.encode()).hexdigest()
        Hashres.set(Hashed)
    if (var1.get() == 'shake_128'):
        Hashed = H.shake_128(Tohash.encode()).hexdigest(200)
        Hashres.set(Hashed)
    if (var1.get() == 'shake_256'):
        Hashed = H.shake_256(Tohash.encode()).hexdigest(200)
        Hashres.set(Hashed)
#hash type choices
Htype = [
    'md5', 'sha1', 'sha224',
    'sha256', 'sha384',
    'sha512', 'blake2b',
    'blake2s','sha3_224',
    'sha3_256', 'sha3_384',
    'sha3_512', 'shake_128',
    'shake_256']
#root configs
root = Tk()
root.geometry("450x450")
root.configure(bg="black")
root.title("Mikeys simple hash finder")
#string var to hold our variable
var1 = StringVar();
var1.set(Htype[0])

Hashres = StringVar();
#just a label
L1 = Label(root,text="select hash type ---->")
L1.configure(bg="black", fg="white",padx=2)
L1.grid(row=0,column=0)
#Dropbox selection
Opt = OptionMenu(root, var1, *Htype)
Opt.config(width=8)
Opt.grid(row=0,column=1)
#just a label
L2= Label(root, text= "Word to hash ---->")
L2.configure(bg = 'Black', fg='White')
L2.grid(row=1,column=0)
#entry to input string you wish to hash for some reason
E1 = Entry(root)
E1.configure(bg = 'Black', fg= 'White')
E1.grid(row=1,column=1)
#button to get has results
Butt = Button(root, text="Hash this shit!",command=Gethash)
Butt.configure(bg='Black', fg='Red')
Butt.grid(row=2,column=0)
#label 3 for hash results
L3 = Label(root,text="", textvariable = Hashres)
L3.configure(bg='black',fg='green')
L3.grid(row=3,column=0)
#roots mainloop
root.mainloop()
