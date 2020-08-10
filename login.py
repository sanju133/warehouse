
from tkinter import*
from PIL import ImageTk
#import password
from home import product
from password import Password
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
        self.root.title("Please Login")
        self.root.geometry("640x426+100+50")
        self.root.resizable(False, False)
        self.bg=ImageTk.PhotoImage(file='sanjumaharjan.jpg')
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        global usename1
        global rollno1
        self.uusername = StringVar()
        self.upassword = StringVar()

        # frame login
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=305, y=70, height=300, width=320)

        # label for interface heading
        title = Label(Frame_login, text="LOGIN SYSTEM !!", font=("bahnschrift", 15, "bold"),
                      fg="black", bg="white").place(x=10, y=20)
        sam = Label(Frame_login, text="Please login in here", font=("arial", 12, "bold"),
                    fg="black", bg="white").place(x=10, y=50)
        self.namevar = StringVar()
        self.pwvar = StringVar()
        # label and entry for username
        self.lbluser = Label(Frame_login, font=('Bahnschrift', 15, "bold"), text="USER NAME:"
                             , fg="black", bg="white").place(x=10, y=90)
        self.txt_username = Entry(Frame_login, font=("Goudy old style", 15), bg="white", textvariable=self.namevar)
        self.txt_username.place(x=130, y=90, width=170, height=25)

        # label and entry for password
        self.lbluser = Label(Frame_login, font=('Bahnschrift', 15, "bold"), text="PASSWORD:"
                             , fg="black", bg="white").place(x=10, y=130)
        self.txt_userpw = Entry(Frame_login, font=("Goudy old style", 15), bg="white", textvariable=self.pwvar,
                                show="*")
        self.txt_userpw.place(x=130, y=130, width=170, height=25)

        # login button
        self.login = Button(self.root, text="LOGIN", bg="white", fg="black", command=self.loginAdd,
                            font=("Bahnschrift", 15, "bold")).place(x=350, y=260, width=200, height=30)

        # change password button
        change = Button(Frame_login, text="Change Password?", bg="white", fg="black", bd=0,
                        command=self.changepasswordlogin,
                        font=("Bahnschrift", 15, "bold")).place(x=10, y=260)

    def loginAdd(self):
        username1 = self.txt_username.get()
        rollno1 = self.txt_userpw.get()
        sql = "SELECT * FROM login where username=%s"
        value = (username1,)

        mycursor.execute(sql, value)
        myresult = mycursor.fetchall()
        global id
        global pw
        for i in myresult:
            id = i[0]
            pw = i[1]
        #file handling
        files = open("myOutFile.txt", "w")
        # write line to output file
        files.write("id:"+ str(id))
        files.write(" password:"+str(pw))
        files.close()

        files = open("myOutFile.txt", 'r')
        all = files.read()
        x = all.split(" ")
        y = x[0].split(":")
        z = x[1].split(":")


        if (username1 == "" or rollno1 == ""):
            messagebox.showinfo("Information", "Fill all the fields")
        ##elifelif (username1 == id and rollno1 == pw): for database
        elif (username1 == y[1] and rollno1 == z[1]):
            self.reg = Toplevel(self.root)

            product(self.reg)


        else:
            messagebox.showinfo("Information", "The entered data are incorrect")





    def changepasswordlogin(self):
        self.reg = Toplevel(self.root)

        Password(self.reg)


root=Tk()
Please_Login(root)
root.mainloop()