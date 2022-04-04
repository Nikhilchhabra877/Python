###################################################
#############  DEVELOPED BY : Nikhil ##############

## Steps:

# Define the project requirements: A Feedback form with below requirements:
  # It will Display a logo and instructions to user
  # The form will have input fiels for email,name and comments.
  # Two buttons for submission and clear the entry fields after submission.
# Plan or sketch the design.
# List down the different types of widgets that needs to be created for the project.
### In this case we create below widgets
# Two frames on top level window for header and contents.
#Toplevel : Master
 #Frame1: Header
    #Label: logo
    #Label: header
    #Label: message
 #Frame: Contents
    #Label: Name
    #Label: Email
    #Label: Comments
    #Entry: Name
    #Entry: Email
    #Entry: Comments(Text widget for multiline comments
    #Button: Submit
    #Button: Clear
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
class Feedback:
    def __init__(self,master):

       # master.title("UAE Trip Feedback")
        #master.resizeable(False,False)
        #master.configure()

        self.style=ttk.Style()
        self.style.configure('Tframe')

        self.frame1=ttk.Frame(master)
        self.frame1.pack()
        self.logo=PhotoImage(file="/Users/nikhil/Desktop/tour_logo.gif")

        ttk.Label(self.frame1,image=self.logo).grid(row=0,column=0,rowspan=2,sticky='ne',padx=5)
        ttk.Label(self.frame1,text="Thanks for the booking!").grid(row=0,column=1)
        ttk.Label(self.frame1,wraplength=400,text=("We are happy that you choose ABC tours Pvt.Ltd. for booking the Holiday package"
                                   "in UAE. Please share your  experience with us to improve our services.")).grid(row=1,column=1)

        self.frame2=ttk.Frame(master)
        self.frame2.pack()

        ttk.Label(self.frame2,text="Name:").grid(row=0,column=0,padx=5,sticky='sw')
        ttk.Label(self.frame2, text="Email:").grid(row=0,column=1,padx=5,sticky='sw')
        ttk.Label(self.frame2, text="Comments:").grid(row=2,column=0,padx=5,sticky='sw')

        self.entry_name= ttk.Entry(self.frame2,width=25)
        self.entry_name.grid(row=1,column=0,padx=5)
        self.entry_email=ttk.Entry(self.frame2,width=25)
        self.entry_email.grid(row=1,column=1,padx=5,)
        self.entry_comments=Text(self.frame2,width=50,height=10)
        self.entry_comments.grid(row=3,column=0,columnspan=2,padx=5)

        ttk.Button(self.frame2,text="Submit",command=self.check_table).grid(row=4,column=0,padx=5,sticky='e')
        ttk.Button(self.frame2,text="Clear",command=self.clearentry).grid(row=4,column=1,padx=5,sticky='w')
        self.path="/Users/nikhil/Desktop/testing.db"
        #self.name=self.entry_name.get()
        #self.email=self.entry_email.get()
        #self.comments=self.entry_comments.get('1.0','end')
    def clearentry(self):
        self.entry_name.delete(0,'end')
        self.entry_email.delete(0,'end')
        self.entry_comments.delete('1.0','end')

    def submitentry(self):
        print("Name: {}".format(self.entry_name.get()))
        print("Email: {}".format(self.entry_email.get()))
        print("Comments: {}".format(self.entry_comments.get('1.0','end')))
        self.clearentry()
        messagebox.showinfo(title="UAE Tour Feedback", message="Feedback has been submitted")


    def check_table(self):
        self.name = self.entry_name.get()
        self.email = self.entry_email.get()
        self.comments = self.entry_comments.get('1.0', 'end')
        conn=sqlite3.connect(self.path)
        conn.execute("CREATE table IF NOT EXISTS Feedback(ID INTEGER PRIMARY KEY,Name TEXT,Email TEXT,Comment TEXT)")

        conn.execute("insert into Feedback (Name,Email,Comment) values(?,?,?)", (self.name,self.email,self.comments))
        conn.commit()
        self.clearentry()
        messagebox.showinfo(title="UAE Tour Feedback", message="Feedback has been submitted")
        conn.close()
        #check_table("/Users/nikhil/Desktop/testing.db","Krati","Krati.ahlawat91@gmail.com","It was a good Tour,However,few thing needs improvement")
def main():
    root=Tk()
    root.title("International Travels Pvt. Limited")
    feedback=Feedback(root)
    root.mainloop()
if __name__ == '__main__':
    main()
