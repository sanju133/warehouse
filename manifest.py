from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview
import home
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
            self.root.config(bg="lavender")

           #main frame
            MainFrame=Frame(self.root,bg="black")
            MainFrame.grid()
            self.title=Label(MainFrame,font=("bahnschrift",50,"bold"),fg="black",
                              text="                             JUSAN WAREHOUSE  ",bg="lavender")
            self.title.grid()
            #dframe
            DataEntryFrame = Frame(self.root, bg="lavender", relief=GROOVE, borderwidth=1)
            DataEntryFrame.place(x=10, y=5, width=450, height=700, )
            self.Title = Label(DataEntryFrame, font=("Goudy old style", 25, "bold"), fg="black",
                               text="        Enter items",
                               bg=("lavender"))
            self.Title.grid()

            self.uname=StringVar()
            self.umanufacture=StringVar()
            self.ucategory=StringVar()
            self.uquantity=StringVar()
            self.uprice=StringVar()
            self.ucolor=StringVar()
            self.uweight=StringVar()
            self.udate=StringVar()
            self.ustatus=StringVar()



            #label and data entry entry
            self.item_name = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="ITEM NAME:"
                                        , fg="black", bg="lavender").place(x=10, y=80)
            self.txt_itemname = Entry(DataEntryFrame,textvariable=self.uname, font=("Goudy old style", 15), bg="white")
            self.txt_itemname.place(x=200, y=80, width=200, height=25)

            #label and data entry for manufacture
            self.lblmanufacture = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="MANUFACTURE:"
                                      , fg="black", bg="lavender").place(x=10, y=120)
            self.txt_manufacture = Entry(DataEntryFrame,textvariable=self.umanufacture, font=("Goudy old style", 15), bg="white")
            self.txt_manufacture.place(x=200, y=120, width=200, height=25)

            #label and data entry for item category
            self.lblitemcategory = Label(DataEntryFrame,font=('Bahnschrift', 15, "bold"), text="ITEM CATEGORY:"
                                         , fg="black", bg="lavender").place(x=10, y=160)
            self.cboitemcategory=ttk.Combobox(DataEntryFrame,textvariable=self.ucategory,font=('goudy old style',15),state='readonly,width=50')
            self.cboitemcategory['value']=('',"food","Vechicle","makeup","clothes","things")
            self.cboitemcategory.place(x=200,y=160,width=200,height=25)

            #label  and data entry for quantity
            self.lblquantity = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="QUANTITY:"
                                        , fg="black", bg="lavender").place(x=10, y=200)
            self.txt_quantity = Entry(DataEntryFrame, textvariable=self.uquantity,font=("Goudy old style", 15), bg="white")
            self.txt_quantity.place(x=200, y=200, width=200, height=25)

            #label and data entry for price
            self.lblprice = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="PRICE(rps):"
                                     , fg="black", bg="lavender").place(x=10, y=240)
            self.txt_price = Entry(DataEntryFrame,textvariable=self.uprice, font=("Goudy old style", 15), bg="white")
            self.txt_price.place(x=200, y=240, width=200, height=25)

            # label and data entry for color
            self.lblcolor = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="COLOR:"
                                  , fg="black", bg="lavender").place(x=10, y=280)
            self.txt_color = Entry(DataEntryFrame,textvariable=self.ucolor, font=("Goudy old style", 15), bg="white")
            self.txt_color.place(x=200, y=280, width=200, height=25)

             # label and data entry for weight
            self.lblweight = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="WEIGHT(kgs):"
                                  , fg="black", bg="lavender").place(x=10, y=320)
            self.txt_weight = Entry(DataEntryFrame, textvariable=self.uweight,font=("Goudy old style", 15), bg="white")
            self.txt_weight.place(x=200, y=320, width=200, height=25)

            #label and data entry for date
            self.lblEnterDate= Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="ENTER DATE:"
                                  , fg="black", bg="lavender").place(x=10, y=360)
            self.txt_EnterDate= Entry(DataEntryFrame, textvariable=self.udate ,font=("Goudy old style", 15), bg="white")
            self.txt_EnterDate.place(x=200, y=360, width=200, height=25)

             #label  and data entry for recieve
            self.lblreceive = Label(DataEntryFrame, font=('Bahnschrift', 15, "bold"), text="RECIEVE:"
                                         , fg="black", bg="lavender").place(x=10, y=400)
            self.cboreceive = ttk.Combobox(DataEntryFrame,textvariable=self.ustatus, font=("goudy old style", 15),
                                                state='readonly,width=50')
            self.cboreceive['value'] = ('', "recieve","not recieve")
            self.cboreceive.place(x=200, y=400, width=200, height=25)

            #button for add, delete , update , clear, back
            self.b1 = Button(self.root,text="ADD", font=('bahnschrift', 15, 'bold'),width=10,command=self.addmanifest1)
            self.b1.place(x=50, y=500)
            self.b2 = Button(self.root,text="DELETE", font=('bahnschrift', 15, 'bold'),width=10,command=self.deletemanifest1)
            self.b2.place(x=50, y=570)

            self.b3= Button(self.root,text="UPDATE", font=('bahnschrift', 15, 'bold'),width=10,command=self.updatemanifest1)
            self.b3.place(x=250, y=500)
            self.b4 = Button(self.root,text="CLEAR", font=('bahnschrift', 15, 'bold'),width=10,command=self.clearmanifest1)
            self.b4.place(x=250, y=570)
            self.b4 = Button(self.root, text="CLEAR", font=('bahnschrift', 15, 'bold'), width=10,
                             command=self.clearmanifest1)
            self.b4.place(x=250, y=570)
            self.b5= Button(self.root, text="HOME", font=('bahnschrift', 15, 'bold'), width=10,
                             command=self.addhome)
            self.b5.place(x=160, y=640)


            #data drame
            ShowdataFrame = Frame(self.root, bg="lavender", relief=GROOVE, borderwidth=1)
            ShowdataFrame.place(x=500, y=80, width=780, height=600)
            scroll_x = Scrollbar(ShowdataFrame, orient=HORIZONTAL)
            scroll_y = Scrollbar(ShowdataFrame, orient=VERTICAL)
            self.Student_table =ttk.Treeview(ShowdataFrame, column=("item name", "manufacture", "item category", "quantity", "price","color", "weight", "enter date", "status")
                                       , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Student_table.xview)
            scroll_y.config(command=self.Student_table.yview)
            self.Student_table.heading("item name",text="item name")
            self.Student_table.heading("manufacture", text="manufacture")
            self.Student_table.heading("item category", text="item category")
            self.Student_table.heading("quantity", text="quantity")
            self.Student_table.heading("price", text="price")
            self.Student_table.heading("color",text="color")
            self.Student_table.heading("weight", text="weight")
            self.Student_table.heading("enter date", text="enter date")
            self.Student_table.heading("status", text="status")
            self.Student_table['show']="headings"
            self.Student_table.pack(fill=BOTH,expand=1)
            self.Student_table.pack()
            mycursor.execute("select * from manifest1")
            row = mycursor.fetchall()
            self.updat(row)
            self.Student_table.bind('<Double 1>', self.san)


        def updat(self, row):
            self.Student_table.delete(*self.Student_table.get_children())
            for i in row:
                self.Student_table.insert("", "end", values=i)

        def clear(self):
            mycursor.execute("select * from manifest1")
            row = mycursor.fetchall()
            self.updat(row)

        def san(self, event):
            rowid = self.Student_table.identify_row(event.y)
            item = self.Student_table.item(self.Student_table.focus())
            self.uname.set(item["values"][0])
            self.umanufacture.set(item["values"][1])
            self.ucategory.set(item["values"][2])
            self.uquantity.set(item["values"][3])
            self.uprice.set(item["values"][4])
            self.ucolor.set(item["values"][5])
            self.uweight.set(item["values"][6])
            self.udate.set(item["values"][7])
            self.ustatus.set(item["values"][8])

        def addmanifest1(self):
            name=self.uname.get()
            manufacture=self.umanufacture.get()
            category=self.ucategory.get()
            quantity=self.uquantity.get()
            price=self.uprice.get()
            color=self.ucolor.get()
            weight=self.uweight.get()
            date=self.udate.get()
            status=self.ustatus.get()
            sql ="INSERT INTO manifest1 (name, manufacture, category, quantity, price, color, weight, date, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (name,manufacture,category,quantity, price, color, weight,date,status)
            mycursor.execute(sql, val)
            mydb1.commit()
            self.clear()

        def clearmanifest1(self):
            name = self.uname.set("")
            manufacture = self.umanufacture.set("")
            category = self.ucategory.set("")
            quantity = self.uquantity.set("")
            price = self.uprice.set("")
            color = self.ucolor.set("")
            weight = self.uweight.set("")
            date = self.udate.set("")
            status = self.ustatus.set("")
        def deletemanifest1(self):
            customer_name=self.uname.get()
            if messagebox.askyesno("Confirm Delete","Are you sure you want to delete this manifest"):
                query="Delete from manifest1 where name=%s"
                valu=(customer_name,)
                mycursor.execute(query,valu)
                mydb1.commit()
                self.clear()
            else:
                return True

        def updatemanifest1(self):
            name = self.uname.get()
            manufacture = self.umanufacture.get()
            category = self.ucategory.get()
            quantity = self.uquantity.get()
            price = self.uprice.get()
            color = self.ucolor.get()
            weight = self.uweight.get()
            date = self.udate.get()
            status = self.ustatus.get()
            if messagebox.askyesno("Confirm Update", "Are you Sure you want to update this manifest?"):
                query = "UPDATE manifest1 set manufacture=%s, category=%s ,quantity=%s ,price=%s , color=%s, weight=%s, date=%s, status=%s WHERE name=%s"
                valu = ( manufacture, category, quantity,price,color,weight,date,status,name)
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