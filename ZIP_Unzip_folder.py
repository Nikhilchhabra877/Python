###################################################
#############  DEVELOPED BY : Nikhil ##############
import zipfile
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from zipfile import ZipFile
import  os
class Extract:
    def __init__(self,master):
        self.frame1=ttk.Frame(master)
        self.label=ttk.Label(self.frame1,text="Click on unzip button to extract the file",font=('Times new Roman',18,'bold'))
        self.button=ttk.Button(self.frame1,text='Unzip',width=10,command=self._unzip)
        self.button1=ttk.Button(self.frame1,text='Zip Directory',width=10,command=self._zipdir)
        self.logo=PhotoImage(file="/Users/nikhil/Desktop/python_logo.gif").subsample(5,5)
        self.image=self.logo
        self.imagelabel=ttk.Label(self.frame1,image=self.image)

        self.frame1.pack()
        self.label.grid(row=0,column=3,columnspan=2,sticky='nw')
        self.button.grid(row=3,column=3)
        self.button1.grid(row=3,column=4)
        self.imagelabel.grid(row=0,column=1,sticky='nw')

    def _unzip(self):
        path=filedialog.askopenfilename()
        with ZipFile(path,'r') as file:
            print("extracting.....")
            file.extractall()
            print("Completed successfully")


    def _zipdir(self):
        path = filedialog.askdirectory()

        with zipfile.ZipFile('/Users/nikhil/Downloads/Output.zip', mode='w') as zipf:
            len_dir_path = len(path)
            for root, _, files in os.walk(path):
                for file in files:
                    # print(file)
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, file_path[len_dir_path:])
                    # print(path)
                    #zipf.write()

def main():
    root=Tk()
    root.title("Zip/Unzip Program")
    ext = Extract(root)
    root.geometry("800x100")
    root.mainloop()

if __name__==  '__main__':
    main()