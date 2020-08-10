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
class Password:
    def __init__ (self,root):
        self.root=root
        self.root.title("Change Password")
        self.root.geometry("710x500+0+0")
        self.root.resizable(False, False)
        self.bg=ImageTk.PhotoImage(file="pw.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.oldusername = StringVar()
        self.oldpw = StringVar()
        self.newpw1 = StringVar()
        self.newpw2 =StringVar()
        # frame login
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=360, y=30, height=400, width=320)
        self.item_pw = Label(Frame_login, font=('arial', 13, "bold"), text="Current Username:"
                               , fg="black", bg="white").place(x=10, y=20)
        self.txt_itempw = Entry(Frame_login, textvariable=self.oldusername, font=("Goudy old style", 15), bg="white",
                                )
        self.txt_itempw.place(x=10, y=50, width=220, height=35)

        self.item_pw = Label(Frame_login,font=('arial', 13, "bold"), text="Current Password:"
                               , fg="black", bg="white").place(x=10, y=100)
        self.txt_itempw = Entry(Frame_login, textvariable=self.oldpw,font=("Goudy old style", 15), bg="white", show="*")
        self.txt_itempw.place(x=10, y=130, width=220, height=35)

        self.item_pw = Label(Frame_login,font=('arial', 13, "bold"), text="New Password:"
                               , fg="black", bg="white").place(x=10, y=180)
        self.txt_itempw = Entry(Frame_login,font=("Goudy old style", 15),textvariable=self.newpw1, bg="white", show="*")
        self.txt_itempw.place(x=10, y=210, width=220, height=35)

        self.item_pw = Label(Frame_login,font=('arial', 13, "bold"), text="Re-Type New Password:"
                               , fg="black", bg="white").place(x=10, y=260)
        self.txt_itempw = Entry(Frame_login,font=("Goudy old style", 15), bg="white",textvariable=self.newpw2, show="*")
        self.txt_itempw.place(x=10, y=290, width=220, height=35)

        # saves change password button
        save = Button(Frame_login, text=" Save Changes", bg="white", fg="black", bd=0,command=self.changePw,
                        font=("gouldy old style", 15, "bold")).place(x=10, y=350 )

    def changePw(self):
        oldUsername = self.oldusername.get()
        oldPw=self.oldpw.get()
        newPw1 = self.newpw1.get()
        newPw2 = self.newpw2.get()
        sql='select password from login where username=%s'
        valu = (oldUsername,)
        mycursor.execute(sql,valu)
        myresult = mycursor.fetchall()
        for i in myresult:
            id=i[0]
        if id== oldPw:
            if newPw1 == newPw2:
                query = "UPDATE login set password=%s where username=%s"
                valu = (newPw1,oldUsername)
                mycursor.execute(query,valu)
                mydb1.commit()
                self.oldpw.set("")
                self.newpw1.set("")
                self.newpw2.set("")
                messagebox.showinfo("warining", "password changed")

            else:
                messagebox.showinfo("warining" , "Password not macthing")

        else:
            messagebox.showinfo("warining", "Usename or old Password not matching")


#root=Tk()
#Password(root)
#root.mainloop()
