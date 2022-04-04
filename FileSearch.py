import os
import pathlib
from tkinter import *
from tkinter import ttk


class searchfiles:

    def __init__(self, master):
        self.frame1 = ttk.Frame(master)
        self.frame1.pack()
        self.label1 = ttk.Label(self.frame1, wraplength=200,
                                text="Welcome folks ,we can search all the files easily by entering the path")
        self.entry_path = ttk.Entry(self.frame1, width=30)
        self.button = ttk.Button(self.frame1, text="Search",command=self.pathfromuser)

        self.label1.grid(row=0, column=1, columnspan=2)
        self.entry_path.grid(row=2, column=1, sticky='e')
        self.button.grid(row=2, column=5, columnspan=2, sticky='w')

        self.frame2=ttk.Frame(master)
        self.frame2.pack()


    def pathfromuser(self):
        path=self.entry_path.get()
        if os.path.exists(path):
            print(path)
            list1=[]
            for p in pathlib.Path(path).iterdir():
                if p.is_file():
                    list1.append(str(p) + "\n")
                #final_string = '\n'.join(list1)
                #print(final_string)
                ttk.Label(self.frame2, text=list1, foreground='red').grid(row=3, column=1)
                self.entry_path.delete(0,'end')
        else:
            self.show= "Invalid path!!"
            ttk.Label(self.frame1,text=self.show,foreground='red').grid(row=3,column=1)

   # def file_search(self,path):
        # path = "/Users/nikhil/Desktop"
      #  for p in pathlib.Path(path).iterdir():
        #    if p.is_file():
         #       print(p)

def main():
    root = Tk()
    search = searchfiles(root)
    root.title("File Search engine")
    root.geometry("640x240")
    root.mainloop()


if __name__ == '__main__':
    main()

'''
def file_search():
    #path = "/Users/nikhil/Desktop"
    for p in pathlib.Path(path).iterdir():
        if p.is_file():
            print(p)
#file_search()
'''