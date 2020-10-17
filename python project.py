#*************************************************CAB BOOKING SYSTEM***********************************************#
from tkinter import *
from tkinter import messagebox
import random
from functools import partial
obj=Tk()
obj.configure(bg="#ff8500")
#top frame
first_frame=Frame(obj)
first_frame.pack(fill=X)

def main_win():

    obj.destroy()
    mainer = Tk()
    def fare_calc():
        ran_dist = [122, 255, 134, 189, 199, 234, 654, 177, 89, 145, 567, 187, 908, 197, 254, 234, 356, 456, 299, 126]
        dist = random.choice(ran_dist)
        new_fr=Frame(mainer)
        new_fr.pack()
        destin = Label(new_fr, text="the distance calculated is "+str(dist)+"Km", bg="black", fg="white", font=('verdana', '20', "bold italic"))
        destin.pack(side=LEFT, fill=X, padx=6, pady=20)
        paisva = dist * 8
        amt = Label(new_fr, text="payable amount is "+str(paisva)+"RS", bg="green", fg="white", font=('verdana', '20', "bold italic"))
        amt.pack(side=LEFT, fill=X, padx=6, pady=20)

        otp = []
        ss = ''
        for i in range(4):
            m = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            otp.append(m)
        for q in otp:
            ss += str(q)
        messagebox.showinfo("Hey user", "your OTP IS " + ss)
        messagebox.showinfo("GUIDE","WE ARE GLAD TO HELP YOU")
        messagebox.showinfo("GUIDE", "The Cab is on its way, will reach you shortly")

    l = Label(mainer, text="START YOUR JOURNEY BRUHH", bg="yellow", font=('verdana', '30', "bold italic"))
    l.pack()
    fra1=Frame(mainer,height=24,bg="green")
    fra1.pack(side=TOP)
    start=Label(fra1, text="starting point", bg="red", font=('verdana', '20', "bold italic"))
    start.pack(side=LEFT,fill=X,padx=6,pady=20)
    e1 = Entry(fra1, font=('verdana', '25', "bold"))
    e1.pack(side=LEFT,padx=8,pady=20)
    dest = Label(fra1, text="destination point", bg="red", font=('verdana', '20', "bold italic"))
    dest.pack(side=LEFT, fill=X, padx=6, pady=20)
    e2 = Entry(fra1, font=('verdana', '25', "bold"))
    e2.pack(side=LEFT, padx=8, pady=20)
    fra2=Frame(mainer)
    sub = Button(fra2, text="SUBMIT", bg="grey", fg="black", font=('verdana', '30', "bold italic"), command=fare_calc)
    sub.pack()
    main_f=Frame(mainer,bg="black")
    main_f.pack(fill=X)
    fra3 = Frame(main_f)
    fra3.pack(side=TOP)
    checkbox = Checkbutton(fra3, text="   Bike", bg="pink", fg="red",width=25,height=2,justify=CENTER, font=('verdana', '13', "bold italic"))
    checkbox.pack(fill=Y)

    checkbox2 = Checkbutton(fra3, text="Micro", bg="pink", fg="red",width=25,height=2, justify=CENTER,font=('verdana', '13', "bold italic"))
    checkbox2.pack(fill=Y)

    checkbox3 = Checkbutton(fra3, text=" Mini", bg="pink", fg="red",width=25,height=2,justify=CENTER,font=('verdana', '13', "bold italic"))
    checkbox3.pack(fill=Y)

    checkbox4 = Checkbutton(fra3, text="  Auto", bg="pink", fg="red",width=25,height=2,justify=CENTER,font=('verdana', '13', "bold italic"))
    checkbox4.pack(fill=Y)

    checkbox5 = Checkbutton(fra3, text="     Sedan", bg="pink", fg="red",width=25,height=2,justify=CENTER, font=('verdana', '13', "bold italic"))
    checkbox5.pack(fill=Y)

    checkbox6 = Checkbutton(fra3, text=" Prime EXec", bg="pink", fg="red",width=25,height=2,justify=CENTER,font=('verdana', '13', "bold italic"))
    checkbox6.pack(fill=Y)
    fra2.pack()

    checkbox7 = Checkbutton(fra3, text=" E-Rickshaw", bg="pink", fg="red",width=25,height=2,justify=CENTER,font=('verdana', '13', "bold italic"))
    checkbox7.pack(fill=Y)
    mainer.mainloop()

def login():
    master=Tk()
    master.configure(bg="lightgreen")
    log=Label(master,text="LOGIN",bg="orange",fg="white",font=('verdana', '55', "bold"))
    log.pack(fill=X)

    def closer():
        messagebox.showinfo("GUIDE", "thank you for login")
        master.destroy()
        main_win()

    fr_1=Frame(master,bg="grey")
    fr_1.pack(pady=8)

    fr_2 = Frame(master, bg="grey")
    fr_2.pack(pady=8)

    fr_3 = Frame(master, bg="grey")
    fr_3.pack(pady=8)

    first=Label(fr_1, text="Mobile no.",bg="red",font=('verdana', '30', "bold italic"))
    first.pack(side=LEFT,padx=12)
    e1 = Entry(fr_1,font=('verdana', '25', "bold"))
    e1.pack(side=LEFT)

    second=Label(fr_2, text="Password ",bg="blue",font=('verdana', '30', "bold italic"))
    second.pack(side=LEFT,padx=11)
    e2 = Entry(fr_2,font=('verdana', '25', "bold"))
    e2.pack(side=LEFT)

    sub=Button(fr_3,text="SUBMIT",bg="grey",fg="black",font=('verdana', '30', "bold italic"),command=closer)
    sub.pack()

    master.mainloop()


def register():
    master = Tk()
    log = Label(master, text="REGISTER", bg="blue", fg="white", font=('verdana', '55', "bold"))
    log.pack(fill=X)
    def otpgen(mob):
        fr_4 = Frame(master)
        fr_4.pack(pady=8)
        otplab = Label(fr_4, text="Enter your OTP", font=('verdana', '30', "bold italic"))
        otplab.pack(side=LEFT)
        eotp = Entry(fr_4, font=('verdana', '25', "bold"))
        eotp.pack(side=LEFT)
        otp = []
        ss = ''
        for i in range(4):
            m = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            otp.append(m)
        for q in otp:
            ss += str(q)
        messagebox.showinfo("Hey user", "your OTP IS " + ss)
        def check():
            if (ss == str(eotp.get())):
                messagebox.showinfo("GUIDE", "Registered Successfully")
                master.destroy()
                messagebox.showinfo("GUIDE", "thank you for login")
                main_win()
            else:
                messagebox.showinfo("guide","not correct keep on doing that")
        sub=Button(fr_4,text="SUBMIT",bg="yellow",fg="black",font=('verdana', '25', "bold"),command=check)
        sub.pack()

    fr_1=Frame(master,bg="grey")
    fr_1.pack(pady=8)

    fr_2 = Frame(master, bg="grey")
    fr_2.pack(pady=8)

    fr_3 = Frame(master, bg="grey")
    fr_3.pack(pady=8)

    fr_4 = Frame(master, bg="grey")
    fr_4.pack(pady=8)

    fr_5 = Frame(master, bg="grey")
    fr_5.pack(pady=8)

    fr_6 = Frame(master, bg="grey")
    fr_6.pack(pady=8)

    fr_8 = Frame(master, bg="grey")
    fr_8.pack(pady=8)

    first = Label(fr_1, text="FIRST NAME", bg="red", font=('verdana', '30', "bold italic"))
    first.pack(side=LEFT, padx=12)
    e1 = Entry(fr_1, font=('verdana', '25', "bold"))
    e1.pack(side=LEFT)

    second = Label(fr_2, text="LAST NAME ", bg="blue", font=('verdana', '30', "bold italic"))
    second.pack(side=LEFT, padx=11)
    e2 = Entry(fr_2, font=('verdana', '25', "bold"))
    e2.pack(side=LEFT)

    third = Label(fr_3, text="EMAIL ID", bg="blue", font=('verdana', '30', "bold italic"))
    third.pack(side=LEFT, padx=11)
    e3 = Entry(fr_3, font=('verdana', '25', "bold"))
    e3.pack(side=LEFT)

    fourth = Label(fr_4, text="MOBILE NUMBER ", bg="blue", font=('verdana', '30', "bold italic"))
    fourth.pack(side=LEFT, padx=11)
    e4 = Entry(fr_4, font=('verdana', '25', "bold"))
    e4.pack(side=LEFT)

    fifth = Label(fr_5, text="PASSWORD ", bg="blue", font=('verdana', '30', "bold italic"))
    fifth.pack(side=LEFT, padx=11)
    e4 = Entry(fr_5, font=('verdana', '25', "bold"))
    e4.pack(side=LEFT)

    sixth = Label(fr_6, text="CONFIRM PASSWORD ", bg="blue", font=('verdana', '30', "bold italic"))
    sixth.pack(side=LEFT, padx=11)
    e4 = Entry(fr_6, font=('verdana', '25', "bold"))
    e4.pack(side=LEFT)

    gen = Button(fr_8, text="Generate OTP", bg="grey", fg="black", font=('verdana', '30', "bold italic"),command=partial(otpgen,fourth["text"]))
    gen.pack()
    master.mainloop()

def change():
    curr = box.cget("background")
    coco = box.cget("fg")
    nextco = "#ffaa00" if curr == "black" else "black"
    nex = "black" if coco == "#ffa500" else "#ffa500"
    box.config(background=nextco, fg=nex)
    obj.after(800, change)
box = Label(first_frame, text="CAB BOOKING SYSTEM", background="#ffa500", fg="black",bd=4, relief=RIDGE,font=('verdana', '55', "italic bold"), justify=LEFT)
box.pack(side=TOP, fill=X)
change()
#middle frame
mid_frame=Frame(obj,bg="#ffa500")
mid_frame.pack(fill=X)
intro=Label(mid_frame,text="Welcome to cab booking system,I hope you have a enriching experience",bg="#ffa500",font=('Times', '25', "bold"))
intro.pack()
#bottom frame
button=Button(text="Login",bg="#ff0000",width=12,height=2,font=("verdana",30,"bold italic"),command=login)
button.pack(side=LEFT,padx=184)

button1=Button(text="Register",bg="#ff0000",width=12,height=2,font=("verdana",30,"bold italic"),command=register)
button1.pack(side=RIGHT,padx=184)

obj.mainloop()
