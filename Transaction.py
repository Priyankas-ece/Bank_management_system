from tkinter import*
import pymysql
con=pymysql.connect(user="root",password="",host="localhost",database="bank_details")
cur=con.cursor()
a=Tk()
f=("times new roman", 14)
bg="purple"
f1="red"
a.state("zoomed")

Accountnumber= StringVar()
Modeofpay= StringVar()
Checknumber= StringVar()
Transactiontype= StringVar()
Date= StringVar()
Amount= StringVar()
Accounttype= StringVar()
Balance= IntVar()

def Check():
    cur.execute("select * from app")
    rec=cur.fetchall()
    flag=0
    for i in rec:
        if i[0]==Accountnumber.get():
            Label(a,text="NAME:"+i[1],fg=f1,font=f).place(x=750,y=110)
            Label(a,text="ACCOUNT TYPE:"+i[6],fg=f1,font=f).place(x=750,y=160)
            Label(a,text="DATE:"+i[12],fg=f1,font=f).place(x=750,y=210)
            Label(a,text="BALANCE:"+str(i[1]),fg=f1,font=f).place(x=750,y=260)

#LABEL
Label(a,text="TRANSACTION",fg="red",font=("Algerian",40)).pack()
Label(a,text="ACCOUNT NUMBER",fg=f1,font=f).place(x=50,y=70)
Label(a,text="MODE OF PAY",fg=f1,font=f).place(x=50,y=70)
Label(a,text="CHECK NUMBER",fg=f1,font=f).place(x=50,y=70)
Label(a,text="TRANSACTION TYPE",fg=f1,font=f).place(x=50,y=70)
Label(a,text="DATE",fg=f1,font=f).place(x=50,y=70)
Label(a,text="AMOUNT",fg=f1,font=f).place(x=50,y=70)
Label(a,text="ACCOUNT TYPE",fg=f1,font=f).place(x=50,y=70)
Label(a,text="BALANCE",fg=f1,font=f).place(x=50,y=70)

#ENTRY
Entry(a,textvariable=Accountnumber,font=f).place(x=260,y=70)
Entry(a,textvariable=Checknumber,font=f).place(x=260,y=170)
Entry(a,textvariable=Date,font=f).place(x=260,y=270)
Entry(a,textvariable=Amount,font=f).place(x=260,y=320)
Entry(a,textvariable=Balance,font=f).place(x=260,y=420)

#RADIO BUTTON
Radiobutton(a,text="CASH",font=f,value="Cash",variable=Modeofpay).place(x=260,y=120)
Radiobutton(a,text="CHECK",font=f,value="Check",variable=Modeofpay).place(x=380,y=120)
Radiobutton(a,text="DEPOSIT",font=f,value="Deposit",variable=Transactiontype).place(x=260,y=220)
Radiobutton(a,text="WITHDRAW",font=f,value="Withdraw",variable=Transactiontype).place(x=380,y=220)
Radiobutton(a,text="SAVINGS",font=f,value="Savings",variable=Accounttype).place(x=260,y=370)
Radiobutton(a,text="CURRENT",font=f,value="Current",variable=Accounttype).place(x=380,y=370)

def Save():
    cur.execute("insert into transaction values('%s','%s'.'%s','%s,'%d',%d,'%s',%d)"%(Accountnumber.get(),Modeofpay.get(),Checknumber.get(),Transactiontype.get(),Date.get(),Accounttype.get(),Balance.get()))
    if Transactiontype.get()=='Deposit':
        cur.execute("Update transaction set Balance=Balance+%d where Accountnumber='%s'"%(Amount.get(),Accountnumber.get()))
        cur.execute("commit")

def Exit():
    a.destroy()

#BUTTON
Button(a,text="SAVE",font=f,command=Save).place(x=260,y=760)
Button(a,text="CHECK",font=f,command=Check).place(x=360,y=760)
Button(a,text="EXIT",font=f,command=Exit).place(x=560,y=110)

a.mainloop()