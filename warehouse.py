from tkinter import*
from tkinter import ttk
import home
from tkinter.ttk import Treeview
from tkinter import messagebox
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
        self.root.geometry("1300x700+0+0")
        self.root.title("WAREHOUSE MANAGEMENT SYSTEM")
        self.root.resizable(False, False)
        self.root.config(bg="sky blue")
        cusdataFrame = Frame(self.root, bg="sky blue", relief=GROOVE, borderwidth=1)
        MainFrame = Frame(self.root, bg="grey")
        MainFrame.grid()
        self.title = Label(MainFrame, font=("gouldy old style", 28, "bold"), fg="black",
                           text="                       Item Delivered                                   Item Received ", bg="sky blue")
        self.title.grid()

        # for item delivered


        # dataframe
        samdataFrame = Frame(self.root, bg="lavender", relief=GROOVE, borderwidth=1)
        samdataFrame.place(x=130, y=70, width=600, height=620)
        scroll_x = Scrollbar(samdataFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(samdataFrame, orient=VERTICAL)
        self.San_table = ttk.Treeview(samdataFrame, column=(
            "customer id", "customer name", "item name", "location", "quantity", "price", "distance", "total", " date",
            "status")
                                      , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.San_table.xview)
        scroll_y.config(command=self.San_table.yview)
        self.San_table.heading("customer name", text="customer name")
        self.San_table.heading("customer id", text="customer id")
        self.San_table.heading("item name", text="item name")
        self.San_table.heading("location", text="location")

        self.San_table.heading("quantity", text="quantity")
        self.San_table.heading("price", text="price")
        self.San_table.heading("distance", text="distance")
        self.San_table.heading("total", text="total")
        self.San_table.heading(" date", text=" date")
        self.San_table.heading("status", text="status")
        self.San_table['show'] = "headings"
        self.San_table.pack(fill=BOTH, expand=1)
        self.San_table.pack()
        mycursor.execute("select * from customer")
        row = mycursor.fetchall()
        self.update(row)

    def update(self, row):
        self.San_table.delete(*self.San_table.get_children())
        for i in row:
            self.San_table.insert("", "end", values=i)



        ShowdataFrame = Frame(self.root, bg="lavender", relief=GROOVE, borderwidth=1)
        ShowdataFrame.place(x=770, y=70, width=500, height=620)
        scroll_x = Scrollbar(ShowdataFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(ShowdataFrame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(ShowdataFrame, column=(
        "item name", "manufacture", "item category", "quantity", "price", "color", "weight", "enter date", "status")
                                          , xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("item name", text="item name")
        self.Student_table.heading("manufacture", text="manufacture")
        self.Student_table.heading("item category", text="item category")
        self.Student_table.heading("quantity", text="quantity")
        self.Student_table.heading("price", text="price")
        self.Student_table.heading("color", text="color")
        self.Student_table.heading("weight", text="weight")
        self.Student_table.heading("enter date", text="enter date")
        self.Student_table.heading("status", text="status")
        self.Student_table['show'] = "headings"
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.pack()
        mycursor.execute("select * from manifest1")
        row = mycursor.fetchall()
        self.updat(row)
    def updat(self, row):
        self.Student_table.delete(*self.Student_table.get_children())
        for i in row:
            self.Student_table.insert("", "end", values=i)

    #button for home
        self.b1 = Button(self.root, text="HOME", font=('bahnschrift', 17, 'bold'), width=10,bg="white",
                         command=self.addhome)
        self.b1.place(x=8, y=10)

    def addhome(self):
        self.reg = Toplevel(self.root)
        home.product(self.reg)


if __name__ =='__main__':
    root=Tk()
    application=product (root)
    root.mainloop()



