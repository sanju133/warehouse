from tkinter import*
from PIL import ImageTk
import company
import manifest
import customer
import warehouse
class product:

        def __init__(self, root):
            self.root = root
            self.root.title("WAREHOUSE MANAGEMENT SYSTEM")
            self.root.geometry("1024x768+0+0")
            self.root.resizable(False, False)
            self.bg = ImageTk.PhotoImage(file='hello.jpg')
            self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
            self.te = Label(self.root, text="  WAREHOUSE MANGEMENT SYSTEM!! ", font=("goudy old style", 41, "bold"),
                            fg="black", bg="white")
            self.te.pack()
            self.b1 = Button(self.root, text="COMPANY", command=self.addcompany, font=('bahnschrift', 20, 'bold'),
                             width=15)
            self.b2 = Button(self.root, text="MAINFEST", command=self.addmanifest, font=('bahnschrift', 20, 'bold'),
                             width=15)
            self.b3 = Button(self.root, text="SHIPMENT", command=self.addcustomer, font=('bahnschrift', 20, 'bold'),
                             width=15)
            self.b4 = Button(self.root, text="WAREHOUSE", command=self.addwarehouse, font=('bahnschrift', 20, 'bold'),
                             width=15)
            self.b1.place(x=40, y=200)
            self.b2.place(x=350, y=200)
            self.b3.place(x=40, y=350)
            self.b4.place(x=350, y=350)

            self.button_quit = Button(self.root, text="QUIT", command=root.quit, font=('bahnschrift', 20, 'bold'),
                                      width=15)

            self.button_quit.place(x=30, y=500)


        def addcompany(self):
            self.reg = Toplevel(self.root)
            company.product(self.reg)

        def addmanifest(self):
            self.reg = Toplevel(self.root)
            manifest.product(self.reg)

        def addcustomer(self):
            self.reg = Toplevel(self.root)
            customer.product(self.reg)

        def addwarehouse(self):
            self.reg = Toplevel(self.root)
            warehouse.product(self.reg)








