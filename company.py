from tkinter import*
from tkinter import ttk
import home
from tkinter import messagebox
from tkinter.ttk import Treeview
import mysql.connector
try:
    mydb1=mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='',
                database='gg'
    )
    mycursor=mydb1.cursor()


except mysql.connector.Error as error:
    messagebox.showinfo("Information", "No Server Connection")
    exit(0)


class product:

        def __init__(self, root):
            self.root = root
            self.root.title("WAREHOUSE MANAGEMENT SYSTEM")
            self.root.geometry("1000x700+0+0")
            self.root.resizable(False, False)
            self.root.config(bg="alice blue")

            MainFrame=Frame(self.root,bg="black")
            MainFrame.grid()
            self.title=Label(MainFrame,font=("Goudy old style",50,"bold"),fg="black",
                              text="      JUSAN WAREHOUSE  ",bg="alice blue")

            self.title.grid()
            #frame
            DataEntryFrame=Frame(self.root,bg="alice blue",relief=GROOVE,borderwidth=0)
            DataEntryFrame.place(x=10,y=80,width=500,height=600,)

            #label and data entry for company detail
            self.Title=Label( DataEntryFrame,font=("Goudy old style",25,"bold"),fg="black",text="        COMPANY DETAIL",
                              bg="alice blue")
            self.Title.grid()

            #label and data entry for company name
            self.uname = StringVar()
            self.ucont=StringVar()
            self.uemail=StringVar()
            self.ulocation = StringVar()
            self.lblcompanyname = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="COMPANY NAME:"
                                 , fg="black", bg="alice blue").place(x=10, y=80)
            self.txt_companyname = Entry(DataEntryFrame,textvariable=self.uname,font=("Goudy old style", 15), bg="white",)
            self.txt_companyname.place(x=200, y=80, width=250, height=35)

            #label and data entry for contact no
            self.lblcontactno= Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="CONTACT NO:"
                                        , fg="black", bg="alice blue").place(x=10, y=140)
            self.txt_contactno = Entry(DataEntryFrame,textvariable=self.ucont, font=("Goudy old style", 15), bg="white")
            self.txt_contactno.place(x=200, y=140, width=250, height=35)

            #label and data entry for email address
            self.lblemailaddress= Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="EMAIL ADDRESS:"
                                      , fg="black", bg="alice blue").place(x=10, y=190)
            self.txt_emailaddress = Entry(DataEntryFrame,textvariable=self.uemail, font=("Goudy old style", 15), bg="white")
            self.txt_emailaddress.place(x=200, y=190, width=250, height=35)

            #label and data entry for location
            self.lbllocation = Label(DataEntryFrame,font=('Bahnschrift', 15, "bold"), text="LOCATION:"
                                         , fg="black", bg="alice blue").place(x=10, y=240)
            self.txt_location = Entry(DataEntryFrame, textvariable=self.ulocation, font=("Goudy old style", 15), bg="white")
            self.txt_location.place(x=200, y=240, width=250, height=35)

            #button
            self.b2 = Button(self.root,text="ADD", font=('bahnschrift', 15, 'bold'),bg="white",width=10 ,command=self.addCompany)
            self.b1 = Button(self.root,text="UPDATE", font=('bahnschrift', 15, 'bold'), bg="white",width=10,command=self.updateCompany)
            self.b3 = Button(self.root,text="DELETE", font=('bahnschrift', 15, 'bold'),bg="white",width=10 ,command=self.deleteCompany)
            self.b4 = Button(self.root,text="CLEAR", font=('bahnschrift', 15, 'bold'),bg="white",width=10,command=self.clearCompany)
            self.b2.place(x=50, y=430)
            self.b1.place(x=300,y=430)
            self.b3.place(x=50,y=520)
            self.b4.place(x=300,y=520)

            self.b5 = Button(self.root, text="HOME", font=('bahnschrift', 15, 'bold'),bg="white", width=10,
                             command=self.addhome)
            self.b5.place(x=150, y=620)

            #self.button_quit = Button(self.root, text="QUIT", command=root.quit, font=('bahnschrift', 15, 'bold'),bg="white",
                                      #width=10)
            #self.button_quit.place(x=150, y=620)


            ShowdataFrame= Frame(self.root, bg="alice blue", relief=GROOVE, borderwidth=5)
            ShowdataFrame.place(x=500, y=80, width=500, height=600)
            scroll_x = Scrollbar(ShowdataFrame, orient=HORIZONTAL)
            scroll_y = Scrollbar(ShowdataFrame, orient=VERTICAL)
            self.San_table = ttk.Treeview(ShowdataFrame, column=("Company name", "contact no", "email address", "location"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.San_table.xview)
            scroll_y.config(command=self.San_table.yview)
            self.San_table.heading("Company name", text="Company name")
            self.San_table.heading("contact no", text="contact no")
            self.San_table.heading("email address", text="email address")
            self.San_table.heading("location", text="location")

            self.San_table.heading("location", text="location")

            self.San_table['show'] = "headings"
            self.San_table.pack(fill=BOTH, expand=1)
            self.San_table.pack()
            mycursor.execute("select * from company")
            row=mycursor.fetchall()
            self.update(row)
            self.San_table.bind('<Double 1>', self.hello)

        def update(self,row):
            self.San_table.delete(*self.San_table.get_children())
            for i in row:
                self.San_table.insert("","end",values=i)

        def clear(self):
            mycursor.execute("select * from company")
            row = mycursor.fetchall()
            self.update(row)

        def hello(self,event):
            rowid=self.San_table.identify_row(event.y)
            item=self.San_table.item(self.San_table.focus())
            self.uname.set(item["values"][0])
            self.ucont.set(item["values"][1])
            self.uemail.set(item["values"][2])
            self.ulocation.set(item["values"][3])
        def addCompany(self):
            name=self.uname.get()
            contact=self.ucont.get()
            email=self.uemail.get()
            location=self.ulocation.get()

            #mycursor.execute("create table if not exists company(name varchar(100) ,contact int(100),email varchar(100),location varchar(100)")
            sql = "INSERT INTO company (name,contact,email,location) VALUES (%s, %s,%s,%s)"
            val=(name,contact,email,location,)
            mycursor.execute(sql,val)
            mydb1.commit()
            self.clear()


        def clearCompany(self):
            self.uname.set("")
            self.ucont.set("")
            self.uemail.set("")
            self.ulocation.set("")
            
        def deleteCompany(self):
            customer_name= self.uname.get()
            if messagebox.askyesno("Confirm Delete","Are you Sure you want to delete this company?"):
                query="DELETE FROM company where name=%s"
                valu=(customer_name,)
                mycursor.execute(query,valu)
                mydb1.commit()
                self.clear()
            else :
                return True

        def updateCompany(self):
            name = self.uname.get()
            contact = self.ucont.get()
            email = self.uemail.get()
            location = self.ulocation.get()
            if messagebox.askyesno("Confirm Update", "Are you Sure you want to update this company?"):
                query = "UPDATE company set contact=%s, email=%s ,location=%s  WHERE name=%s"
                valu = (contact,email,location,name,)
                mycursor.execute(query, valu)
                mydb1.commit()
                self.clear()
            else:
                return True
        def addhome(self):
            self.reg = Toplevel(self.root)
            home.product(self.reg)



if __name__ =='__main__':
    root=Tk()
    application=product (root)
    root.mainloop()

