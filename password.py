from tkinter import*
from PIL import ImageTk
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
class Please_Login:
    def __init__ (self,root):
        self.root=root
        self.root.title("Change Password")
        self.root.geometry("710x500+0+0")
        self.root.resizable(False, False)
        self.bg=ImageTk.PhotoImage(file="pw.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # frame login
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=360, y=30, height=400, width=320)
        self.item_name = Label(Frame_login,font=('arial', 13, "bold"), text="Current Password:"
                               , fg="black", bg="white").place(x=10, y=20)
        self.txt_itemname = Entry(Frame_login,font=("Goudy old style", 15), bg="white", show="*")
        self.txt_itemname.place(x=10, y=50, width=220, height=35)

        self.item_name = Label(Frame_login,font=('arial', 13, "bold"), text="New Password:"
                               , fg="black", bg="white").place(x=10, y=120)
        self.txt_itemname = Entry(Frame_login,font=("Goudy old style", 15), bg="white", show="*")
        self.txt_itemname.place(x=10, y=150, width=220, height=35)

        self.item_name = Label(Frame_login,font=('arial', 13, "bold"), text="Re-Type New Password:"
                               , fg="black", bg="white").place(x=10, y=220)
        self.txt_itemname = Entry(Frame_login,font=("Goudy old style", 15), bg="white", show="*")
        self.txt_itemname.place(x=10, y=250, width=220, height=35)

        # saves change password button
        save = Button(Frame_login, text=" Save Changes", bg="white", fg="black", bd=0,
                        font=("gouldy old style", 15, "bold")).place(x=10, y=350)



root=Tk()
Please_Login(root)
root.mainloop()
