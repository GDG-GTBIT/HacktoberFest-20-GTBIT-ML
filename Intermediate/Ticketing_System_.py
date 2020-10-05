import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pandas as pd
import mysql.connector
from tkinter import *

from tkinter import messagebox
con= mysql.connector.connect(user='root', password='*********',
                              host='localhost',
                              database='ts')
rootp=Tk()
Label(rootp,text="AP AIRLINE BOOKING SYSTEM",font="Bold 20").pack()
def fun8():
    rootp.destroy()
    root4=Tk()
    root4.title("WELCOME TO OUR Cancellation System")
    
    Label(root4,text="Passport_Number").grid(row=0,column=0)
    c1=Entry(root4)
    c1.grid(row=0,column=1)
    
    Label(root4,text="Name").grid(row=1,column=0)
    c2=Entry(root4)
    c2.grid(row=1,column=1)
    
    Label(root4,text="Class").grid(row=2,column=0)
    c3=ttk.Combobox(root4,height=5,width=15,values=["First","Business","Economy"])
    c3.grid(row=2,column=1)
     
    Label(root5,text="Boarding").grid(row=3,column=0)
    c4=ttk.Combobox(root5,height=5,width=15,values=["New Delhi","Mumbai","Chennai","Kolkata","Lucknow","Goa","Hyderabad","Bangalore","Chandigarh","Ahmedabad"])
    c4.grid(row=3,column=1)
    
    def fun2():
        a=c1.get()
        b=c2.get()
        c=c3.get()
        d=d4.get()
        cur=con.cursor()
        x=str(a)
        y=str(b)
        con.commit()
        if a=='' or b=='' or c=='':
             tkMessageBox.showerror("Oops","Please Fill all the Spaces to Proceed")
        else:     
             if c=="Economy":
                cur.execute("delete from apl where Passport_Number=(?) and Name=(?)",(a,b,))
                cur.execute("select * from apl")
                tkMessageBox.showinfo("Your Reservation is cancelled",cur.fetchall())
             if c=="Business":
                cur.execute("delete from apl where Passport_Number=(?) and Name=(?)",(a,b,))
                cur.execute("select * from apl")
                tkMessageBox.showinfo("Your Reservation is cancelled",cur.fetchall())
             else:
                    cur.execute("delete from ap where Passport_Number=x and Boarding=y")
                    cur.execute("select * from ap")
                    tkMessageBox.showinfo("Your Reservation is cancelled",cur.fetchall())
                    
    Bc=Button(root4,text="Cancel Reservation",command=fun2).grid(row=4,column=0)
    root4.mainloop()
def fun9():
    rootp.destroy()
    root5=Tk()
    root5.title("Welcome,Search flights")
    
    Label(root5,text="Boarding").grid(row=0,column=0)
    w1=ttk.Combobox(root5,height=5,width=15,values=["New Delhi","Mumbai","Chennai","Kolkata","Lucknow","Goa","Hyderabad","Bangalore","Chandigarh","Ahmedabad"])
    w1.grid(row=0,column=1)
    
    Label(root5,text="Destination").grid(row=1,column=0)
    w2=ttk.Combobox(root5,height=5,width=15,values=["New Delhi","Mumbai","Chennai","Kolkata","Lucknow","Goa","Hyderabad","Bangalore","Chandigarh","Ahmedabad"])
    w2.grid(row=1,column=1)
    
    Label(root5,text="Date").grid(row=2,column=0)
    w3=ttk.Combobox(root5,text="Date",height=5,width=15,values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])
    w3.grid(row=2,column=1)
    
    Label(root5,text="Month").grid(row=3,column=0)
    w4=ttk.Combobox(root5,text="Month",height=5,width=15,values=[1,2,3,4,5,6,7,8,9,10,11,12])
    w4.grid(row=3,column=1)
    
    Label(root5,text='Class').grid(row=4,column=0)
    w5=ttk.Combobox(root5,text='Class',height=5,width=15,values=["First","Business","Economy"])
    w5.grid(row=4,column=1)
   
    def fun10():
        a=w1.get()
        b=w2.get()
        c=w3.get()
        d=w4.get()
        e=w5.get()
        f=["Spicejet","Indigo","Airindia","kingfisher"]
        cur=con.cursor()
        if a=='' or b=='' or c=='' or d=='':
            messagebox.showerror("Error","Cant leave any field empty")
           
        else:
             if a!=b:
                 cur.execute("create table ap(Boarding char(20),Destination char(20),Day char(12),Date int(31),class char(10))")
                 cur.execute("insert into ap values('New Delhi','Mumbai','Sunday',1.00,'Economic')")
                 cur.execute("insert into ap values('New Delhi','Chennai','Monday',1.00,'First')")
                 cur.execute("insert into ap values('New Delhi','Lucknow','Tuesday',1.00,'Economic')")
                 cur.execute("insert into ap values('Kolkata','Delhi','Wednesday',1.00,'Economic')")
                 cur.execute("insert into ap values('Mumbai','New Delhi','Wednesday',7.00,'First')")
                 cur.execute("select * from ap where Boarding=? and Destination=? and Day=?",(a,b,c,))
                 con.commit()
                 e=cur.fetchall()
                 messagebox.showinfo("Flights Available are",f)
             else:
                messagebox.showerror("Oops","boarding and destination can't be same")
        
    Bs=Button(root5,text="Search",command=fun10).grid(row=5,column=0)
    root5.mainloop()
    
def fun5():
    rootp.destroy()
    root=Tk()
    root.title('Flight Search And Booking')
   
    Label(root,text="Passport_Number").grid(row=0,column=0)
    b1=Entry(root)
    b1.grid(row=0,column=1)    
   
    Label(root,text="Name").grid(row=1,column=0)
    b2=Entry(root)
    b2.grid(row=1,column=1)
    
    Label(root,text="Boarding").grid(row=2,column=0)
    b3=ttk.Combobox(root,height=5,width=15,values=["New Delhi","Mumbai","Chennai","Kolkata","Lucknow","Goa","Hyderabad","Bangalore","Chandigarh","Ahmedabad"])
    b3.grid(row=2,column=1)
    
    Label(root,text='Destination').grid(row=3,column=0)
    b4=ttk.Combobox(root,height=5,width=15,values=["New Delhi","Mumbai","Chennai","Kolkata","Lucknow","Goa","Hyderabad","Bangalore","Chandigarh","Ahmedabad"])
    b4.grid(row=3,column=1)

    Label(root,text='Class').grid(row=4,column=0)    
    b5=ttk.Combobox(root,text='Class',height=5,width=15,values=["First","Business","Economy"])
    b5.grid(row=4,column=1)
    
    
    Label(root,text="Date").grid(row=5,column=0)
    b6=ttk.Combobox(root,text="Date",height=5,width=15,values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])
    b6.grid(row=5,column=1)
    
    Label(root,text="Month").grid(row=6,column=0)
    b7=ttk.Combobox(root,text="Month",height=5,width=15,values=[1,2,3,4,5,6,7,8,9,10,11,12])
    b7.grid(row=6,column=1)
    
    def fun():
        a=b1.get()
        b=b2.get()
        c=b3.get()
        d=b4.get()
        e=b5.get()
        f=b6.get()
        g=b7.get()
        x=(a,b,e,c)
        cur=con.cursor()
        
        if a=='' or b=='' or c=='' or d=='' or e=='' or f=='':
            messagebox.showerror("OOPS","you can't leave any field empty")
        else :
                    
                if a!=b:
                    #cur.execute("create table ticketing(boarding char(20),destination char(20),Class char(3),day char(12),date int(31),Passport_number int(250))")
                    cur.execute("insert into apl values(?,?,?,?)",x)
                    messagebox.showinfo("Congratulations!!","Your Seat has been Reserved")
                    con.commit()
                    cur.execute("Select * from apl where Passport_Number=(?)",(a,))
                    messagebox.showinfo("records",cur.fetchall())
                else:
                    messagebox.showerror("Error","You can't Choose the same city")
            
    Bi=Button(root,text="Insert",command=fun).grid(row=7,column=1)
    
    root.mainloop()
    
B1=Button(rootp,text="Cancel Booking",command=fun8).pack()
B2=Button(rootp,text="Search Flight",command=fun9).pack()
B3=Button(rootp,text="Book Flight",command=fun5).pack()


rootp.mainloop()
    
