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
            self.root.geometry("1300x700+0+0")
            self.root.resizable(False, False)
            self.root.config(bg="light grey")
            #main frame and title
            MainFrame=Frame(self.root,bg="black")
            MainFrame.grid()
            self.title=Label(MainFrame,font=("bahnschrift",50,"bold"),fg="black",
                              text="                             JUSAN WAREHOUSE  ",bg="light grey")
            self.title.grid()

           #frame for customer details
            JusanEntryFrame = Frame(self.root, bg="light grey", relief=GROOVE, borderwidth=1)
            JusanEntryFrame.place(x=10, y=5, width=450, height=700, )
            self.Title = Label(JusanEntryFrame, font=("Goudy old style", 25, "bold"), fg="black",
                               text="        CUSTOMER DETAILS",
                               bg=("light grey"))
            self.Title.grid()

            self.uname=StringVar()
            self.uid = StringVar()
            self.uitem = StringVar()
            self.ulocation= StringVar()
            self.uprice = StringVar()
            self.uquantity= StringVar()
            self.udistance = StringVar()
            self.utotal = StringVar()
            self.udate = StringVar()
            self.udeliver = StringVar()






            #label  and data entry for customer id
            self.lblcustomerid = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="CUSTOMER NAME:"
                                        , fg="black", bg="light grey").place(x=10, y=80)
            self.txt_customerid = Entry(JusanEntryFrame, textvariable=self.uname, font=("Goudy old style", 15), bg="white")
            self.txt_customerid.place(x=200, y=80, width=200, height=25)

            #label and data entry for customer name
            self.lblcustomername= Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="CUSTOMER ID:"
                                      , fg="black", bg="light grey").place(x=10, y=120)
            self.txt_customername= Entry(JusanEntryFrame,textvariable=self.uid, font=("Goudy old style", 15), bg="white")
            self.txt_customername.place(x=200, y=120, width=200, height=25)

            #label and data entry for item name
            self.lblitemcategory = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="ITEMS NAME:"
                                         , fg="black", bg="light grey").place(x=10, y=160)
            self.cboitemcategory=ttk.Combobox(JusanEntryFrame,textvariable=self.uitem,font=('goudy old style',15),state='readonly,width=50')
            self.cboitemcategory['value']=('',"food","Vechicle","makeup","clothes","things")
            self.cboitemcategory.place(x=200,y=160,width=200,height=25)


            #label  and data entry for location
            self.lbllocation = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="LOCATION:"
                                        , fg="black", bg="light grey").place(x=10, y=200)
            self.txt_location= Entry(JusanEntryFrame,textvariable=self.ulocation, font=("Goudy old style", 15), bg="white")
            self.txt_location.place(x=200, y=200, width=200, height=25)

            #label and data entry for price
            self.lblprice = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="PRICE(rps):"
                                     , fg="black", bg="light grey").place(x=10, y=240)
            self.txt_price = Entry(JusanEntryFrame,textvariable=self.uprice, font=("Goudy old style", 15), bg="white")
            self.txt_price.place(x=200, y=240, width=200, height=25)

            #label and data entry entry for quantity
            self.lblquantity= Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="QUANTITY:"
                                  , fg="black", bg="light grey").place(x=10, y=280)
            self.txt_quantity = Entry(JusanEntryFrame,textvariable=self.uquantity, font=("Goudy old style", 15), bg="white")
            self.txt_quantity.place(x=200, y=280, width=200, height=25)

            #label and data entry for distance
            self.lbldistance= Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="DISTANCE:"
                                  , fg="black", bg="light grey").place(x=10, y=320)
            self.txt_distance= Entry(JusanEntryFrame,textvariable=self.udistance, font=("Goudy old style", 15), bg="white")
            self.txt_distance.place(x=200, y=320, width=200, height=25)

            #label  and data entry for total
            self.lbltotal= Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="TOTAL:"
                                  , fg="black", bg="light grey").place(x=10, y=360)
            self.txt_total= Entry(JusanEntryFrame, textvariable=self.utotal, font=("Goudy old style", 15), bg="white")
            self.txt_total.place(x=200, y=360, width=200, height=25)

            #label and data entry entry for date
            self.lblDate = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="DATE:"
                                      , fg="black", bg="light grey").place(x=10, y=400)
            self.txt_Date = Entry(JusanEntryFrame,textvariable=self.udate, font=("Goudy old style", 15), bg="white")
            self.txt_Date.place(x=200, y=400, width=200, height=25)

            #label and data entry for status
            self.lblstatus = Label(JusanEntryFrame, font=('Bahnschrift', 15, "bold"), text="STATUS:"
                                         , fg="black", bg="light grey").place(x=10, y=440)
            self.cbostatus = ttk.Combobox(JusanEntryFrame,textvariable=self.udeliver, font=('goudy old style', 15),
                                                state='readonly,width=50')
            self.cbostatus['value'] = ('', "deliever","not deliever")
            self.cbostatus.place(x=200, y=440, width=200, height=25)

            #buttons
            self.b2 = Button(self.root,text="ADD", font=('bahnschrift', 15, 'bold'),width=10,command=self.addcustomer)
            self.b2.place(x=50, y=500)
            self.b1 = Button(self.root,text="DELETE", font=('bahnschrift', 15, 'bold'),width=10,command=self.deletecustomer)
            self.b1.place(x=50, y=580)

            self.b3= Button(self.root,text="UPDATE", font=('bahnschrift', 15, 'bold'),width=10,command=self.updatecustomer)
            self.b3.place(x=300, y=500)
            self.b4= Button(self.root,text="CLEAR", font=('bahnschrift', 15, 'bold'),width=10,command=self.clearcustomer)
            self.b4.place(x=300, y=580)
            self.b5 = Button(self.root, text="HOME", font=('bahnschrift', 15, 'bold'), width=10,
                             command=self.addhome)
            self.b5.place(x=170, y=650)

            #dataframe
            samdataFrame = Frame(self.root, bg="lavender", relief=GROOVE, borderwidth=1)
            samdataFrame.place(x=500, y=80, width=780, height=600)
            scroll_x = Scrollbar(samdataFrame, orient=HORIZONTAL)
            scroll_y = Scrollbar(samdataFrame, orient=VERTICAL)
            self.San_table =ttk.Treeview(samdataFrame, column=("customer id", "customer name", "item name","location","quantity", "price","distance", "total", " date", "status")
                                       , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.San_table.xview)
            scroll_y.config(command=self.San_table.yview)
            self.San_table.heading("customer name",text="customer name")
            self.San_table.heading("customer id", text="customer id")
            self.San_table.heading("item name", text="item name")
            self.San_table.heading("location", text="location")

            self.San_table.heading("quantity", text="quantity")
            self.San_table.heading("price", text="price")
            self.San_table.heading("distance",text="distance")
            self.San_table.heading("total", text="total")
            self.San_table.heading(" date", text=" date")
            self.San_table.heading("status", text="status")
            self.San_table['show']="headings"
            self.San_table.pack(fill=BOTH,expand=1)
            self.San_table.pack()
            mycursor.execute("select * from customer")
            row = mycursor.fetchall()
            self.update(row)
            self.San_table.bind('<Double 1>', self.hello)

        def update(self, row):
            self.San_table.delete(*self.San_table.get_children())
            for i in row:
             self.San_table.insert("", "end", values=i)

        def clear(self):
            mycursor.execute("select * from customer")
            row = mycursor.fetchall()
            self.update(row)

        def hello(self, event):
            rowid = self.San_table.identify_row(event.y)
            item = self.San_table.item(self.San_table.focus())
            self.uname.set(item["values"][0])
            self.uid.set(item["values"][1])
            self.uitem.set(item["values"][2])
            self.ulocation.set(item["values"][3])
            self.uprice.set(item["values"][4])
            self.uquantity.set(item["values"][5])
            self.udistance.set(item["values"][6])
            self.utotal.set(item["values"][7])
            self.udate.set(item["values"][8])
            self.udeliver.set(item["values"][9])

        def addcustomer(self):
            name= self.uname.get()
            id = self.uid.get()
            item = self.uitem.get()
            location= self.ulocation.get()
            price = self.uprice.get()
            quantity = self.uquantity.get()
            distance= self.udistance.get()
            total= self.utotal.get()
            date= self.udate.get()
            deliver = self.udeliver.get()
            sql = "INSERT INTO customer(name, id, item,  location,price,quantity,distance,total,date, deliver) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
            val = (name, id, item,  location,price,quantity,distance,total,date, deliver)
            mycursor.execute(sql, val)
            mydb1.commit()
            self.clear()

        def clearcustomer(self):
            name = self.uname.set("")
            id = self.uid.set("")
            item= self.uitem.set("")
            location= self.ulocation.set("")
            price = self.uprice.set("")
            quantity= self.uquantity.set("")
            distance = self.udistance.set("")
            total = self.utotal.set("")
            date= self.udate.set("")
            deliver = self.udeliver.set("")


        def deletecustomer(self):
            customer_name = self.uname.get()
            if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this customer"):
                query = "Delete from customer where name=%s"
                valu = (customer_name,)
                mycursor.execute(query, valu)
                mydb1.commit()
                self.clear()
            else:
                return True

        def updatecustomer(self):
            name = self.uname.get()
            id = self.uid.get()
            item = self.uitem.get()
            location = self.ulocation.get()
            price = self.uprice.get()
            quantity = self.uquantity.get()
            distance= self.udistance.get()
            total= self.utotal.get()
            date = self.udate.get()
            deliver = self.udeliver.get()
            if messagebox.askyesno("Confirm Update", "Are you Sure you want to update this customer?"):
                query = "UPDATE customer set id=%s, item=%s ,location=%s ,price=%s , quantity=%s, distance=%s, total=%s, date=%s, deliver=%s WHERE name=%s"
                valu = (id, item, location, price, quantity, distance, total,date, deliver, name)
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
