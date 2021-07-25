from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import Project_backend
import Project_frontend
from tkinter import font

loginfo={"Admin":"321jkj123"}

class Login:
    x=0  
    def __init__(self,root):

        self.root=root
        self.root.title("LoginSystem")
        self.root.geometry("1152x737+0+0")
        self.root.resizable(False,False)
        
        self.bg=ImageTk.PhotoImage(file="abc.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="#DDCBE3")
        Frame_login.place(x=335,y=85,height=240,width=480)

        if Login.x==0 :
            title=Label(Frame_login,text="Login Here",font=("Comic sans ms",25,"bold"),fg="#181540",bg="#DDCBE3").place(x=155,y=10)
        else:
            title=Label(Frame_login,text="Signup Here",font=("Comic sans ms",25,"bold"),fg="#181540",bg="#DDCBE3").place(x=155,y=10)
            Login.x==0

        lbl_user=Label(Frame_login,text="Username",font=("Comic sans ms",15,"bold"),fg="#181540",bg="#DDCBE3").place(x=50,y=80)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="white")
        self.txt_user.place(x=175,y=88,width=250,height=25)
        

        lbl_pass=Label(Frame_login,text="Password",font=("Comic sans ms",15,"bold"),fg="#181540",bg="#DDCBE3").place(x=50,y=120)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="white",show='*')
        self.txt_pass.place(x=175,y=130,width=250,height=25)

        if Login.x==0 :
            Login_btn=Button(self.root,command=self.login_function,text="Login",fg="white",bg="#181540",font=("Comic sans ms",12)).place(x=445,y=275,width=130)
            Signupp_btn=Button(self.root,command=self.signupp_function,text="Signup",fg="white",bg="#181540",font=("Comic sans ms",12)).place(x=598,y=275,width=130)
        else:
            Signup_btn=Button(self.root,command=self.signup_function,text="Signup",fg="white",bg="#181540",font=("Comic sans ms",12)).place(x=500,y=275,width=160)
            
    def window2(self):
        Project_frontend.Movie(root)

    def signupp_function(self):
        Login.x=1
        self.__init__(root)
        Login.x=0
        
    def login_function(self):
        username=self.txt_user.get()
        password=self.txt_pass.get()
        if username=="" or password=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
            self.__init__(root)
        elif username in loginfo:
            if password!=loginfo[username]:
                messagebox.showerror("Error","Incorrect Password!",parent=self.root)
                self.__init__(root)
            else :
                messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\n",parent=self.root)    
                self.window2()
        else:
            messagebox.showerror("Error","Incorrect Username!",parent=self.root)
            self.__init__(root)
            
    def signup_function(self):

        username=self.txt_user.get()
        password=self.txt_pass.get()
        
        if (username=="" or password=="") :
            Login.x=1
            self.__init__(root)
            Login.x=0
            return
        
        
        if Login.x==0:        
            if username in loginfo:
                messagebox.showerror("Error","Username not available!",parent=self.root)            
            else:
                loginfo.update({username:password})
                messagebox.showinfo("Welcome","Thank you for creating account")
        
        self.__init__(root)
        

while(Project_backend.check):
    root=Tk()
    obj=Login(root)
    Project_backend.check=0
    root.mainloop()