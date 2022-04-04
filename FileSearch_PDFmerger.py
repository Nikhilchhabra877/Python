###################################################
#############  DEVELOPED BY : Nikhil ##############
import os
import pathlib
from tkinter import *
from tkinter import ttk
from tkscrolledframe import ScrolledFrame
from PyPDF2 import PdfFileMerger
import tkscrolledframe
class searchfiles:

    def __init__(self, master):
        self.frame1 = ttk.Frame(master)
        self.frame1.pack()
        self.label1 = ttk.Label(self.frame1,
                                text="Welcome folks ,we can search all the files easily by entering the PATH:-",font=('Times new Roman',18,'bold'))
        self.entry_path = ttk.Entry(self.frame1, width=30)
        self.button = ttk.Button(self.frame1, text="Search",command=self.pathfromuser)
        self.label1.grid(row=0, column=1,sticky="nw")
        self.entry_path.grid(row=0, column=2, sticky='e')
        self.button.grid(row=0, column=3, columnspan=2, sticky='w')

        self.frame2 = ttk.Frame(master)
        self.frame2.pack(side="top", expand=1, fill="both")
        self.sf = ScrolledFrame(self.frame2, width=380, height=240)
        self.sf.pack(side="top", expand=1, fill="both")
        self.sf.bind_arrow_keys(self.frame2)
        self.sf.bind_scroll_wheel(self.frame2)
        #self.frame3 = self.sf.display_widget(ttk.Frame)

        self.pdfframe=ttk.Frame(master)
        self.pdfframe.pack(side="top", expand=1, fill="both")

        self.labelforpdf=ttk.Label(self.pdfframe,text="Do you want to search the pdf files from the above path and merge? Enter the path and press yes to proceed. PATH:-",wraplength=500,font=('Times new Roman',18,'bold'))
        self.buttonpdf=ttk.Button(self.pdfframe,text="Press yes",command=self.searchandmergepdf)
        self.entry_path1 = ttk.Entry(self.pdfframe, width=30)
        self.entry_path1.grid(row=1, column=2, sticky='e',rowspan=2)
        self.labelforpdf.grid(row=1,column=1,sticky="nw",rowspan=4)
        self.buttonpdf.grid(row=1,column=3,sticky='w')

        #self.path1 = self.entry_path.get()
    def pathfromuser(self):

        path=self.entry_path.get()
        if os.path.exists(path):
            print(path)
            list1=[]
            for p in pathlib.Path(path).iterdir():
                if p.is_file():
                    list1.append(str(p) + "\n")
                self.frame3 = self.sf.display_widget(ttk.Frame)
                ttk.Label(self.frame3, text=list1, foreground='yellow').pack()
                self.entry_path.delete(0, 'end')

        else:
            self.show= "Invalid path!!"
            self.frame4 = self.sf.display_widget(ttk.Frame)
            ttk.Label(self.frame4,text=self.show,foreground='red',font=('Times new Roman',15,'bold'),justify=CENTER).grid(row=3,column=1)

    def searchandmergepdf(self):

        source_dir = self.entry_path1.get()
        #print((self.entry_path.get()))
        merger = PdfFileMerger()
        if os.path.exists(source_dir):
            for item in os.listdir(source_dir+"/"):
                if item.endswith('pdf'):
                # print(item)
                    merger.append(source_dir+ str('/') + item)
            #print(merger)

        #merger.write(source_dir + "/" + '/Complete.pdf')
            merger.write(source_dir +str('/')+"complete.pdf")
            merger.close()
            message="PDF has been saved at {}".format(source_dir)
            ttk.Label(self.pdfframe, text=message, foreground='yellow').grid(row=7,column=2)

        else:
            self.show = "Invalid path!! please enter the valid path"
            self.frame4 = self.sf.display_widget(ttk.Frame)
            ttk.Label(self.pdfframe, text=self.show, foreground='red', font=('Times new Roman', 15, 'bold'),
                      justify=CENTER).grid(row=7, column=3)

            #print("invalid path")

def main():
    root = Tk()
    search = searchfiles(root)
    root.title("File Search engine")
    root.geometry("1380x1340")
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