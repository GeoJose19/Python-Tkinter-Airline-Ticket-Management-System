#GEMAGO AIRLINES BOOKING SYSTEM

#Importing all the necessary modules
from tkinter import*
import tkinter.messagebox
import pickle
from prettytable import PrettyTable
from PIL import ImageTk,Image 
import csv
import os
import mysql.connector
import random

def project():
    
    def booking():
        
        screen2=Toplevel(screen1)
        screen2.geometry("1366x768")
        screen2.title("Book a ticket")

        C = Canvas(screen2, bg="black", height=250, width=300)
        filename = PhotoImage(file = "D:/Python/rsz_11.png")
        background_label = Label(screen2, image=filename)                      #Canvas for background picture
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.grid()
        
        def save_info():
            
            try:
                firstname_info=firstname.get()
                lastname_info=lastname.get()
                age_info=age.get()
                gender_info=gender.get()
                from_info=from1.get()
                to_info=to.get()
                Passport_id_info=Passport_id.get()
                date_info=date.get()
                classtype_info=classtype.get()
                print("\nFirst Name:",firstname_info,"\nLast Name:",lastname_info,"\nAge:",age_info,"\nGender:",gender_info,"\nFrom:",from_info,"\nTo:",\
                      to_info,"\nPassport ID:",Passport_id_info,"\nDate:",date_info,"\nClass Type:",classtype_info)
            except:
                print("Input Not Recognized")


            try:
                with open("Gemago.dat","rb+") as k:
                    t=pickle.load(k)
                    t.append([x,firstname_info,lastname_info,age_info,gender_info,Passport_id_info,date_info,classtype_info,from_info,to_info])         #Saving into file
                    k.seek(0)
                    print("\nSuccessfully registered\n")
                    pickle.dump(t,k)
            except:
                print("Could not save to file")
                
            try:
                db=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="gemago")           #Saving into database
                mycursor=db.cursor()
                q="insert into ticket values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(x,firstname_info,lastname_info,age_info,gender_info,from_info,to_info,Passport_id_info,date_info,classtype_info)
                mycursor.execute(q)
                db.commit()
                db.close()
            except:
                print("Could not upload to database")
                
            firstname_entry.delete(0,END)
            lastname_entry.delete(0,END)
            age_entry.delete(0,END) 
            Passport_id_entry.delete(0,END)
            date_entry.delete(0,END)

            payment()

        def unicode():
            global x
            id1=random.randint(100000,999999)           #Unique Code Function
            x=id1
            with open("IDcodes.dat","rb+") as k:
                t=pickle.load(k)
                if x in t:
                    unicode()

            try:
                with open("IDcodes.dat","rb+") as k:
                    t=pickle.load(k)
                    t.append(x)                                               #Appending unique code into Binary file
                    k.seek(0)
                    pickle.dump(t,k)
            except:
                print("Could not update ID file")
                
            tkinter.messagebox.showinfo("ID",id1)
            print("ID:",x)
            save_info()
          
        F1=Frame(screen2,width=100,bg="White")
        F1.grid(row=0,column=30,padx=2,pady=2,ipadx=2,ipady=2)      #Creating Frames
        F3=Frame(screen2,width=100,bg="White")
        F3.grid(row=2,column=30)
        F2=Frame(screen2,width=100,bg="White")
        F2.grid(row=1,column=30,padx=10,pady=10,ipadx=10,ipady=10)
        
        heading=Label(F1,text="BOOK YOUR TICKETS",padx=2,pady=2,font="Arial 28 underline bold italic",fg="Black",bg="White",width='25',height="2") 
        heading.pack()

        firstname=Label(F2,text="FIRSTNAME  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=0,column=0,padx=15,pady=15)
        lastname=Label(F2,text="LASTNAME ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=1,column=0,padx=15,pady=15)
        age=Label(F2,text="AGE  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=2,column=0,padx=15,pady=15)
        gender=Label(F2,text="GENDER  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=3,column=0,padx=15,pady=15)                          #Creating and Placement Labels
        from1=Label(F2,text="DEPARTURE CITY  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=0,column=3,padx=15,pady=15)
        to=Label(F2,text="ARRIVAL CITY  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=1,column=3,padx=15,pady=15)
        Passport_id=Label(F2,text="PASSPORT ID ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=4,column=0,padx=15,pady=15)
        classtype=Label(F2,text="CLASS TYPE  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=2,column=3,padx=15,pady=15)
        date=Label(F2,text="DATE OF DEPARTURE  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=5,column=0,padx=15,pady=15)

        def message():
            tkinter.messagebox.showinfo("Confirmation","Confirm please")
            answer=tkinter.messagebox.askquestion("Confirmation?","Are you sure you want to proceed?")
            if answer=="yes":
                unicode()
                
        firstname=StringVar()
        lastname=StringVar()
        age=IntVar()                        #Assigning Variables
        gender=StringVar()
        from1=StringVar()
        to=StringVar()
        Passport_id=StringVar()
        date=StringVar()
        classtype=StringVar()

        firstname_entry=Entry(F2,textvariable=firstname,width="30")
        lastname_entry=Entry(F2,textvariable=lastname,width="30")
        age_entry=Entry(F2,textvariable=age,width="30")
        gender_entry=OptionMenu(F2,gender,"M","F","Others")
        from1_entry=OptionMenu(F2,from1,"Cochin","Dubai","Tokyo","Newyork","London")            #Creating Entries
        to_entry=OptionMenu(F2,to,"Cochin","Dubai","Tokyo","Newyork","London")
        Passport_id_entry=Entry(F2,textvariable=Passport_id,width="30")
        classtype_entry=OptionMenu(F2,classtype,"ECONOMY CLASS","BUSINESS CLASS","FIRST CLASS")
        date_entry=Entry(F2,textvariable=date,width="30")

        firstname_entry.grid(row=0,column=1,padx=10,pady=10)
        lastname_entry.grid(row=1,column=1,padx=10,pady=10)
        age_entry.grid(row=2,column=1,padx=10,pady=10)
        gender_entry.grid(row=3,column=1,padx=10,pady=10)           #Placing Entries
        from1_entry.grid(row=0,column=4,padx=10,pady=10)
        to_entry.grid(row=1,column=4,padx=10,pady=10)
        Passport_id_entry.grid(row=4,column=1,padx=10,pady=10)
        classtype_entry.grid(row=2,column=4,padx=10,pady=10)
        date_entry.grid(row=5,column=1,padx=10,pady=10)
        
        submit=Button(F3,text="SUBMIT",width="30",height="3",command=message,bg="ORANGE").grid(row=0,column=1)

        next_button=Button(F3,text="NEXT",width="30",height="3",command=payment,bg="ORANGE").grid(row=0,column=2)
        
        prev_button=Button(F3,text="PREVIOUS",width="30",height="3",command=baggage,bg="ORANGE").grid(row=0,column=0)

        screen2.mainloop()
       
    def payment():
        
        screen3=Toplevel(screen1)
        screen3.geometry("1366x768")
        screen3.title("Payment")
        
        C = Canvas(screen3, bg="black", height=250, width=300)
        filename = PhotoImage(file = "D:/Python/Paris.png")
        background_label = Label(screen3, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.grid()
        
        def saved_info():
            
            idd_info=idd.get()
            card_type_info=clicked.get()
            card_no_info=card_no.get()
            admin_info=admin.get()
            cvv_info=cvv.get()
            exp_d_info=exp_d.get()
            exp_y_info=exp_y.get()

            print("\nID:",idd_info,"\nCard Type:",card_type_info,"\nCard No:",card_no_info,"\nAdmin No:",admin_info,"\nCVV:",cvv_info,"\nExpiry Date:",exp_d_info,"\nExpiry Year:",exp_y_info)        
                 
            idd_entry.delete(0,END)
            card_no_entry.delete(0,END)
            admin_entry.delete(0,END)
            cvv_entry.delete(0,END)
            exp_d_entry.delete(0,END)
            exp_y_entry.delete(0,END)
            
            try:
                with open("Gemago.dat","rb+") as b:
                    t=pickle.load(b)
                    L1=[idd_info,card_type_info,card_no_info,admin_info,cvv_info,exp_d_info,exp_y_info]
                    for i in t:
                        if i[0]==L1[0]:
                            i.extend(L1)        #Extending already existing details(Booking) with Payment Details
                    b.seek(0)
                    pickle.dump(t,b)
                    b.seek(0)
            except:
                print("Could not write to file")

            try:
                with open("GEMAGOfares.csv","r",newline='') as f, open("Gemago.dat","br") as f1:
                    rec=pickle.load(f1)
                    wobj=csv.reader(f)
                    LB=[]
                    LP=[]
                    for i in rec:
                        if i[0]==idd_info:              #Calculating Price
                            LB=i
                            LP=i
                    for r in wobj:
                        if r[0]==LB[8] and r[1]==LB[9] and LB[7]=="ECONOMY CLASS":                             
                            print("Total Amount to be paid : Rs. ",(int(r[2])+int(r[3])))
                        if r[0]==LB[8] and r[1]==LB[9] and LB[7]=="FIRST CLASS":                             
                            print("Total Amount to be paid : Rs. ",(int(r[2])+int(r[3])+1000))
                        if r[0]==LB[8] and r[1]==LB[9] and LB[7]=="BUSINESS CLASS":                             
                                        print("Total Amount to be paid : Rs. ",(int(r[2])+int(r[3])+5000))
            except:
                print("Error:Could not calculate amount")

                
            if LB[7]=="BUSINESS CLASS":
                with open("Business.dat","rb+") as k:
                    t=pickle.load(k)
                    w=[LP[8],LP[9]]
                    if w not in t:
                        t.append(w)
                        print("Your seat:","B1")
                        k.seek(0)
                        pickle.dump(t,k)
                    else:
                        seat_fun_buss()
                        
            elif LB[7]=="FIRST CLASS":
                with open("First.dat","rb+") as k:
                    t=pickle.load(k)
                    w=[LP[8],LP[9]]
                    if w not in t:
                        t.append(w)
                        print("Your seat:","F1")
                        k.seek(0)
                        pickle.dump(t,k)
                    else:
                        seat_fun_first()
                    
            elif LB[7]=="ECONOMY CLASS":
                with open("Economy.dat","rb+") as k:
                    t=pickle.load(k)
                    w=[LP[8],LP[9]]
                    if w not in t:
                        t.append(w)
                        print("Your seat:","E1")
                        k.seek(0)
                        pickle.dump(t,k)
                    else:
                        seat_fun_eco()                
                   
            print("\nPayment successful\n")
            
            view_ticket()


        def seat_fun_buss():
            try:
                Buss=["B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13","B14","B15","B16","B17","B18","B19","B20","B21","B22","B23","B24","B25"]
                seat=random.randint(0,23)   
                x=Buss[seat]
                with open("Buss_seat.dat","rb+") as k:
                    t=pickle.load(k)
                    if x in t:
                        seat_fun_buss()
                    else:
                        print("Your seat:",x)
            except:
                print("All seats are booked")

            try:
                 with open("Buss_seat.dat","rb+") as k:
                     t=pickle.load(k)
                     t.append(x)                                              
                     k.seek(0)
                     pickle.dump(t,k)
            except:
                print("Could not update seats")

        def seat_fun_first():
            try:
                First=["F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","F13","F14","F15","F16","F17","F18","F19","F20","F21","F22","F23","F24","F25"]
                seat=random.randint(0,23)   
                x=First[seat]
                with open("First_seat.dat","rb+") as k:
                    t=pickle.load(k)
                    if x in t:
                        seat_fun_first()
                    else:
                        print("Your seat:",x)
            except:
                print("All seats are booked")

            try:
                 with open("First_seat.dat","rb+") as k:
                     t=pickle.load(k)
                     t.append(x)                                              
                     k.seek(0)
                     pickle.dump(t,k)
            except:
                print("Could not update seats")

        def seat_fun_eco():
            try:
                Eco=["E2","E3","E4","E5","E6","E7","E8","E9","E10","E11","E12","E13","E14","E15","E16","E17","E18","E19","E20","E21","E22","E23","E24","E25"]
                seat=random.randint(0,23)   
                x=Eco[seat]
                with open("Eco_seat.dat","rb+") as k:
                    t=pickle.load(k)
                    if x in t:
                        seat_fun_Eco()
                    else:
                        print("Your seat:",x)
            except:
                print("All seats are booked")

            try:
                 with open("Eco_seat.dat","rb+") as k:
                     t=pickle.load(k)
                     t.append(x)                                              
                     k.seek(0)
                     pickle.dump(t,k)
            except:
                print("Could not update seats")
        
        F1=Frame(screen3,width=100)
        F1.grid(row=0,column=30,padx=2,pady=2,ipadx=2,ipady=2)      #Creating Frames
        F3=Frame(screen3,width=100)
        F3.grid(row=2,column=30)
        F2=Frame(screen3,width=100,bg="White")
        F2.grid(row=1,column=30,padx=10,pady=10,ipadx=10,ipady=10)

        heading=Label(F1,text="PAYMENT",padx=2,pady=2,font="Arial 28 underline bold italic",fg="Black",bg="White",width='25',height="2") 
        heading.pack()

        name=Label(F2,text="ID: ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=0,column=0,padx=1,pady=1)              #Creation and Placement of Labels
        admin=Label(F2,text="ADMIN",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=1,column=0,padx=1,pady=1)
        card_no=Label(F2,text="CARD NO:",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=2,column=0,padx=1,pady=1)   
        card_type=Label(F2,text="SELECT PAYMENT METHOD:",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=0,column=3,padx=1,pady=1)
        cvv=Label(F2,text="ENTER CVV:",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=1,column=3,padx=1,pady=1)
        exp_d=Label(F2,text="EXPIRY DATE:",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=2,column=3,padx=1,pady=1)
        exp_y=Label(F2,text="EXPIRY YEAR:",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=3,column=3,padx=1,pady=1)
            
        idd=IntVar()
        card_type=StringVar()
        clicked=StringVar()
        card_no=IntVar()
        admin=IntVar()          #Assiging variables
        cvv=IntVar()
        exp_d=StringVar()
        exp_y=StringVar()
        
        idd_entry=Entry(F2,textvariable=idd,width="30")
        card_type_drop_entry=OptionMenu(F2,clicked,"CREDIT CARD","DEBIT CARD","MASTER CARD")        #Creation of Entries
        card_no_entry=Entry(F2,textvariable=card_no,width="30")
        admin_entry=Entry(F2,textvariable=admin,width="30")
        cvv_entry=Entry(F2,textvariable=cvv,width="30")
        exp_d_entry=Entry(F2,textvariable=exp_d,width="30")
        exp_y_entry=Entry(F2,textvariable=exp_y,width="30")

        idd_entry.grid(row=0,column=1,padx=10,pady=10)
        admin_entry.grid(row=1,column=1,padx=10,pady=10)
        card_no_entry.grid(row=2,column=1,padx=10,pady=10)
        card_type_drop_entry.grid(row=0,column=4,padx=10,pady=10)   #Placing Entries
        cvv_entry.grid(row=1,column=4,padx=10,pady=10)
        exp_d_entry.grid(row=2,column=4,padx=10,pady=10)
        exp_y_entry.grid(row=3,column=4,padx=10,pady=10)
        
        submit=Button(F3,text="SUBMIT",width="30",height="3",command=saved_info,bg="ORANGE").grid(row=0,column=1)

        next_button=Button(F3,text="NEXT",width="30",height="3",command=view_ticket,bg="ORANGE").grid(row=0,column=2)
        
        prev_button=Button(F3,text="PREVIOUS",width="30",height="3",command=booking,bg="ORANGE").grid(row=0,column=0)

        screen3.mainloop()

    def view_ticket():

        def file_details():
            
            screen100= Tk()
            F100=Frame(screen100)
            F100.pack()
            name_info=name.get()
            try:
                with open("Gemago.dat", "br") as f:
                    rec=pickle.load(f)
                    LV=[]
                    for i in rec:
                        if i[0]==name_info:
                            LV=i[0:10]
            
                #Table
                Table=PrettyTable()
                Table.field_names=["ID","First Name ","Last Name","Age","Gender ","Passport ID","Date","Class Type","From","To"]
                Table.add_row([LV[0],LV[1],LV[2],LV[3],LV[4],LV[5],LV[6],LV[7],LV[8],LV[9]])
                print(Table)
                Label(F100,text=Table,font="Arial 15 bold",bg="white",fg="black").pack()
            except:
                print("Could not find specific file")

            name2_entry.delete(0,END)
                
            screen100.mainloop()
        
        screen4=Toplevel(screen1)
        screen4.geometry("1366x768")
        screen4.title("View Ticket")
        
        C = Canvas(screen4, bg="black", height=250, width=300)
        filename = PhotoImage(file = "D:/Python/kerala.png")
        background_label = Label(screen4, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.grid()
        
        F1=Frame(screen4,width=100,bg="White")
        F1.grid(row=0,column=30,padx=2,pady=2,ipadx=2,ipady=2)      #Creating Frames
        F3=Frame(screen4,width=100)
        F3.grid(row=2,column=30)
        F2=Frame(screen4,width=100,bg="White")
        F2.grid(row=1,column=30,padx=10,pady=10,ipadx=10,ipady=10)
        
        heading=Label(F1,text="VIEW YOUR TICKETS",padx=2,pady=2,font="Arial 28 underline bold italic",fg="Black",bg="White",width='25',height="2") 
        heading.pack()

        name=IntVar()
        
        name1=Label(F2,text="ID: ",anchor="w",padx=2,pady=2,font="times 17 bold ",fg="Black",bg="White").grid(row=0,column=0,padx=15,pady=15) #Creation and Placement of Label

        
        name2_entry=Entry(F2,textvariable=name,width="30")  #Creation and Placement of Entry
        name2_entry.grid(row=0,column=1,padx=15,pady=15)
        
        name_info=name.get()
        
        submit=Button(F3,text="SUBMIT",width="30",height="3",command=file_details,bg="ORANGE").grid(row=0,column=1)

        next_button=Button(F3,text="NEXT",width="30",height="3",command=cancellation,bg="ORANGE").grid(row=0,column=2)
        
        prev_button=Button(F3,text="PREVIOUS",width="30",height="3",command=payment,bg="ORANGE").grid(row=0,column=0)

        screen4.mainloop()

    def baggage():
        
        screen5=Toplevel(screen1)
        screen5.geometry("1366x768")
        screen5.title("Baggage rules")

        img = ImageTk.PhotoImage(Image.open("fincollage.png"))
        panel1 = Label(screen5,image = img)
        panel1.pack( fill = "both", expand = "yes")

        proceed=Button(panel1,text="PROCEED",width="30",height="2",command=booking,bg="YELLOW").place(x=575,y=350)

        screen5.mainloop()
        
    def cancellation():
        screen6=Toplevel(screen1)
        screen6.geometry("1366x768")
        screen6.title("Cancellation")

        C = Canvas(screen6, bg="black", height=250, width=300)
        filename = PhotoImage(file = "D:/Python/tokyo.png")
        background_label = Label(screen6, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.grid()
        
        def confirm():
            tkinter.messagebox.showinfo("Confirmation","Confirm please")
            answer=tkinter.messagebox.askquestion("Confirmation?","Are you sure you want to proceed?")
            if answer=="yes":
                ticket()

        def ticket():
            try:
                name_info=name.get()
                with open("Gemago.dat", "br") as f:
                    rec=pickle.load(f)
                    for i in rec:
                        if i[0]==name_info:
                            a=rec.index(i)
                    del rec[a]                                                          #Deletion of a particular User
                with open("Gemago.dat", "wb") as f:
                    pickle.dump(rec,f)
                print("Ticket successfully cancelled")
            except:
                print("Could not delete specified file")
                
            try:
                db=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="gemago")
                c2=db.cursor()
                c2.execute("delete from ticket where ID='{}'".format(name_info))   #Deletion of a particular User from the database
                db.commit()
                db.close()
            except:
                print("Could not delete from database")
                
                name2_entry.delete(0,END)

        F1=Frame(screen6,width=100,bg="White")
        F1.grid(row=0,column=30,padx=2,pady=2,ipadx=2,ipady=2)      #Creation of Frames
        F3=Frame(screen6,width=100) 
        F3.grid(row=2,column=30)
        F2=Frame(screen6,width=100,bg="White")
        F2.grid(row=1,column=30,padx=10,pady=10,ipadx=10,ipady=10)

        name=IntVar()
        
        name1=Label(F2,text="ID: ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=0,column=0,padx=15,pady=15)
        name2_entry=Entry(F2,textvariable=name,width="30")
        name2_entry.grid(row=0,column=1,padx=15,pady=15)        #Creation and Placement of Labels and Entries
        name_info=name.get()

        heading=Label(F1,text="TICKET CANCELLATION",font="Arial 28 bold",fg="black",bg="White").pack()
        
        submit=Button(F3,text="SUBMIT",width="30",height="3",command=confirm,bg="ORANGE").grid(row=0,column=1)

        next_button=Button(F3,text="NEXT",width="30",height="3",command=updation,bg="ORANGE").grid(row=0,column=2)
        
        prev_button=Button(F3,text="PREVIOUS",width="30",height="3",command=view_ticket,bg="ORANGE").grid(row=0,column=0)

        screen6.mainloop()

    def updation():
        
        screen7=Toplevel(screen1)
        screen7.geometry("1366x768")
        screen7.title("Updation")

        C = Canvas(screen7, bg="black", height=250, width=300)
        filename = PhotoImage(file = "D:/Python/germany.png")
        background_label = Label(screen7, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.grid()

        def save_info():
            name_info=idd1.get()
            firstname_info=firstname.get()
            lastname_info=lastname.get()
            age_info=age.get()
            gender_info=gender.get()
            Passport_id_info=Passport_id.get()
            date_info=date.get()
            
            try:
                with open("Gemago.dat","rb+") as k:
                    rec=pickle.load(k)
                    for i in rec:                            
                        if i[0]==name_info:
                            LN=[firstname_info,lastname_info,age_info,gender_info,Passport_id_info,date_info]     #Updation of a particular User
                            i[1:7]=LN[0:7]
                            print("\nID:",name_info,"\nFirst Name:",firstname_info,"\nLast Name:",lastname_info,"\nAge:",age_info,"\nGender:",gender_info,"\nPassport ID:",Passport_id_info,"\nDate:",date_info)
                            print("\nSuccessfully updated\n")
                            break
                    else:
                        print("Not found")
            except:
                print("Could not update the file")
                
            try:
                with open("Gemago.dat","wb") as k:
                    pickle.dump(rec,k)
            except:
                print("Could not update")
                
            try:            
                db=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="gemago")
                mycursor=db.cursor()
                q="update ticket set Firstname='{}',Lastname='{}',Age={},Gender='{}',PassportID='{}',DateOf='{}' where ID={}".format(firstname_info,lastname_info,age_info,gender_info,Passport_id_info,date_info,name_info)
                mycursor.execute(q)
                db.commit()                                 #Updation of a particular User in the database
                db.close()
            except:
                print("Could not update database")
                
            idd_entry.delete(0,END)   
            firstname_entry.delete(0,END)
            lastname_entry.delete(0,END)
            age_entry.delete(0,END) 
            Passport_id_entry.delete(0,END)
            date_entry.delete(0,END)

          
        F1=Frame(screen7,width=100,bg="White")
        F1.grid(row=0,column=30,padx=2,pady=2,ipadx=2,ipady=2)
        F3=Frame(screen7,width=100,bg="White")
        F3.grid(row=2,column=30)
        F2=Frame(screen7,width=100,bg="White")
        F2.grid(row=1,column=30,padx=10,pady=10,ipadx=10,ipady=10)
        
        heading=Label(F1,text="UPDATE YOUR TICKETS",padx=2,pady=2,font="Arial 28 underline bold italic",fg="Black",bg="White",width='25',height="2") 
        heading.pack()
        
        idd=Label(F2,text="ID  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=0,column=3,padx=15,pady=15)
        firstname=Label(F2,text="FIRSTNAME  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=0,column=0,padx=15,pady=15)    #Creation and Placement of Labels
        lastname=Label(F2,text="LASTNAME ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=1,column=0,padx=15,pady=15)
        age=Label(F2,text="AGE  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=2,column=0,padx=15,pady=15)
        gender=Label(F2,text="GENDER  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=1,column=3,padx=15,pady=15)
        Passport_id=Label(F2,text="PASSPORT ID ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=4,column=0,padx=15,pady=15)
        date=Label(F2,text="DATE OF DEPARTURE  ",anchor="w",padx=2,pady=2,font="times 13 bold ",fg="Black",bg="White").grid(row=5,column=0,padx=15,pady=15)

        idd1=IntVar()       
        firstname=StringVar()
        lastname=StringVar()        #Assigning Variables
        age=IntVar()
        gender=StringVar()
        Passport_id=StringVar()
        date=StringVar()

        idd_entry=Entry(F2,textvariable=idd1,width="30")
        firstname_entry=Entry(F2,textvariable=firstname,width="30")
        lastname_entry=Entry(F2,textvariable=lastname,width="30")
        age_entry=Entry(F2,textvariable=age,width="30")
        gender_entry=OptionMenu(F2,gender,"M","F","Others")
        Passport_id_entry=Entry(F2,textvariable=Passport_id,width="30")
        date_entry=Entry(F2,textvariable=date,width="30")
                                                                                                                                                                #Creation and Placement of Entries
        idd_entry.grid(row=0,column=4,padx=10,pady=10)
        firstname_entry.grid(row=0,column=1,padx=10,pady=10)
        lastname_entry.grid(row=1,column=1,padx=10,pady=10)
        age_entry.grid(row=2,column=1,padx=10,pady=10)
        gender_entry.grid(row=1,column=4,padx=10,pady=10)
        Passport_id_entry.grid(row=4,column=1,padx=10,pady=10)
        date_entry.grid(row=5,column=1,padx=10,pady=10)

        
        submit=Button(F3,text="SUBMIT",width="30",height="3",command=save_info,bg="ORANGE").grid(row=0,column=1)
        
        screen7.mainloop()

    def main_page():
        
        global screen1
        screen1=Toplevel(front)
        
        C = Canvas(screen1, bg="black", height=250, width=300)
        filename = PhotoImage(file = "D://Python//aeroplane.png")
        background_label = Label(screen1, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.grid()
        
        screen1.geometry("1366x768")
        screen1.title("MAIN PAGE")

        F1=Frame(screen1,width=100)
        F1.grid(row=0,column=30,padx=2,pady=2,ipadx=2,ipady=2)      #Creating Frames
        F2=Frame(screen1,width=100)
        F2.grid(row=1,column=30)
        
        heading=Label(F1,text="WELCOME TO GEMAGO",padx=2,pady=2,font="Arial 30 underline bold italic",fg="Black",bg="White",width='25',height="2") 
        heading.pack()

        baggage_button=Button(F2,text="BAGGAGE INFORMATION",width="30",height="3",command=baggage,bg="cyan",fg="black").grid(row=0,column=0,sticky=W)
        book_button=Button(F2,text="BOOK YOUR TICKETS",width="30",height="3",command=booking,bg="yellow",fg="black").grid(row=1,column=0,sticky=W)                  #Creation and Placement of Buttons
        payment_button=Button(F2,text="PAYMENT",width="30",height="3",command=payment,bg="green2",fg='black').grid(row=2,column=0,sticky=W)
        View_button=Button(F2,text="VIEW YOUR TICKETS",width="30",height="3",command=view_ticket,bg="deep sky blue",fg='black').grid(row=3,column=0,sticky=W)
        Delete_button=Button(F2,text="CANCELLATION",width="30",height="3",command=cancellation,bg="coral",fg='black').grid(row=4,column=0,sticky=W)
        flightinfo_button=Button(F2,text="UPDATION",width="30",height="3",command=updation,bg="orange",fg='black').grid(row=5,column=0,sticky=W)

        screen1.mainloop()
        
    main_page()
    
def front():
    global front
    front=Tk()
    front.geometry("1366x768")
    front.title("Welcome")

    img = ImageTk.PhotoImage(Image.open("FrontPage.jpg"))
    panel1 = Label(front,image = img)
    panel1.pack( fill = "both", expand = "yes")

    proceed=Button(panel1,text="PROCEED",width="30",height="2",command=project,bg="YELLOW").place(x=575,y=550)

    front.mainloop()    
       
try:
              
    #Creation of database and SQL Table
    
    db=mysql.connector.connect(host="localhost",user="root",passwd="tiger")
    c1=db.cursor()
    q="create database gemago"
    c1.execute(q)
    db.close()

    db=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="gemago")
    mycursor=db.cursor()
    q="create table ticket (ID int,Firstname varchar(50),Lastname varchar(50),Age int,Gender varchar(10),Departure varchar(50),Arrival varchar(50),PassportID int,DateOf varchar(50),Coach varchar(50))"
    mycursor.execute(q)
    db.close()

    fname=['Departure City','Arrival City','Passenger(Above 18)','Passenger(Below 18)']
    rows=[['Cochin','Dubai',25000,20000],['Dubai','Cochin',25000,22000],['Cochin','Tokyo',48000,42000],['Tokyo','Cochin',50000,45000],['Cochin','Newyork',105200,98000],['Newyork','Cochin',103900,96000],['Cochin','London',55000,45000],['London','Cochin',58000,45000],['Dubai','Tokyo',56000,51000],['Tokyo','Dubai',57800,48200],['Dubai','Newyork',82000,75000],['Newyork','Dubai',84600,76500],['Dubai','London',40000,34000],['London','Dubai',42000,36000],['Tokyo','Newyork',55000,49900],['Newyork','Tokyo',54750,48678],['Tokyo','London',93000,87800],['London','Tokyo',95000,88200],['Newyork','London',82752,76987],['London','Newyork',84986,75896]]

    with open("GEMAGOfares.csv","w",newline='') as f:
        wobj=csv.writer(f,delimiter=',')
        wobj.writerow(fname)
        for r in rows:
            wobj.writerow(r)
    f.close()


    #Creation of Binary files
    
    with open("Gemago.dat","wb") as k:
        L=[]
        pickle.dump(L,k)
        
    with open("IDcodes.dat","wb") as f:
        L=[]
        pickle.dump(L,f)
    
    with open("Buss_seat.dat","wb") as f:
        L=[]
        pickle.dump(L,f)
 
    with open("Business.dat","wb") as f:
        L=[]
        pickle.dump(L,f)
    with open("First_seat.dat","wb") as f:
        L=[]
        pickle.dump(L,f)
 
    with open("First.dat","wb") as f:
        L=[]
        pickle.dump(L,f)
    with open("Eco_seat.dat","wb") as f:
        L=[]
        pickle.dump(L,f)
 
    with open("Economy.dat","wb") as f:
        L=[]
        pickle.dump(L,f)
    
    front()
except:
    front()



