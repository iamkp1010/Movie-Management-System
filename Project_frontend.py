# Frontend
from tkinter import *
import tkinter.messagebox
import Project_backend
import cast
import director

Project_backend.MovieData()
Project_backend.Cast()
Project_backend.Director()
Project_backend.foreignkeyon()


class Movie:

    def __init__(self, root):
        self.root = root
        self.root.title("Movie Management System")
        self.root.geometry("3000x850+0+0")
        self.root.resizable(True, True)
        self.root.config(bg="black")

        Movie_Name = StringVar()
        Movie_ID = StringVar()
        Release_Date = StringVar()
        Genre = StringVar() 
        Budget = StringVar()
        Duration = StringVar()
        Rating = StringVar()

        # Fuctions

        def adddirector():
            director.Director(root)

        def addcast():
            cast.Cast(root)

        def Logout():
            Project_backend.check = 1
            Logout = tkinter.messagebox.askyesno(
                "Online Movie Ticket Booking System", "Are you sure?")
            if Logout > 0:
                root.destroy()

        def clcdata():
            self.txtMovie_ID.delete(0, END)
            self.txtMovie_Name.delete(0, END)
            self.txtRelease_Date.delete(0, END)
            self.txtGenre.delete(0, END)
            self.txtBudget.delete(0, END)
            self.txtRating.delete(0, END)
            self.txtDuration.delete(0, END)

        def adddata():
            x=Project_backend.check_movieid(Movie_ID.get())
            if(len(Movie_ID.get()) != 0 and x == 1):
                Project_backend.AddMovieRec(Movie_ID.get(), Movie_Name.get(), Release_Date.get(), Genre.get(), Budget.get(), Duration.get(), Rating.get())
                searchdb()
            else:
                clcdata()
                messagebox.showerror("Error","Movie id already exists!")


        def disdata():
            clcdata()
            MovieList.delete(0, END)

            for row in Project_backend.ViewMovieData():
                s0="Movie_id :- "+str(row[0])
                s1="        Movie_Name : "+str(row[1])
                s2="        Release_Date : "+str(row[2])
                s3="        Genre : "+str(row[3])
                s4="        Budget : "+str(row[4])
                s5="        Duration : "+str(row[5])
                s6="        Rating : "+str(row[6])

                MovieList.insert(END, str(s0), str(""))
                MovieList.insert(END, str(s1))
                MovieList.insert(END, str(s2))
                MovieList.insert(END, str(s3))
                MovieList.insert(END, str(s4))
                MovieList.insert(END, str(s5))
                MovieList.insert(END, str(s6), str(""))
                ii=list(Project_backend.SearchDirectorData(row[0]))

                s7="        Director : "

                if(len(ii)!=0):
                    MovieList.insert(END,str(s7),str(""))
                else:
                    s7+=" Not Available"
                    MovieList.insert(END, str(s7),str(""))

                if(len(ii)!=0):
                    for row1 in Project_backend.SearchDirectorData(row[0]):
                        s8="                Name : "+str(row1[1]) +", DOB : "+str(row1[2])
                        MovieList.insert(END, str(s8))
                
                ii=list(Project_backend.SearchCastData(row[0]))
                s9="        Cast : "

                if(len(ii)!=0):
                    MovieList.insert(END,str(""),str(s9),str(""))
                else:
                    s9+=" Not Available"
                    MovieList.insert(END,str(""),str(s9),str(""))

                if(len(ii)!=0):
                    for row2 in Project_backend.SearchCastData(row[0]):
                        s10="               Name : "+str(row2[1])+", DOB : "+str(row2[2])
                        MovieList.insert(END, str(s10))

                MovieList.insert(END, str("---------------------------------------------------------------------------------------------------------------"), str(""))
            
            i=0
            for row in Project_backend.ViewMovieData(): 
                c=0             
                MovieList.itemconfig(i, {'fg': '#a4ebf3'})
                for row1 in Project_backend.SearchDirectorData(row[0]):
                    c=c+1

                for row2 in Project_backend.SearchCastData(row[0]):
                    c=c+1
                    
                i=i+6+c+10
                MovieList.itemconfig(i-2, {'fg': '#eff48e'})

        def movierec(event):
            global sd
            searchmovie = MovieList.curselection()[0]
            sd = MovieList.get(searchmovie)

            self.txtMovie_ID.delete(0, END)
            self.txtMovie_ID.insert(END, sd[12])

            row=Project_backend.SearchMovieData(sd[12])
            self.txtMovie_Name.delete(0, END)
            self.txtMovie_Name.insert(END, row[0][1])
            self.txtRelease_Date.delete(0, END)
            self.txtRelease_Date.insert(END, row[0][2])
            self.txtGenre.delete(0, END)
            self.txtGenre.insert(END, row[0][3])
            self.txtBudget.delete(0, END)
            self.txtBudget.insert(END, row[0][4])
            self.txtDuration.delete(0, END)
            self.txtDuration.insert(END, row[0][5])
            self.txtRating.delete(0, END)
            self.txtRating.insert(END, row[0][6])

        def deldata():
            if(len(Movie_ID.get()) != 0):
                Project_backend.DeleteMovieRec(sd[12])
                Project_backend.DeleteDirectorData(sd[12])
                Project_backend.DeleteCastData(sd[12])
                clcdata()
                disdata()

        def searchdb():
            MovieList.delete(0, END)
            for row in Project_backend.SearchMovieData(Movie_ID.get()):
                s0="Movie_id :- "+str(row[0])
                s1="        Movie_Name : "+str(row[1])
                s2="        Release_Date : "+str(row[2])
                s3="        Genre : "+str(row[3])
                s4="        Budget : "+str(row[4])
                s5="        Duration : "+str(row[5])
                s6="        Rating : "+str(row[6])

                MovieList.insert(END, str(s0), str(""))
                MovieList.insert(END, str(s1))
                MovieList.insert(END, str(s2))
                MovieList.insert(END, str(s3))
                MovieList.insert(END, str(s4))
                MovieList.insert(END, str(s5))
                MovieList.insert(END, str(s6),str(""))

                ii=list(Project_backend.SearchDirectorData(row[0]))

                s7="        Director : "

                if(len(ii)!=0):
                    MovieList.insert(END,str(s7),str(""))
                else:
                    s7+=" Not Available"
                    MovieList.insert(END, str(s7),str(""))

                if(len(ii)!=0):
                    for row1 in Project_backend.SearchDirectorData(row[0]):
                        s8="                Name : "+str(row1[1]) +", DOB : "+str(row1[2])
                        MovieList.insert(END, str(s8))
                
                ii=list(Project_backend.SearchCastData(row[0]))
                s9="        Cast : "

                if(len(ii)!=0):
                    MovieList.insert(END,str(""),str(s9),str(""))
                else:
                    s9+=" Not Available"
                    MovieList.insert(END,str(""),str(s9),str(""))

                if(len(ii)!=0):
                    for row2 in Project_backend.SearchCastData(row[0]):
                        s10="               Name : "+str(row2[1])+", DOB : "+str(row2[2])
                        MovieList.insert(END, str(s10))

                MovieList.insert(END, str("---------------------------------------------------------------------------------------------------------------"), str(""))

                i=0
                for row in Project_backend.SearchMovieData(Movie_ID.get()): 
                    c=0             
                    MovieList.itemconfig(i, {'fg': '#a4ebf3'})
                    for row1 in Project_backend.SearchDirectorData(row[0]):
                        c=c+1

                    for row2 in Project_backend.SearchCastData(row[0]):
                        c=c+1
                    
                i=i+6+c+10
                MovieList.itemconfig(i-2, {'fg': '#eff48e'})



        def updata():
            if(len(Movie_ID.get()) != 0):
                Project_backend.DeleteMovieRec(sd[12])
            if(len(Movie_ID.get()) != 0):
                Project_backend.AddMovieRec(Movie_ID.get(), Movie_Name.get(), Release_Date.get(), Genre.get(), Budget.get(), Duration.get(), Rating.get())
                searchdb()
                
        # Frames
        MainFrame = Frame(self.root, bg="#28282A")
        MainFrame.grid()

        TFrame = Frame(MainFrame, bd=5, padx=54, pady=10,
                       bg="#28282A", relief=RIDGE)
        TFrame.pack(side=TOP)

        self.TFrame = Label(TFrame, font=('Arial', 51, 'bold'),
                            text="               Movie Management System                 ", bg="#28282A", fg="#a4ebf3")
        self.TFrame.grid()  

        BFrame = Frame(MainFrame, bd=0, width=1350, height=70,
                       padx=112, pady=10, bg="#28282A", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame = Frame(MainFrame, bd=0, width=1300, height=400,
                       padx=120, pady=20, bg="#28282A", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL = LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, pady=45, bg="#28282A",
                             relief=RIDGE, font=('Arial', 20, 'bold'), text="Movie Info\n", fg="#ff847c")
        DFrameL.pack(side=LEFT)

        DFrameR = LabelFrame(DFrame, bd=0, width=450, height=300, padx=31, pady=0, bg="#28282A", relief=RIDGE, font=('Arial', 20, 'bold'), text="\tMovie Details\n", fg="#ff847c")
        DFrameR.pack(side=RIGHT)

        # Labels & Entry Box
        self.lblMovie_ID = Label(DFrameL, font=(
            'Arial', 18, 'bold'), text="Movie ID", padx=2, pady=2, bg="#28282A", fg="#eff48e")
        self.lblMovie_ID.grid(row=0, column=0, sticky=W)
        self.txtMovie_ID = Entry(DFrameL, font=(
            'Arial', 18, 'bold'), textvariable=Movie_ID, width=39, bg="light grey", fg="black")
        self.txtMovie_ID.grid(row=0, column=1)

        self.lblMovie_Name = Label(DFrameL, font=(
            'Arial', 18, 'bold'), text="Movie Name", padx=2, pady=2, bg="#28282A", fg="#eff48e")
        self.lblMovie_Name.grid(row=1, column=0, sticky=W)
        self.txtMovie_Name = Entry(DFrameL, font=(
            'Arial', 18, 'bold'), textvariable=Movie_Name, width=39, bg="light grey", fg="black")
        self.txtMovie_Name.grid(row=1, column=1)

        self.lblRelease_Date = Label(DFrameL, font=(
            'Arial', 18, 'bold'), text="Release Date", padx=2, pady=2, bg="#28282A", fg="#eff48e")
        self.lblRelease_Date.grid(row=2, column=0, sticky=W)
        self.txtRelease_Date = Entry(DFrameL, font=(
            'Arial', 18, 'bold'), textvariable=Release_Date, width=39, bg="light grey", fg="black")
        self.txtRelease_Date.grid(row=2, column=1)

        self.lblGenre = Label(DFrameL, font=(
            'Arial', 18, 'bold'), text="Genre", padx=2, pady=2, bg="#28282A", fg="#eff48e")
        self.lblGenre.grid(row=3, column=0, sticky=W)
        self.txtGenre = Entry(DFrameL, font=(
            'Arial', 18, 'bold'), textvariable=Genre, width=39, bg="light grey", fg="black")
        self.txtGenre.grid(row=3, column=1)

        self.lblBudget = Label(DFrameL, font=(
            'Arial', 18, 'bold'), text="Budget (Crores INR)", padx=2, pady=2, bg="#28282A", fg="#eff48e")
        self.lblBudget.grid(row=4, column=0, sticky=W)
        self.txtBudget = Entry(DFrameL, font=(
            'Arial', 18, 'bold'), textvariable=Budget, width=39, bg="light grey", fg="black")
        self.txtBudget.grid(row=4, column=1)

        self.lblDuration = Label(DFrameL, font=(
            'Arial', 18, 'bold'), text="Duration (Hrs)", padx=2, pady=2, bg="#28282A", fg="#eff48e")
        self.lblDuration.grid(row=5, column=0, sticky=W)
        self.txtDuration = Entry(DFrameL, font=(
            'Arial', 18, 'bold'), textvariable=Duration, width=39, bg="light grey", fg="black")
        self.txtDuration.grid(row=5, column=1)

        self.lblRating = Label(DFrameL, font=(
            'Arial', 18, 'bold'), text="Rating (Out of 5)", padx=2, pady=2, bg="#28282A", fg="#eff48e")
        self.lblRating.grid(row=6, column=0, sticky=W)
        self.txtRating = Entry(DFrameL, font=(
            'Arial', 18, 'bold'), textvariable=Rating, width=39, bg="light grey", fg="black")
        self.txtRating.grid(row=6, column=1)

        #ListBox & ScrollBar
        sb = Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        MovieList = Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="black", fg="white", yscrollcommand=sb.set)
        MovieList.bind('<<ListboxSelect>>', movierec)
        MovieList.grid(row=0, column=0, padx=9)
        sb.config(command=MovieList.yview)

        # Buttons
        self.btnadd = Button(BFrame, text="Add New", font=(
            'Arial', 20, 'bold'), width=8, height=1, bd=4, bg="#c6fced", command=adddata)
        self.btnadd.grid(row=0, column=0)

        self.btnadd = Button(BFrame, text="Director", font=(
            'Arial', 20, 'bold'), width=8, height=1, bd=4, bg="#c6fced", command=adddirector)
        self.btnadd.grid(row=0, column=1)

        self.btnadd = Button(BFrame, text="Cast", font=(
            'Arial', 20, 'bold'), width=8, height=1, bd=4, bg="#c6fced", command=addcast)
        self.btnadd.grid(row=0, column=2)

        self.btndis = Button(BFrame, text="Display", font=(
            'Arial', 20, 'bold'), width=8, height=1, bd=4, bg="#c6fced", command=disdata)
        self.btndis.grid(row=0, column=3)

        self.btnclc = Button(BFrame, text="Clear", font=(
            'Arial', 20, 'bold'), width=8, height=1, bd=4, bg="#c6fced", command=clcdata)
        self.btnclc.grid(row=0, column=4)

        self.btnse = Button(BFrame, text="Search", font=(
            'Arial', 20, 'bold'), width=8, height=1, bd=4, bg="#c6fced", command=searchdb)
        self.btnse.grid(row=0, column=5)

        self.btndel = Button(BFrame, text="Delete", font=(
            'Arial', 20, 'bold'), width=8, height=1, bd=4, bg="#c6fced", command=deldata)
        self.btndel.grid(row=0, column=6)

        self.btnup = Button(BFrame, text="Update", font=(
            'Arial', 20, 'bold'), width=8, height=1, bd=4, bg="#c6fced", command=updata)
        self.btnup.grid(row=0, column=7)

        self.btnx = Button(BFrame, text="Log Out", font=(
            'Arial', 20, 'bold'), width=8, height=1, bd=4, bg="salmon", command=Logout)
        self.btnx.grid(row=0, column=8)

        self.btnx = Button(BFrame, text="Exit", font=(
            'Arial', 20, 'bold'), width=8, height=20, bd=0, bg="#28282A")
        self.btnx.grid(row=100, column=1)


if __name__ == '__main__':
    root = Tk()
    root.mainloop()
