# Director
from tkinter import *
import tkinter.messagebox
import Project_backend

class Director:
    def __init__(self, root):
        root = Tk()
        root.title("Director window")
        root.geometry("3000x850+0+0")
        root.resizable(True, True)
        root.config(bg="white")
        
        Movie_ID = StringVar(root)
        Director_name =StringVar(root)
        DOB=StringVar(root)

        # Fuctions

        def clcdata():
            self.txtMovie_ID.delete(0, END)
            self.txtDirector_name.delete(0, END)
            self.txtDOB.delete(0, END)
        
        def adddata():
            x=Project_backend.check_movieid(Movie_ID.get())
            if(len(Movie_ID.get()) != 0 and x == 0):
                Project_backend.AddDirectorData(Movie_ID.get(), Director_name.get(), DOB.get())
                searchdb()
            else:
                clcdata()
                messagebox.showerror("Error","Movie id not exists!")
                
        def disdata():
            clcdata()
            MovieList.delete(0, END)
            for row in Project_backend.ViewDirectorData():
                s0="Movie_id :- "+str(row[0])
                s1="        Director_name : "+str(row[1])
                s2="        DOB : "+str(row[2])

                MovieList.insert(END, str(s0), str(""))
                MovieList.insert(END, str(s1))
                MovieList.insert(END, str(s2), str(""))

                MovieList.insert(END, str("---------------------------------------------------------------------------------------------------------------"), str(""))
            i=0
            j=5
            for row in Project_backend.ViewDirectorData():
                MovieList.itemconfig(i, {'fg': '#a4ebf3'})
                MovieList.itemconfig(j, {'fg': '#eff48e'})
                i=i+7
                j=j+7

        def movierec(event):
            global sd
            searchmovie = MovieList.curselection()[0]
            sd = MovieList.get(searchmovie)

            self.txtMovie_ID.delete(0, END)
            self.txtMovie_ID.insert(END, sd[12])

            row=Project_backend.SearchDirectorData(sd[12])
            self.txtDirector_name.delete(0, END)
            self.txtDirector_name.insert(END, row[0][1])
            self.txtDOB.delete(0, END)
            self.txtDOB.insert(END, row[0][2])

        def searchdb():
            MovieList.delete(0, END)
            for row in Project_backend.SearchDirectorData(Movie_ID.get()):
                s0="Movie_id :- "+str(row[0])
                s1="        Director_Name : "+str(row[1])
                s2="        DOB : "+str(row[2])

                MovieList.insert(END, str(s0), str(""))
                MovieList.insert(END, str(s1))
                MovieList.insert(END, str(s2),str(""))
        
                MovieList.insert(END, str("---------------------------------------------------------------------------------------------------------------"), str(""))

            i=0
            j=5
            for row in Project_backend.ViewDirectorData():
                MovieList.itemconfig(i, {'fg': '#a4ebf3'})
                MovieList.itemconfig(j, {'fg': '#eff48e'})
                i=i+7
                j=j+7
            
        def deldata():
            if(len(Movie_ID.get()) != 0):
                Project_backend.DeleteDirectorData(sd[12])
                clcdata()
                disdata()

        def updata():
            if(len(Movie_ID.get()) != 0):
                Project_backend.DeleteDirectorData(sd[12])
            if(len(Movie_ID.get()) != 0):
                Project_backend.AddDirectorData(Movie_ID.get(), Director_name.get(), DOB.get())
                searchdb()

        #Frames
        MainFrame = Frame(root, bg="#28282A")
        MainFrame.grid()

        TFrame = Frame(MainFrame, bd=5, padx=54, pady=10,bg="#28282A", relief=RIDGE)
        TFrame.pack(side=TOP)

        self.TFrame = Label(TFrame, font=('Arial', 51, 'bold'),text="                            DIRECTOR                                ", bg="#28282A", fg="#a4ebf3")
        self.TFrame.grid()  

        BFrame = Frame(MainFrame, bd=0, width=1350, height=70,padx=112, pady=10, bg="#28282A", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame = Frame(MainFrame, bd=0, width=1300, height=400,padx=120, pady=20, bg="#28282A", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL = LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, pady=45, bg="#28282A",relief=RIDGE, font=('Arial', 20, 'bold'), text="Movie Info\n", fg="#ff847c")
        DFrameL.pack(side=LEFT)

        DFrameR = LabelFrame(DFrame, bd=0, width=450, height=300, padx=31, pady=0, bg="#28282A", relief=RIDGE, font=('Arial', 20, 'bold'), text="\tMovie Details\n", fg="#ff847c")
        DFrameR.pack(side=RIGHT)

        # Labels & Entry Box
        self.lblMovie_ID = Label(DFrameL, font=('Arial', 18, 'bold'), text="Movie ID", padx=2, pady=2, bg="#28282A", fg="#eff48e")
        self.lblMovie_ID.grid(row=0, column=0, sticky=W)
        self.txtMovie_ID = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Movie_ID, width=39, bg="light grey", fg="black")
        self.txtMovie_ID.grid(row=0, column=1)

        self.lblDirector_name = Label(DFrameL, font=('Arial', 18, 'bold'), text="Director Name", padx=2, pady=2, bg="#28282A", fg="#eff48e")
        self.lblDirector_name.grid(row=1, column=0, sticky=W)
        self.txtDirector_name = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=Director_name, width=39, bg="light grey", fg="black")
        self.txtDirector_name.grid(row=1, column=1)

        self.lblDOB = Label(DFrameL, font=('Arial', 18, 'bold'), text="DOB", padx=2, pady=2, bg="#28282A", fg="#eff48e")
        self.lblDOB.grid(row=2, column=0, sticky=W)
        self.txtDOB = Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=DOB, width=39, bg="light grey", fg="black")
        self.txtDOB.grid(row=2, column=1)

        # ListBox & ScrollBar
        sb = Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        MovieList = Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=sb.set)
        MovieList.bind('<<ListboxSelect>>', movierec)
        MovieList.grid(row=0, column=0, padx=9)
        sb.config(command=MovieList.yview)

        #  Buttons
        self.btnadd = Button(BFrame, text="Add New", font=('Arial', 20, 'bold'), width=9, height=1, bd=4, bg="#c6fced", command=adddata)
        self.btnadd.grid(row=0, column=0)

        self.btndis = Button(BFrame, text="Display", font=('Arial', 20, 'bold'), width=9, height=1, bd=4, bg="#c6fced", command=disdata)
        self.btndis.grid(row=0, column=1)

        self.btnclc = Button(BFrame, text="Clear", font=('Arial', 20, 'bold'), width=9, height=1, bd=4, bg="#c6fced", command=clcdata)
        self.btnclc.grid(row=0, column=2)

        self.btnse = Button(BFrame, text="Search", font=('Arial', 20, 'bold'), width=9, height=1, bd=4, bg="#c6fced", command=searchdb)
        self.btnse.grid(row=0, column=3)

        self.btnclc = Button(BFrame, text="Delete", font=('Arial', 20, 'bold'), width=9, height=1, bd=4, bg="#c6fced", command=deldata)
        self.btnclc.grid(row=0, column=4)

        self.btnup = Button(BFrame, text="Update", font=('Arial', 20, 'bold'), width=9, height=1, bd=4, bg="#c6fced", command=updata)
        self.btnup.grid(row=0, column=5)

        self.btnx = Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=9, height=20, bd=0, bg="#28282A")
        self.btnx.grid(row=100, column=1)

