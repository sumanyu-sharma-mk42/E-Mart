# importing modules

import tkinter,center_tk_window,smtplib,webbrowser,os
from tkinter import ttk
import datetime
import time
from tkinter import *
from tkinter import ttk
import mysql.connector as m
import PIL
from PIL import Image
import re

# connection database

mydb = m.connect(
  host="localhost",
  user="root",
  password="1234"
)

mycursor = mydb.cursor()
try:
        mycursor.execute("CREATE DATABASE app")
except:
        pass

con = m.connect(user = 'root',host = 'localhost',passwd = '1234',database = 'app')
cursor = con.cursor()

# communication with email services

s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('email id that you created for alerts','16 digit app password')
x=0
regex = "^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
um =am=em = ''

# to open menu window

def menu():
        global Mainmenu
        global st
        global mt
        global nt
        global gamesi
        global gamesis
        global entertainmenti
        global entertainmentis
        global shoppingi
        global shoppingis
        global settingi
        global settingis
        global mmroot
        mmroot=Tk()
        mmroot.iconify()
        Mainmenu = Toplevel()
        Mainmenu.geometry('1920x1080')
        Mainmenu.configure(bg='black')
        gamesi = PhotoImage(file= 'Picture1.png')
        gamesis = gamesi.subsample(3,3)
        gamesl=Label(Mainmenu,text='Games',bg='Black',fg='White')
        gamesl.pack(pady=5)
        gamesl.config(font=("Courier",15))
        games = Button(Mainmenu,command=gamesmain,image = gamesis,bg='black')
        games.pack(pady=5)
        entertainmenti = PhotoImage(file = 'Picture2.png')
        entertainmentis = entertainmenti.subsample(3,3)
        entertainmentl = Label(Mainmenu,text='Entertainment',bg='Black',fg='White')
        entertainmentl.config(font=("Courier",15))
        entertainmentl.pack(pady=5)
        Entertainment = Button(Mainmenu,command=Entertainmentmain,image = entertainmentis,bg='black')
        Entertainment.pack(pady=5)
        shoppingi = PhotoImage(file = 'Picture3.png')
        shoppingis = shoppingi.subsample(3,3)
        shoppingl = Label(Mainmenu,text='Shopping',bg='Black',fg='White')
        shoppingl.config(font=("Courier",15))
        shoppingl.pack(pady=5)
        Shopping=Button(Mainmenu,command=shoppingfunc,image = shoppingis,bg='black')
        Shopping.pack(pady=5)
        settingi = PhotoImage(file = 'Picture4.png')
        settingis = settingi.subsample(3,3)
        settingl = Label(Mainmenu,text='Settings',bg='Black',fg='White')
        settingl.config(font=("Courier",15))
        settingl.pack(pady=5)
        Settings=Button(Mainmenu,text='Settings',command = settingfunc,image = settingis)
        Settings.pack(pady=5)
        cursor.execute("select NEWS,MUSIC,SHOPPING from users where USERNAME = '{}';".format(username_all))
        fata = cursor.fetchall()
        nt = fata[0][0]
        mt = fata[0][1]
        st = fata[0][2]
        
        
# to toggle backward

def backbuttonfunc(t,h):
    t.destroy()
    h()
    
# for logging in to the app

def Mainmenu():
        cursor.execute('select USERNAME,PASSWORD from users')
        data = cursor.fetchall()
        if unameentry.get()=='' or pentry.get()=='':
                i_credentials=Label(rframe,text='Please fill the details',bg='black',fg='white')
                i_credentials.config(font=("Courier",15))
                i_credentials.pack()
                             
        else:
                for i in data:
                    if unameentry.get()== i[0] and i[1] == pentry.get():
                        cursor.execute("select USERNAME,EMAIL,NAME from users where USERNAME = '{}' ;".format(unameentry.get()))
                        data = cursor.fetchall()
                        global username_all
                        global email_all
                        global jii
                        global kii
                        global tii
                        global oii
                        global pii
                        global namee
                        namee = data[0][2]
                        username_all = data[0][0]
                        email_all = data[0][1]
                        cursor.execute("select SCI_TECH from users where USERNAME = '{}'; ".format(username_all))
                        sata = cursor.fetchall()
                        jii = sata[0][0]
                        cursor.execute("select SCI_FI from users where USERNAME = '{}'; ".format(username_all))
                        kata = cursor.fetchall()
                        kii = kata[0][0]
                        cursor.execute("select ROMANTIC from users where USERNAME = '{}'; ".format(username_all))
                        pata = cursor.fetchall()
                        pii = pata[0][0]
                        cursor.execute("select FANTASY from users where USERNAME = '{}'; ".format(username_all))
                        tata = cursor.fetchall()
                        tii = tata[0][0]
                        cursor.execute("select SUSPENSE from users where USERNAME = '{}'; ".format(username_all))
                        oata = cursor.fetchall()
                        oii = oata[0][0]
                        try:
                                
                                r.destroy()
                        except:
                                pass
                        menu()
                        v= Label(Mainmenu,text='Welcome Back '+namee,bg='black',fg='white')
                        v.config(font=("Monteserrat",20))
                        v.pack()
                        cursor.execute("select LAST_LOGIN from users where USERNAME = '{}' ;".format(username_all))
                        welcomata = cursor.fetchall()
                        hiata  =welcomata[0][0]
                        welcome = Label(Mainmenu,text = "Haven't seen you since: "+hiata,bg='black',fg='white')
                        welcome.config(font=("Monteserrat",10))
                        welcome.pack()
                        date_time = str(datetime.datetime.now())
                        tiata = date_time[0:19]
                        
                        cursor.execute("update users set LAST_LOGIN = '{}' where USERNAME = '{}';".format(tiata,username_all))
                        con.commit()
                        break
                else:
                        i_credentials=Label(rframe,text='Incorrect Credentials, try again',bg='black',fg='white')
                        i_credentials.config(font=("Courier",15))
                        i_credentials.pack()
                        
# to send password recovery mail

def fpasswordok():
        try:
            z = "select PASSWORD from users where EMAIL = '{}';".format(mailentry.get())
            cursor.execute(z)
            data = cursor.fetchall()
            f = data[0][0]
            s.sendmail('aalascare@gmail.com',mailentry.get(),f)
            try:
                    fpasswordmain.destroy()
            except:
                                pass
            mailsentlabel=Label(rframe,text='Password has been sent to registered Email ID!',bg='black',fg='white')
            mailsentlabel.config(font=("Courier",10))
            mailsentlabel.pack(pady=10)
        except:
                imail = Label(fpasswordmain,text='Incorrect Email',bg='black',fg='white')
                imail.config(font=("Courier",15))
                imail.pack()

# input window for password recovery

def fpassword():
    global fpasswordmain
    global mailentry
    fpasswordmain=Tk()
    fpasswordmain.geometry('480x270')
    fpasswordmain.configure(bg='black')
    center_tk_window.center(r,fpasswordmain)
    mailenterlabel=Label(fpasswordmain,text='Enter Registered Email ID',bg='black',fg='white')
    mailenterlabel.config(font=("Courier",22))
    mailenterlabel.pack(pady=20)
    mailentry=Entry(fpasswordmain,width=25)
    mailentry.config(font=("Courier",15))
    mailentry.pack(pady=15)
    mailsentbutton=Button(fpasswordmain,text='Ok',command=fpasswordok)
    mailsentbutton.config(font=("Courier",15))
    mailsentbutton.pack(pady=15)

# for collecting preference data from database

def pref():
        
        global am
        global um
        global em
        global newsdict
        global musicdict
        global shoppingdict
        newsdict = {'www.bbc.com':bbcvar.get(),'https://timesofindia.indiatimes.com/home/headlines':toivar.get(),'https://www.hindustantimes.com/topic/headline':htvar.get(),'https://www.thequint.com/':quintvar.get(),'https://www.jagran.com/':jagranvar.get(),'https://www.aajtak.in/':aajtakvar.get(),'https://www.ndtv.com/latest':ndtvvar.get(),'https://inshorts.com/en/read/':inshortsvar.get(),'https://www.bhaskar.com/':dainikbhaskarvar.get(),'hi':nbtvar.get()}
        musicdict = {'https://gaana.com/album/hindi':hinvar.get(),'https://gaana.com/album/english':engvar.get(),'https://gaana.com/album/punjabi':punvar.get(),'https://gaana.com/album/telugu':teluguvar.get(),'https://gaana.com/album/tamil':tamilvar.get(),'https://gaana.com/album/bhojpuri':bhojpurivar.get()}
        shoppingdict = {'AMAZON':amavar.get(),'FLIPKART':flipvar.get(),'SNAPDEAL':snapvar.get(),'SHOPCLUES':cluesvar.get(),'MYNTRA':myntravar.get()}
        for i in newsdict:
                um = um + str(newsdict[i])
        for j in musicdict:
                am = am + str(musicdict[j])
        for g in shoppingdict:
                em = em + str(shoppingdict[g])
        cursor.execute("update users set NEWS = '{}';".format(um))
        con.commit()
        cursor.execute("update users set MUSIC = '{}';".format(am))
        con.commit()
        cursor.execute("update users set SHOPPING = '{}';".format(em))
        con.commit()
        
        
        menu()
        v= Label(Mainmenu,text='Welcome To a Wonderfull Experience! '+namee,bg='black',fg='white')
        v.config(font=("Monteserrat",20))
        v.pack()
        date_time = str(datetime.datetime.now())
        tiata = date_time[0:19]
        
        cursor.execute("update users set LAST_LOGIN = '{}' where USERNAME = '{}';".format(tiata,username_all))
        con.commit()

# user's preference input for personalised app experience

def preferences():
    global preferncesmain
    global bbcvar
    global toivar
    global htvar
    global quintvar
    global jagranvar
    global aajtakvar
    global ndtvvar
    global inshortsvar
    global dainikbhaskarvar
    global nbtvar
    global engvar
    global hinvar
    global punvar
    global tamilvar
    global teluguvar 
    global bhojpurivar
    global flipvar
    global amavar
    global snapvar
    global cluesvar
    global myntravar
    preferencemain=Toplevel(signupmain)
    preferencemain.geometry('1920x1080')
    preferencemain.configure(bg='black')
    preferenceslabel=Label(preferencemain,text='Preferences',bg='black',fg='white')
    preferenceslabel.config(font=("Courier", 44))
    preferenceslabel.pack()
    
    newsplabel=Label(preferencemain,text='News Preference',bg='black',fg='white')
    newsplabel.config(font=('',30))
    newsplabel.place(x = 20, y = 85, anchor = NW)
    bbcvar = IntVar()
    toivar = IntVar()   
    htvar = IntVar()
    quintvar = IntVar()
    jagranvar = IntVar()
    aajtakvar = IntVar()
    ndtvvar = IntVar()
    inshortsvar = IntVar()
    dainikbhaskarvar = IntVar()
    nbtvar = IntVar()
    bbcc = Checkbutton(preferencemain, text = "BBC",variable = bbcvar,onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    bbcc.config(font=('',15))
    bbcc.place(x = 30, y = 140, anchor = NW)
    toic = Checkbutton(preferencemain, text = "Times Of India", variable = toivar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    toic.place(x = 30, y = 195, anchor = NW)
    toic.config(font=('',15))
    htc = Checkbutton(preferencemain, text = "Hindustan Times", variable = htvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    htc.place(x = 30, y = 250, anchor = NW)
    htc.config(font=('',15))
    quintc = Checkbutton(preferencemain, text = "The Quint", variable = quintvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    quintc.place(x = 30, y = 305, anchor = NW)
    quintc.config(font=('',15))
    jagranc = Checkbutton(preferencemain, text = "Dainik Jagran", variable = jagranvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    jagranc.place(x = 30, y = 360, anchor = NW)
    jagranc.config(font=('',15))
    aajtakc = Checkbutton(preferencemain, text = "Aaj Tak", variable = aajtakvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    aajtakc.place(x = 30, y = 415, anchor = NW)
    aajtakc.config(font=('',15))
    ndtvc = Checkbutton(preferencemain, text = "NDTV", variable = ndtvvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    ndtvc.place(x = 30, y = 470, anchor = NW)
    ndtvc.config(font=('',15))
    inshortsc = Checkbutton(preferencemain, text = "Inshorts", variable = inshortsvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    inshortsc.place(x = 30, y = 525, anchor = NW)
    inshortsc.config(font=('',15))
    dainikbhaskarc = Checkbutton(preferencemain, text = "Dainik Bhaskar", variable = dainikbhaskarvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    dainikbhaskarc.place(x = 30, y = 580, anchor = NW)
    dainikbhaskarc.config(font=('',15))
    nbtc = Checkbutton(preferencemain, text = "Navbharat Times", variable = nbtvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    nbtc.place(x = 30, y = 635 , anchor = NW)
    nbtc.config(font=('',15))

    musicplabel=Label(preferencemain,text='Music Preference',bg='black',fg='white')
    musicplabel.config(font=('',30))
    musicplabel.pack(pady=15)
    engvar = IntVar()   
    hinvar = IntVar()   
    punvar = IntVar()
    tamilvar = IntVar()
    teluguvar = IntVar()
    bhojpurivar = IntVar()
    engc = Checkbutton(preferencemain, text = "English",variable = engvar,onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    engc.place(x = 665, y = 140)
    engc.config(font=('',15))
    hinc = Checkbutton(preferencemain, text = "Hindi", variable = hinvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    hinc.place(x = 665, y = 195)
    hinc.config(font=('',15))
    punc = Checkbutton(preferencemain, text = "Punjabi", variable = punvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    punc.place(x = 665, y = 250)
    punc.config(font=('',15))
    tamilc = Checkbutton(preferencemain, text = "Tamil", variable = tamilvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    tamilc.place(x = 665, y = 305)
    tamilc.config(font=('',15))
    teluguc = Checkbutton(preferencemain, text = "Telugu", variable = teluguvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    teluguc.place(x = 665, y = 360)
    teluguc.config(font=('',15))
    bhojpuric = Checkbutton(preferencemain, text = "Bhojpuri", variable = bhojpurivar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    bhojpuric.place(x = 665, y = 415)
    bhojpuric.config(font=('',15))

    shoppingplabel=Label(preferencemain,text='Shopping Preference',bg='black',fg='white')
    shoppingplabel.config(font=('',30))
    shoppingplabel.place(x = 1125, y = 85)   
    amavar = IntVar()   
    flipvar = IntVar()   
    snapvar = IntVar()
    cluesvar = IntVar()
    myntravar = IntVar()
    amac = Checkbutton(preferencemain, text = "Amazon",variable = amavar,onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    amac.place(x = 1135, y = 140)
    amac.config(font=('',15))
    flipc = Checkbutton(preferencemain, text = "Flipkart", variable = flipvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    flipc.place(x = 1135, y = 195)
    flipc.config(font=('',15))
    snapc = Checkbutton(preferencemain, text = "Snapdeal", variable = snapvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    snapc.place(x = 1135, y = 250)
    snapc.config(font=('',15))
    cluesc = Checkbutton(preferencemain, text = "Shopclues", variable = cluesvar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    cluesc.place(x = 1135, y = 305)
    cluesc.config(font=('',15))
    myntrac = Checkbutton(preferencemain, text = "Myntra", variable = myntravar, onvalue = 1, offvalue = 0,bg='black',fg='white',selectcolor="midnight blue")
    myntrac.place(x = 1135, y = 360)
    myntrac.config(font=('',15))
    prefbutton = Button(preferencemain,text='Submit',command = pref)
    prefbutton.place(x = 665, y = 735)
    prefbutton.config(font=('',25))

# signup window function

def Signupmain():
    try:
            cursor.execute("create table users(USERNAME varchar(300) primary key,NAME varchar(300),PASSWORD varchar(500),EMAIL varchar(400),SUSPENSE MEDIUMTEXT,SCI_FI MEDIUMTEXT,SCI_TECH MEDIUMTEXT,ROMANTIC MEDIUMTEXT,FANTASY MEDIUMTEXT,LAST_LOGIN varchar(100),NEWS MEDIUMTEXT,MUSIC MEDIUMTEXT,SHOPPING MEDIUMTEXT);")
            con.commit()
    except:
            pass
    global signupmain
    global unamerentry
    global nameentry
    global passwordentry
    global emailentry
    try:
            r.destroy()
    except:
            pass
    signupmain=Tk()
    signupmain.geometry('1920x1080')
    signupmain.configure(bg='black')
    please = Label(signupmain,text = 'PLEASE FILL ALL THE DETAILS FOR GREAT EXPERIENCE!!',bg='black',fg='white')
    please.pack(pady=15)
    please.config(font=("Courier",30))
    name=Label(signupmain, text = 'Name',bg='black',fg='white')
    name.pack(pady=15)
    name.config(font=("Courier",20))
    nameentry=Entry(signupmain, width = 35)
    nameentry.pack(pady=15)
    nameentry.config(font=("Courier",20))
    email=Label(signupmain, text = 'Email',bg='black',fg='white')
    email.pack(pady=15)
    email.config(font=("Courier",20))
    emailentry=Entry(signupmain, width = 35)
    emailentry.pack(pady=15)
    emailentry.config(font=("Courier",20))
    uname=Label(signupmain, text = 'Username',bg='black',fg='white')
    uname.pack(pady=15)
    uname.config(font=("Courier",20))
    unamerentry=Entry(signupmain, width = 35)
    unamerentry.pack(pady=15)
    unamerentry.config(font=("Courier",20))
    password=Label(signupmain, text = 'Password',bg='black',fg='white')
    password.pack(pady=15)
    password.config(font=("Courier",20))
    passwordentry=Entry(signupmain,width=35)
    passwordentry.pack(pady=15)
    passwordentry.config(font=("Courier",20))
    Signup=Button(signupmain,text='Signup',command=mainaftersignup)
    Signup.pack(pady=15)
    Signup.config(font=("Courier",20))

# storing signup data into database

def mainaftersignup():
        if re.search(regex,emailentry.get()):
                try:    
                                cursor.execute("insert into users() values('{}','{}','{}','{}',',',',',',',',',',',' ',' ',' ',' ');".format(unamerentry.get(),nameentry.get(),passwordentry.get(),emailentry.get()))
                                con.commit()
                                with open('aalas.txt') as f:
                                        r = f.read()
                                s.sendmail('aalascare@gmail.com',emailentry.get(),r)
                                cursor.execute("select USERNAME,EMAIL,NAME from users where USERNAME = '{}' ;".format(unamerentry.get()))
                                data = cursor.fetchall()
                                global username_all
                                global email_all
                                global jii
                                global kii
                                global tii
                                global oii
                                global pii
                                global namee
                                namee = data[0][2]
                                username_all = data[0][0]
                                email_all = data[0][1]
                                cursor.execute("select SCI_TECH from users where USERNAME = '{}'; ".format(username_all))
                                sata = cursor.fetchall()
                                jii = sata[0][0]
                                cursor.execute("select SCI_FI from users where USERNAME = '{}'; ".format(username_all))
                                kata = cursor.fetchall()
                                kii = kata[0][0]
                                cursor.execute("select ROMANTIC from users where USERNAME = '{}'; ".format(username_all))
                                pata = cursor.fetchall()
                                pii = pata[0][0]
                                cursor.execute("select FANTASY from users where USERNAME = '{}'; ".format(username_all))
                                tata = cursor.fetchall()
                                tii = tata[0][0]
                                cursor.execute("select SUSPENSE from users where USERNAME = '{}'; ".format(username_all))
                                oata = cursor.fetchall()
                                oii = oata[0][0]
                                preferences()
                                
                                
                except:
                            already = Label(signupmain,text='Username alraedy taken',bg='black',fg='white')
                            already.config(font=("Courier",20))
                            already.pack()
        else:
            already = Label(signupmain,text='Incorrect Email',bg='black',fg='white')
            already.config(font=("Courier",20))
            already.pack()

# opening games:

def unfairmario():
        webbrowser.open('https://playunfairmario.net/')
        
def dino():
        webbrowser.open('https://chromedino.com/')
        
def commando():
        webbrowser.open('https://www.miniclip.com/games/commando-2/en/#t-w-c-H')
        

# opening games window

def gamesmain():
        global umi
        global di
        global ci
        gameswin = Tk()
        gameswin.geometry('1920x1080')
        gameswin.configure(bg='black')
        umi = PhotoImage(file='unfairmario.png',master=gameswin).subsample(2,2)
        di = PhotoImage(file='Dinogame.png',master=gameswin).subsample(2,2)
        ci = PhotoImage(file='Commando2.png',master=gameswin).subsample(2,2)
        backbe=Button(gameswin,text='Back',command=lambda: backbuttonfunc(gameswin,menu))
        backbe.config(font=("Courier",10))
        backbe.pack(side=LEFT,anchor=NW)
        gamesl=Label(gameswin,text='GAMES',bg='black',fg='SteelBlue2')
        gamesl.config(font=('Montserrat Medium',45))
        gamesl.pack(pady=10)
        unfairmariol = Label(gameswin,text='Unfair Mario',bg='Black',fg='white')
        unfairmariol.config(font=("Courier",20))
        unfairmariol.pack(pady=20)
        unfairmariob = Button(gameswin,text='Unfair Mario',command=unfairmario,image = umi)
        unfairmariob.pack(pady=20)
        dinol = Label(gameswin,text='Chrome Dino',bg='Black',fg='white')
        dinob = Button(gameswin,text='Chrome Dino',command=dino,image = di)
        dinol.config(font=("Courier",20))
        dinol.pack(pady=20)
        dinob.pack(pady=20)
        commandob = Button(gameswin,text='Commando 2',command=commando,image = ci)
        commandol = Label(gameswin,text='Commando 2',bg='Black',fg='white')
        commandol.config(font=("Courier",20))
        commandol.pack(pady=20)
        commandob.pack(pady=20)
        try:
                Mainmenu.destroy()
        except:
                pass
        try:
                mmroot.destroy()
        except:
                pass
        
        try:
                signupmain.destroy()
        except:
                pass
        
# opening entertainment window

def Entertainmentmain():
    global entertainment
    entertainment = Tk()
    entertainment.geometry('1920x1080')
    entertainment.configure(bg='black')
    backbe=Button(entertainment,text='Back',command=lambda: backbuttonfunc(entertainment,menu))
    backbe.config(font=("Courier",10))
    backbe.pack(side=LEFT,anchor=NW)
    entertainmentl=Label(entertainment,text='ENTERTAINMENT',bg='black',fg='SteelBlue2')
    entertainmentl.config(font=("Montserrat Medium",45))
    entertainmentl.pack(pady=20)
    Books=Button(entertainment,text='Books',command=Booksmain)
    Books.config(font=("Courier",30))
    Books.pack(pady=50)
    Music=Button(entertainment,text='Music',command=musicmain)
    Music.config(font=("Courier",30))
    Music.pack(pady=50)
    News=Button(entertainment,text='News',command=Newsmain)
    News.config(font=("Courier",30))
    News.pack(pady=50)
    try:
                Mainmenu.destroy()
    except:
                pass
    try:
                mmroot.destroy()
    
    except:
                pass
    try:
                signupmain.destroy()
    except:
                pass
# opening books window

def Booksmain():
    global booksmain
    booksmain = Tk()
    booksmain.geometry('1920x1080')
    booksmain.configure(bg='black')
    backbe=Button(booksmain,text='Back',command=lambda: backbuttonfunc(booksmain,Entertainmentmain))
    backbe.config(font=("Courier",10))
    backbe.pack(side=LEFT,anchor=NW,fill=X)
    booksl=Label(booksmain,text='Books',bg='black',fg='SteelBlue2')
    booksl.config(font=('Montserrat Medium',45))
    booksl.pack(pady=10)
    SciTec=Button(booksmain,text='Science and Technology',command=lambda: Scitecmain('SCI_TECH'),width=25)
    SciTec.config(font=("Courier",30))
    SciTec.pack(pady=30)
    Scifi=Button(booksmain,text='Sci-Fi',command=lambda: Scitecmain('SCI_FI'),width=25)
    Scifi.config(font=("Courier",30))
    Scifi.pack(pady=30)
    Romantic=Button(booksmain,text='Romantic',command=lambda: Scitecmain('ROMANTIC'),width=25)
    Romantic.config(font=("Courier",30))
    Romantic.pack(pady=30)
    Fantasy=Button(booksmain,text='fantasy',command=lambda: Scitecmain('FANTASY'),width=25)
    Fantasy.config(font=("Courier",30))
    Fantasy.pack(pady=30)
    Suspense=Button(booksmain,text='Suspense',command=lambda: Scitecmain('SUSPENSE'),width=25)
    Suspense.config(font=("Courier",30))
    Suspense.pack(pady=30)
    try:
            entertainment.destroy()
    except:
            pass
        
# opening downloaded book file

def openbook(f):
    os.startfile(f + '.pdf')
    

# updating the database with newly added books and creating it's button

def Scitecadd(inout):
     global jii
     global kii
     global tii
     global oii
     global pii
     jii = jii + scitecentry.get()+','
     kii = kii + scitecentry.get()+','
     pii = pii + scitecentry.get()+','
     tii = tii + scitecentry.get()+','
     oii = oii + scitecentry.get()+','
     if inout =='SCI_TECH':
             cursor.execute("update users set SCI_TECH = '{}' where USERNAME = '{}'; ".format(jii,username_all))
             con.commit()
     elif inout == 'SCI_FI':
             cursor.execute("update users set SCI_FI = '{}' where USERNAME = '{}'; ".format(kii,username_all))
             con.commit()
     elif inout=='ROMANTIC':
             cursor.execute("update users set ROMANTIC = '{}' where USERNAME = '{}'; ".format(pii,username_all))
             con.commit()
     elif inout=='FANTASY':
             cursor.execute("update users set FANTASY = '{}' where USERNAME = '{}'; ".format(tii,username_all))
             con.commit()
     else:
             cursor.execute("update users set SUSPENSE = '{}' where USERNAME = '{}'; ".format(oii,username_all))
             con.commit()
             
     addscitec=Button(second_frame,text=scitecentry.get(),command =lambda: openbook(scitecentry.get()),width=100)
     addscitec.config(font=("Courier",18))
     addscitec.pack(pady = 10)
     
# making book buttons

def add__button(window,file_path):
        
        c = Button(window,text=file_path,command= lambda: openbook(file_path),width=100)
        c.config(font=("Courier",18))
        c.pack(pady = 10)
              
# displaying button of stored books

def addbefore(window,file):
        
         
        with open(file+'.txt') as f:
                d = f.readlines()
        for  i in d:
                v = i[0:-1]
                add__button(window,v)
        
        if file =='SCI_TECH':
                        
                                cursor.execute("select SCI_TECH from users where USERNAME = '{}' ;".format(username_all))
                                data = cursor.fetchall() 
        elif file == 'SCI_FI':
                        
                                cursor.execute("select SCI_FI from users where USERNAME = '{}' ;".format(username_all))
                                data = cursor.fetchall()
        elif file == 'FANTASY':
                        
                                cursor.execute("select FANTASY from users where USERNAME = '{}' ;".format(username_all))
                                data = cursor.fetchall()
        elif file == 'ROMANTIC':
                        
                                cursor.execute("select ROMANTIC from users where USERNAME = '{}' ;".format(username_all))
                                data = cursor.fetchall()
        elif file == 'SUSPENSE':
                        
                                cursor.execute("select SUSPENSE from users where USERNAME = '{}' ;".format(username_all))
                                data = cursor.fetchall()

                                
        if data[0][0]!=',':
                v = data[0][0]
                d = v.split(sep=',')
                        
                f = d[1:-1]
                        
                for g in f:
                        add__button(window,g)
        else:
                pass
        
# book genre menu window

def Scitecmain(jonour):
     global second_frame
     global scitecentry
     scitecmain=Tk()
     scitecmain.geometry('1920x1080')
     scitecmain.configure(bg='black')
     mainframe = Frame(scitecmain)
     mainframe.configure(bg='black')
     mainframe.pack(fill=BOTH,expand=1)
     canvas = Canvas(mainframe)
     canvas.configure(bg='black')
     canvas.pack(side=LEFT, fill=BOTH, expand=1)
     my_scrollbar = Scrollbar(mainframe, orient=VERTICAL, command=canvas.yview)
     my_scrollbar.pack(side=RIGHT, fill=Y)
     canvas.configure(yscrollcommand=my_scrollbar.set)
     canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
     second_frame = Frame(canvas)
     second_frame.configure(bg='black')
     canvas.create_window((0,0),window=second_frame,anchor='nw',width=1520,height=100000) 
     backbe=Button(second_frame,text='Back',command=lambda: backbuttonfunc(scitecmain,Booksmain))
     backbe.config(font=("Courier",10))
     backbe.pack(side=LEFT,anchor=NW,fill=X)
     if jonour =='SCI_TECH':
             genrel=Label(second_frame,text='Science & Technology',bg='black',fg='SteelBlue2')
             genrel.config(font=("Montserrat Medium",40))
             genrel.pack(pady=10)
     elif jonour == 'SCI_FI':
             genrel=Label(second_frame,text='Science Fiction',bg='black',fg='SteelBlue2')
             genrel.config(font=("Montserrat Medium",40))
             genrel.pack(pady=10)
     elif jonour=='ROMANTIC':
             genrel=Label(second_frame,text='Romantic',bg='black',fg='SteelBlue2')
             genrel.config(font=("Montserrat Medium",40))
             genrel.pack(pady=10)
     elif jonour=='FANTASY':
             genrel=Label(second_frame,text='Fantasy',bg='black',fg='SteelBlue2')
             genrel.config(font=("Montserrat Medium",40))
             genrel.pack(pady=10)
     else:
             genrel=Label(second_frame,text='Suspense',bg='black',fg='SteelBlue2')
             genrel.config(font=("Montserrat Medium",40))
             genrel.pack(pady=10)     
     scitecentry=Entry(second_frame, width=50)
     scitecentry.config(font=("Courier",20))
     scitecentry.pack(pady=5)
     scitecadd=Button(second_frame, text='Add',command=lambda: Scitecadd(jonour))
     scitecadd.config(font=("Courier",20))
     scitecadd.pack(pady=15)
     browseb=Button(second_frame,text = 'Browse',command=browsef)
     browseb.config(font=("Courier",20))
     browseb.pack(pady=25)
     addbefore(second_frame,jonour)
     try:
             booksmain.destroy()
     except:
             pass
        
# for browsing more books online

def browsef():
        webbrowser.open('https://www.pdfdrive.com/')

# opening music online

def openmusic():
    webbrowser.open('https://gaana.com/search/'+searchentry.get())

# for making music menu window

def musicmain():
    global searchentry
    global musicimg
    musicmain=Tk()
    musicmain.geometry('1920x1080')
    musicmain.configure(bg='black')
    musicimg=PhotoImage(file='music.png',master=musicmain)
    musicimgl=Label(musicmain,image=musicimg)
    musicimgl.place(x=0, y=0, relwidth=1, relheight=1)    
    backbe=Button(musicmain,text='Back',command=lambda: backbuttonfunc(musicmain,Entertainmentmain))
    backbe.config(font=("Courier",10))
    backbe.pack(side=LEFT,anchor=NW,fill=X)
    musicl=Label(musicmain,text='Music',bg='black',fg='SteelBlue2')
    musicl.config(font=("Montserrat Medium",40))
    musicl.pack(pady=10)
    search=Label(musicmain,text='Search Songs',bg='black',fg='white')
    search.config(font=("Courier",30))
    search.pack(pady=10)
    searchentry=Entry(musicmain,width = 35)
    searchentry.config(font=("Courier",25))
    searchentry.pack(pady=10)
    searchent = Button(musicmain,text = 'search',command = openmusic)
    searchent.config(font=("Courier",22,"bold"))
    searchent.pack(pady=20)
    
    if mt[0]=='1':
            buttonnews = Button(musicmain,text='HINDI',command=lambda: webbrowser.open('https://gaana.com/album/hindi'),width=15)
            buttonnews.config(font=("Courier",20,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if mt[1]=='1':
            buttonnews = Button(musicmain,text='ENGLISH',command=lambda: webbrowser.open('https://gaana.com/album/english'),width=15)
            buttonnews.config(font=("Courier",20,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if mt[2]=='1':
            buttonnews = Button(musicmain,text='PUNJABI',command=lambda: webbrowser.open('https://gaana.com/album/punjabi'),width=15)
            buttonnews.config(font=("Courier",20,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if mt[3]=='1':
            buttonnews = Button(musicmain,text='TELUGU',command=lambda: webbrowser.open('https://gaana.com/album/telugu'),width=15)
            buttonnews.config(font=("Courier",20,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if mt[4]=='1':
            buttonnews = Button(musicmain,text='TAMIL',command=lambda: webbrowser.open('https://gaana.com/album/tamil'),width=15)
            buttonnews.config(font=("Courier",20,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if mt[5]=='1':
            buttonnews = Button(musicmain,text='BHOJPURI',command=lambda: webbrowser.open('https://gaana.com/album/bhojpuri'),width=15)
            buttonnews.config(font=("Courier",20,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    try:
            entertainment.destroy()
    except:
            pass

# for making news menu window

def Newsmain():
    global newsimg
    newsmain=Tk()
    newsmain.geometry('1920x1080')
    newsmain.configure(bg='black')
    newsimg=PhotoImage(file='news.png',master=newsmain)
    newsimgl=Label(newsmain,image=newsimg)
    newsimgl.place(x=0, y=0, relwidth=1, relheight=1)
    backbe=Button(newsmain,text='Back',command=lambda: backbuttonfunc(newsmain,Entertainmentmain))
    backbe.config(font=("Courier",10))
    backbe.pack(side=LEFT,anchor=NW,fill=X)
    newsl=Label(newsmain,text='News',bg='black',fg='SteelBlue2')
    newsl.config(font=("Montserrat Medium",40))
    newsl.pack(pady=10)
    if nt[0]=='1':
            buttonnews = Button(newsmain,text='BBC',command=lambda: webbrowser.open('www.bbc.com'),width=20)
            buttonnews.config(font=("Courier",15,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if nt[1]=='1':
            buttonnews = Button(newsmain,text='Times of India',command=lambda: webbrowser.open('https://timesofindia.indiatimes.com/home/headlines'),width=20)
            buttonnews.config(font=("Courier",15,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if nt[2]=='1':
            buttonnews = Button(newsmain,text='Hindustan Times',command=lambda: webbrowser.open('https://www.hindustantimes.com/topic/headline'),width=20)
            buttonnews.config(font=("Courier",15,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if nt[3]=='1':
            buttonnews = Button(newsmain,text='The Quint',command=lambda: webbrowser.open('https://www.thequint.com/'),width=20)
            buttonnews.config(font=("Courier",15,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if nt[4]=='1':
            buttonnews = Button(newsmain,text='Jagran',command=lambda: webbrowser.open('https://www.jagran.com/'),width=20)
            buttonnews.config(font=("Courier",15,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if nt[5]=='1':
            buttonnews = Button(newsmain,text='Aajtak',command=lambda: webbrowser.open('https://www.aajtak.in/'),width=20)
            buttonnews.config(font=("Courier",15,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if nt[6]=='1':
            buttonnews = Button(newsmain,text='NDTV',command=lambda: webbrowser.open('https://www.ndtv.com/latest'),width=20)
            buttonnews.config(font=("Courier",15,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if nt[7]=='1':
            buttonnews = Button(newsmain,text='Inshorts',command=lambda: webbrowser.open('https://inshorts.com/en/read/'),width=20)
            buttonnews.config(font=("Courier",15,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if nt[8]=='1':
            buttonnews = Button(newsmain,text='Dianikbhaskar',command=lambda: webbrowser.open('https://www.bhaskar.com/'),width=20)
            buttonnews.config(font=("Courier",15,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    if nt[9]=='1':
            buttonnews = Button(newsmain,text='Navbharat Times',command=lambda: webbrowser.open('https://navbharattimes.indiatimes.com/'),width=20)
            buttonnews.config(font=("Courier",15,"bold"))
            buttonnews.pack(pady=15)
    else:
            pass
    try:
            entertainment.destroy()
    except:
            pass

# making button to open the 'ABOUT' section of the app

def aboutfunc():
    with open('about.txt') as f:
            r = f.readlines()
    aboutmain = Tk()
    aboutmain.geometry('1920x1080')
    aboutmain.configure(bg='black')
    backbe=Button(aboutmain,text='Back',command=lambda: backbuttonfunc(aboutmain,settingfunc))
    backbe.config(font=("Courier",10))
    backbe.pack(side=LEFT,anchor=NW,fill=X)
    abouttitle=Label(aboutmain,text='About Us',bg='black',fg='SteelBlue2')
    abouttitle.config(font=("Montserrat Medium",40))
    abouttitle.pack(side=TOP,anchor=N)
    for i in r:
            aboutbody=Label(aboutmain,text=i,bg='black',fg='white')
            aboutbody.config(font=("Courier",18))
            aboutbody.pack()
    try:
            settingmain.destroy()
    except:
            pass

# displaying all the details of the user

def accountfunc():
    accountmain=Tk()
    accountmain.geometry('1920x1080')
    accountmain.configure(bg='black')
    backbe=Button(accountmain,text='Back',command=lambda: backbuttonfunc(accountmain,settingfunc))
    backbe.config(font=("Courier",10))
    backbe.pack(side=LEFT,anchor=NW,fill=X)
    accountl = Label(accountmain,text='Account Details',bg='black',fg='SteelBlue2')
    accountl.config(font=("Montserrat Medium",45))
    accountl.pack(pady=10)
    cursor.execute("select * from users where USERNAME = '{}' ;".format(username_all))
    data = cursor.fetchall()
    label_1 = Label(accountmain,text='USERNAME: '+data[0][0],bg='black',fg='white')
    label_1.config(font=("Courier",30))
    label_1.place(x=60,y=180)
    label_2 = Label(accountmain,text='NAME: '+data[0][1],bg='black',fg='white')
    label_2.config(font=("Courier",30))
    label_2.place(x=60,y=260)
    label_4 = Label(accountmain,text='EMAIL: '+data[0][3],bg='black',fg='white')
    label_4.config(font=("Courier",30))
    label_4.place(x=60,y=340)
    try:
            settingmain.destroy()
    except:
            pass
        
# updating a new password in the database

def newpassword():
                cursor.execute("select PASSWORD from users where USERNAME = '{}' ;".format(username_all))
                data = cursor.fetchall()
                if data[0][0]==cuurpasswentry.get():
                        with open('passchangeemail.txt') as d:
                                p = d.read()
                        cursor.execute("update users set PASSWORD = '{}' where USERNAME = '{}' ".format(newpasswentry.get(),username_all))
                        con.commit()
                        change = Label(passwordchangemain,text='Password change successful',bg='black',fg='White')
                        change.config(font=("Courier",30))
                        change.pack()
                        s.sendmail('aalascare@gmail.com',email_all,p)
                else:
                        userpasssss = Label(passwordchangemain,text='Password did not match',bg='black',fg='White')
                        userpasssss.config(font=("Courier",30))
                        userpasssss.pack()  

# displaying password change window

def passwordchangefunc():
        global cuurpasswentry
        global newpasswentry
        global passwordchangemain
        passwordchangemain=Tk()
        passwordchangemain.geometry('1920x1080')
        passwordchangemain.configure(bg='black')
        backbe=Button(passwordchangemain,text='Back',command=lambda: backbuttonfunc(passwordchangemain,settingfunc))
        backbe.config(font=("Courier",10))
        backbe.pack(side=LEFT,anchor=NW,fill=X)
        passwchangel=Label(passwordchangemain,text='Password Change',bg='black',fg='SteelBlue2')
        passwchangel.config(font=("Montserrat Medium",45))
        passwchangel.pack(pady=10)
        currpasswlabel=Label(passwordchangemain,text='Current Password',bg='black',fg='White')
        currpasswlabel.config(font=("Courier",25))
        currpasswlabel.pack(pady=20)
        cuurpasswentry=Entry(passwordchangemain,width=35)
        cuurpasswentry.config(font=("Courier",25))
        cuurpasswentry.pack(pady=20)
        newpasswlabel=Label(passwordchangemain,text='New Password',bg='black',fg='White')
        newpasswlabel.config(font=("Courier",25))
        newpasswlabel.pack(pady=20)
        newpasswentry=Entry(passwordchangemain,width=35)
        newpasswentry.config(font=("Courier",25))
        newpasswentry.pack(pady=20)
        changepasswbutton=Button(passwordchangemain,text='Change Password',command=newpassword)
        changepasswbutton.config(font=("Courier",25))
        changepasswbutton.pack(pady=20)
        try:
                settingmain.destroy()
        except:
                pass

# updating email in the database

def newemail():
        if re.search(regex,curremailentry.get()):
            cursor.execute("update users set Email = '{}' where USERNAME = '{}' ".format(curremailentry.get(),username_all))
            con.commit()
            emailchange = Label(emailchangemain,text = 'Email Change Successful',bg='black',fg='White')
            emailchange.config(font=("Courier",30))
            emailchange.pack(pady=30)
            s.sendmail('aalascare@gmail.com',curremailentry.get(),'Your Email was Changed Successfully!!')
        else:
             already=Label(emailchangemain,text='Incorrect Email Format',bg='black',fg='white')
             already.config(font=("Courier",30))
             already.pack(pady = 30)

# displaying email change window

def emailchangefunc():
        global curremailentry
        global emailchangemain
        emailchangemain=Tk()
        emailchangemain.geometry('1920x1080')
        emailchangemain.configure(bg='black')
        backbe=Button(emailchangemain,text='Back',command=lambda: backbuttonfunc(emailchangemain,settingfunc))
        backbe.config(font=("Courier",10))
        backbe.pack(side=LEFT,anchor=NW,fill=X)
        emailchangel=Label(emailchangemain,text='Email Change',bg='black',fg='SteelBlue2')
        emailchangel.config(font=("Montserrat Medium",45))
        emailchangel.pack(pady=20)
        curremaillabel=Label(emailchangemain,text='New Email',bg='black',fg='White')
        curremaillabel.config(font=("Courier",30))
        curremaillabel.pack(pady=40)
        curremailentry=Entry(emailchangemain,width=35)
        curremailentry.config(font=("Courier",30))
        curremailentry.pack(pady=40)
        changeemailbutton=Button(emailchangemain,text='Change Email',command=newemail)
        changeemailbutton.config(font=("Courier",30))
        changeemailbutton.pack(pady=40)
        try:
                settingmain.destroy()
        except:
                pass

# displaying setting window

def settingfunc():
    global settingmain
    settingmain = Tk()
    settingmain.geometry('1920x1080')
    settingmain.configure(bg='black')
    backbe=Button(settingmain,text='Back',command=lambda: backbuttonfunc(settingmain,menu))
    backbe.config(font=("Courier",10))
    backbe.pack(side=LEFT,anchor=NW,fill=X)
    settingl=Label(settingmain,text='Settings',bg='black',fg='SteelBlue2')
    settingl.config(font=("Montserrat Medium",45))
    settingl.pack(pady=10)
    passwchangebutton=Button(settingmain,text='Password Change',command=passwordchangefunc)
    passwchangebutton.config(font=("Courier",25))
    passwchangebutton.pack(pady=30)
    emailchangebutton=Button(settingmain,text='Email Change',command=emailchangefunc)
    emailchangebutton.config(font=("Courier",25))
    emailchangebutton.pack(pady=30)
    accountdetailbutton=Button(settingmain,text='Account Details',command=accountfunc)
    accountdetailbutton.config(font=("Courier",25))
    accountdetailbutton.pack(pady=30)
    aboutbutton=Button(settingmain,text='About',command=aboutfunc)
    aboutbutton.config(font=("Courier",25))
    aboutbutton.pack(pady=30)
    appversionlabel=Label(settingmain,text='App Version mk.4.2.0',bg='black',fg='SteelBlue1')
    appversionlabel.config(font=("Montserrat Light",15))
    appversionlabel.pack(side=BOTTOM,anchor=S,fill=Y,pady = 60)
    try:
            Mainmenu.destroy()
    except:
            pass
    try:
                mmroot.destroy()
    
    except:
                pass
    try:
                signupmain.destroy()
    except:
                pass

# opening searched item

def amazonsearch(open_this):
        v = open_this+amazonsearchentry.get()
        webbrowser.open(v)

# displaying search bar window

def amazonshoppingfunc(what_search):
    global amazonsearchentry
    amazonshoppingmain = Tk()
    amazonshoppingmain.geometry('1920x1080')
    amazonshoppingmain.configure(bg='black')
    backbe=Button(amazonshoppingmain,text='Back',command=lambda: backbuttonfunc(amazonshoppingmain,shoppingfunc))
    backbe.config(font=("Courier",10))
    backbe.pack(side=LEFT,anchor=NW,fill=X)
    amazonsearchlabel=Label(amazonshoppingmain,text='Search',bg='black',fg='SteelBlue2')
    amazonsearchlabel.config(font=("Montserrat Medium",40))
    amazonsearchlabel.pack(pady=20)
    amazonsearchentry=Entry(amazonshoppingmain,width=35)
    amazonsearchentry.config(font=("Courier", 30))
    amazonsearchentry.pack(pady=40)
    ama = Button(amazonshoppingmain,text='search',command = lambda: amazonsearch(what_search))
    ama.config(font=("Courier", 30))
    ama.pack(pady=40)
    try:
            shoppingmain.destroy()
    except:
            pass

# browsing through grocery

def grocery():
        webbrowser.open('https://www.amazon.in/pantry-online-grocery-shopping-store/b?ie=UTF8&node=9574332031')

# displaying shopping window

def shoppingfunc():
    global shoppingmain
    global shoppingimg
    shoppingmain = Tk()
    shoppingmain.geometry('1920x1080')
    shoppingmain.configure(bg='black')
    shoppingimg=PhotoImage(file='shopping.png',master=shoppingmain)
    shoppingimgl=Label(shoppingmain,image=shoppingimg)
    shoppingimgl.place(x=0, y=0, relwidth=1, relheight=1)
    backbe=Button(shoppingmain,text='Back',command=lambda: backbuttonfunc(shoppingmain,menu))
    backbe.config(font=("Courier",10))
    backbe.pack(side=LEFT,anchor=NW,fill=X)
    shoppingl=Label(shoppingmain,text='Shopping',bg='black',fg='SteelBlue2')
    shoppingl.config(font=("Montserrat Medium",45))
    shoppingl.pack(pady=10)
    grocerybutton=Button(shoppingmain,text='Grocery',command = grocery,width=10)
    grocerybutton.config(font=("Courier", 30,"bold"))
    grocerybutton.pack(pady=20)
    if st[0] == '1':
            amazonshopping=Button(shoppingmain,text='Amazon',command=lambda: amazonshoppingfunc('https://www.amazon.in/s?k='),width=10)
            amazonshopping.config(font=("Courier", 30,"bold"))
            amazonshopping.pack(pady=20)
    else:
            pass
    if st[1]=='1':
            amazonshopping=Button(shoppingmain,text='Flipkart',command=lambda: amazonshoppingfunc('https://www.flipkart.com/search?q='),width=10)
            amazonshopping.config(font=("Courier", 30,"bold"))
            amazonshopping.pack(pady=20)
    else:
            pass
    if st[2]=='1':
            amazonshopping=Button(shoppingmain,text='Snapdeal',command=lambda: amazonshoppingfunc('https://www.snapdeal.com/search?keyword='),width=10)
            amazonshopping.config(font=("Courier", 30,"bold"))
            amazonshopping.pack(pady=20)
    else:
            pass
    if st[3]=='1':
            amazonshopping=Button(shoppingmain,text='Shopclues',command=lambda: amazonshoppingfunc('https://www.shopclues.com/search?q='),width=10)
            amazonshopping.config(font=("Courier", 30,"bold"))
            amazonshopping.pack(pady=20)
    else:
            pass
    if st[4]=='1':
            amazonshopping=Button(shoppingmain,text='Myntra',command=lambda: amazonshoppingfunc('https://www.myntra.com/'),width=10)
            amazonshopping.config(font=("Courier", 30,"bold"))
            amazonshopping.pack(pady=20)
    else:
            pass
    try:
                Mainmenu.destroy()
    except:
                pass
    try:
                mmroot.destroy()
    except:
                pass
    
    try:
                signupmain.destroy()
    except:
                pass

# making primary root window

r=Tk()
r.geometry('1920x1080')
emplabel3=Label(r,text='').pack()
img=PhotoImage(file = "images_result.png")
bgimglabel=Label(r,image=img)
bgimglabel.place(x=0, y=0, relwidth=1, relheight=1)

rframe1=Frame(r,bg='black')
rframe1.pack()

aalaslabel=Label(rframe1,text='E-Mart',bg='black',fg='white')
aalaslabel.config(font=("Courier",40))
aalaslabel.pack()
explabel=Label(rframe1,text='Your Destination to an Ultimate Experience!!',bg='black',fg='white')
explabel.config(font=("Courier", 25))

explabel.pack()
rframe=Frame(r,width=500, height=800,bg='black')
rframe.place(relx=.5, rely=.5, anchor="center")

username=Label(rframe, text = 'Username',bg='black',fg='white')
username.pack()
username.config(font=("Courier", 30))

unameentry=Entry(rframe, width = 35)
unameentry.pack()
unameentry.config(font=("Courier", 15))

p=Label(rframe,text='Password',bg='black',fg='white')
p.pack()
p.config(font=("Courier", 30))

pentry=Entry(rframe,show = '*',width=35)
pentry.pack()
pentry.config(font=("Courier", 15))

    
login=Button(rframe,text='Login',command=Mainmenu)
login.place(x=115,y=200)
login.config(font=("Courier", 15))

emplabel2=Label(rframe,text='',bg='black',fg='white')
emplabel2.pack(pady=10)
emplabel2.config(font=("Courier", 15))


emplabel=Label(rframe,text='',bg='black',fg='white')
emplabel.pack(pady=10)
emplabel.config(font=("Courier", 15))
signup=Button(rframe,text='Signup',command=Signupmain,)
signup.place(x=215,y=200)
signup.config(font=("Courier", 15))
fpassword=Button(rframe,text='Forget Password',command=fpassword)
fpassword.pack(pady=30)
fpassword.config(font=("Courier", 15))


r.mainloop()
s.close()
con.close()
