# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 10:13:13 2019

@author: Ravi Shankar
"""


import tkinter.messagebox
from tkinter import*
from PIL import Image,ImageTk


root = Tk()
root.title('Lovely Professional University')
root.geometry('1920x1080')
root.wm_iconbitmap('images.png')


l = Label(root, bg = 'orange',text = 'Lovely Professional University',fg = 'white',height = 2,width =1980, font = ('arial',30,'italic'))
l.pack()

img = Image.open('C:/Users/Ravi Shankar/Music/py/download.jpeg')
pho = ImageTk.PhotoImage(img)
lb = Label(image = pho)
lb.place(x = 280,y=7)


f = Frame(root,bg = 'red',height =50,width =1980)
f.pack()

b = Button(root,bg = 'red',fg = 'white',text = 'Home')
b.place(x=120,y=110)

#LPUNEST application
def lpunest():
    root2 = Tk()
    root2.geometry('500x500')
    label9 = Label(root2,bg = 'brown',fg= 'white',text = 'Application of LPUNEST',relief = 'solid',width = 20,font = ('arial',19,'bold'))
    label9.place(x = 90,y=53)
    
    label10 =  Label(root2,text = 'Full Name : ',width = 20,font = ('arial',10,'bold'))
    label10.place(x=80,y=130)
    
    fn1 = StringVar()
    en1 = Entry(root2,textvar = fn1)
    en1.place(x=300,y=130)

    label11 =  Label(root2,text = 'Father Name : ',width = 20,font = ('arial',10,'bold'))
    label11.place(x=80,y=160)
    
    ln1 = StringVar()
    en2 = Entry(root2,textvar = ln1)
    en2.place(x=300,y=160)
    
    label12 = Label(root2,text = 'Country : ',width = 20,font = ('arial',10,'bold'))
    label12.place(x=80,y=190)
    
    var = StringVar()
    list1 = ['India','Kuwait','China']
    drop = OptionMenu(root2,var,*list1)
    var.set('Select country')
    drop.config(width=15)
    drop.place(x=300,y=190)

    label14 = Label(root2,text = 'Gender : ',width = 20,font = ('arial',10,'bold'))
    label14.place(x=80,y=220)
    
    rdd = StringVar()
    rd1 = Radiobutton(root2,text = 'Female',variable = rdd,value='Female').place(x = 300,y=220)
    rd2 = Radiobutton(root2,text = 'Male',variable = rdd,value = 'Male').place(x =380,y=220)
    
    
    label15 = Label(root2,text = 'Group : ',width = 20,font = ('arial',10,'bold'))
    label15.place(x=80,y=250)
    
    rdd = StringVar()
    rd3 = Radiobutton(root2,text = 'M.P.C',variable = rdd,value='M.P.C').place(x = 300,y=250)
    rd4 = Radiobutton(root2,text = 'Bi.P.C',variable = rdd,value = 'Bi.P.C').place(x =380,y=250)
    
    label16 = Label(root2,text = 'City : ',width = 20,font = ('arial',10,'bold'))
    label16.place(x=80,y=280)
    
    fn2 = StringVar()
    en2 = Entry(root2,textvar = fn2)
    en2.place(x=300,y=280)
    
    label17 = Label(root2,text = 'State : ',width = 20,font = ('arial',10,'bold'))
    label17.place(x=80,y=310)
    
    fn3 = StringVar()
    en3 = Entry(root2,textvar = fn3)
    en3.place(x=300,y=310)
    
    label18 = Label(root2,text = 'Street : ',width = 20,font = ('arial',10,'bold'))
    label18.place(x=80,y=340)
    
    fn4 = StringVar()
    en4 = Entry(root2,textvar = fn4)
    en4.place(x=300,y=340)
    #for payment
    def pay():
        root3 = Tk()
        root3.geometry('500x500')
        label19 = Label(root3,bg = 'brown',fg= 'white',text = 'Payment Methods',relief = 'solid',width = 20,font = ('arial',19,'bold'))
        label19.place(x = 90,y=53)
        
        label20 = Label(root3,text = 'Cards : ',width = 20,font = ('arial',10,'bold'))
        label20.place(x=80,y=130)
    
        rdd = StringVar()
        rd3 = Radiobutton(root3,text = 'Credit',variable = rdd,value='Credit').place(x = 300,y=130)
        rd4 = Radiobutton(root3,text = 'Debit',variable = rdd,value = 'Debit').place(x =380,y=130)
        
        label21 = Label(root3,text = 'Card Number : ',width = 20,font = ('arial',10,'bold'))
        label21.place(x=80,y=160)
    
        fn2 = StringVar()
        en2 = Entry(root3,textvar = fn2)
        en2.place(x=300,y=160)
        
        label22 = Label(root3,text = 'Month/Year : ',width = 20,font = ('arial',10,'bold'))
        label22.place(x=80,y=190)
        
        fn2 = StringVar()
        en2 = Entry(root3,textvar = fn2)
        en2.place(x=300,y=190)
        
        label22 = Label(root3,text = 'CVV : ',width = 20,font = ('arial',10,'bold'))
        label22.place(x=80,y=220)
        
        fn2 = StringVar()
        en2 = Entry(root3,textvar = fn2)
        en2.place(x=300,y=220)
        
        label22 = Label(root3,text = 'Card Holder Name : ',width = 20,font = ('arial',10,'bold'))
        label22.place(x=80,y=250)
        
        fn2 = StringVar()
        en2 = Entry(root3,textvar = fn2)
        en2.place(x=300,y=250)
        
        #after registered
        def succ():
            tkinter.messagebox.showinfo('Welcome',"User is successfully Registered")
            exit()
            
        b3 = Button(root3,text='Confirm',width = 12,bg = 'brown',fg = 'white',command = succ)
        b3.place(x=200,y = 380)
        
        root3.mainloop()
        
    b1 = Button(root2,text='Register',width = 12,bg = 'brown',fg = 'white',command = pay)
    b1.place(x=150,y = 380)

    b2 = Button(root2,text='Cancel',width = 12,bg = 'brown',fg = 'white')
    b2.place(x=280,y = 380)
    

    root2.mainloop()
    

#Gallery
def galler():
    rot = Tk()
    rot.geometry('1980x1080')
    c2 = Canvas(rot,bg = 'white',height = 1000,width =1000)
    file2=PhotoImage(file="downloadd.png")
    c2.create_image(110,10, anchor=NE, image=file2)
    c2.pack()
    rot.mainloop()
    
 #Registration Form       
def regist():
    root1 = Tk()
    root1.geometry('500x500')
    label = Label(root1,bg = 'orange',fg= 'white',text = 'Application form',relief = 'solid',width = 20,font = ('arial',19,'bold'))
    label.place(x = 90,y=53)
    
    label2 =  Label(root1,text = 'First Name : ',width = 20,font = ('arial',10,'bold'))
    label2.place(x=80,y=130)
    
    fn1 = StringVar()
    en1 = Entry(root1,textvar = fn1)
    en1.place(x=300,y=130)

    label3 =  Label(root1,text = 'Last Name : ',width = 20,font = ('arial',10,'bold'))
    label3.place(x=80,y=160)
    
    ln1 = StringVar()
    en2 = Entry(root1,textvar = ln1)
    en2.place(x=300,y=160)
    
    label4 = Label(root1,text = 'Country : ',width = 20,font = ('arial',10,'bold'))
    label4.place(x=80,y=190)
    
    var = StringVar()
    list1 = ['India','Kuwait','China']
    drop = OptionMenu(root1,var,*list1)
    var.set('Select country')
    drop.config(width=15)
    drop.place(x=300,y=190)
    
    label5 = Label(root1,text = 'Application Based on : ',width = 20,font = ('arial',10,'bold'))
    label5.place(x=80,y=220)
    
    chec = StringVar()
    ch = Checkbutton(root1,text='LPUNEST',font = ('bold',10),variable= chec)
    ch.place(x = 300,y=220)

    check1 = StringVar()
    ch = Checkbutton(root1,text='IP Marks',variable = check1,font = ('bold',10))
    ch.place(x = 400,y=220)

    label6 = Label(root1,text = 'Gender : ',width = 20,font = ('arial',10,'bold'))
    label6.place(x=80,y=250)
    
    rdd = StringVar()
    rd1 = Radiobutton(root1,text = 'Female',variable = rdd,value='Female').place(x = 300,y=250)
    rd2 = Radiobutton(root1,text = 'Male',variable = rdd,value = 'Male').place(x =380,y=250)
    
    label7 = Label(root1,text = 'Marks (in LPUNEST) : ',width = 20,font = ('arial',10,'bold'))
    label7.place(x=80,y=280)
    
    ln2 = StringVar()
    en3 = Entry(root1,textvar = ln2)
    en3.place(x=300,y=280)
    
    label8 = Label(root1,text = 'Marks (in IP) : ',width = 20,font = ('arial',10,'bold'))
    label8.place(x=80,y=310)
    
    ln3 = StringVar()
    en4 = Entry(root1,textvar = ln3)
    en4.place(x=300,y=310)
    
    def printtt():
        tkinter.messagebox.showinfo('Welcome',"User is successfully Registered")
        exit()
        
    b1 = Button(root1,text='Register',width = 12,bg = 'brown',fg = 'white',command = printtt)
    b1.place(x=150,y = 380)

    b2 = Button(root1,text='Cancel',width = 12,bg = 'brown',fg = 'white')
    b2.place(x=280,y = 380)
    

    root1.mainloop()
    
def about():
    root4 = Tk()
    root4.geometry('1920x1080')
    f2 = Label(root4,bg = 'brown',text = 'About LPU',fg = 'White',height =2,width = 1000,font = ('arial',20,'bold'))
    f2.pack()
    cann = Canvas(root4,bg = 'white',width =1000,height =600)
    
    cann.pack()
    root4.mainloop()


b1 = Button(root,bg = 'red',fg = 'white',text = 'Gallery',command = galler)
b1.place(x=320,y=110)

b2 = Button(root,bg = 'red',fg = 'white',text = 'LPUNEST',command = lpunest)
b2.place(x=520,y=110)

b3 = Button(root,bg = 'red',fg = 'white',text = 'Application Form',command = regist)
b3.place(x=720,y=110)

b4 = Button(root,bg = 'red',fg = 'white',text = 'About',command = about)
b4.place(x=920,y=110)

c=Canvas(root,bg='white', height=700,width=1980)

file1=PhotoImage(file="downloadd.png")
c.create_image(1100,10, anchor=NE, image=file1)

c.pack()

root.mainloop()
