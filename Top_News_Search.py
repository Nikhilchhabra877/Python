### Developed by : Nikhil ######

'''
- Top headlines application

This program fetch the TOP news and display the title, description and photo by using TKinter.
We can read top-20 headline of a specific country by pressing previous and next button. if you want to read more about
it ,then press next to open the webpage that contains full article.
'''

import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image

class TopNewsApp:
    def __init__(self):
        ### Fetch the data from web
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=ca&apiKey=1760b9c3e25842e4a3a045fd89270f0d").json()
        ### Function to load the basic initial GUI
        self.load_gui()
        ### Fetch the json data from web and display using TKinter  GUI
        self.load_news(0)

    ### Function for initialize the GUI
    def load_gui(self):
        self.root = Tk()
        self.root.title("Top Headlines")
        self.root.geometry("450x700")
        self.root.resizable(0,0)
        self.root.configure(background='black')

    ### Clear the GUI page
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    ### Load the data and and display on the page
    def load_news(self,index):
        self.clear()
        try:
            image = self.data['articles'][index]['urlToImage']
            r_data = urlopen(image).read()
            img = Image.open(io.BytesIO(r_data)).resize((350,250))
            photo = ImageTk.PhotoImage(img)
        except:
            image = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            r_data = urlopen(image).read()
            im = Image.open(io.BytesIO(r_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image=photo)
        label.pack()


        heading = Label(self.root,text = self.data['articles'][index]['title'],bg='black',fg='white',wraplength=400,justify='center',font=('Times New Roman',14))
        des = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=400,justify='center',font=('Times New Roman',12))
        heading.pack(pady=(10,20))
        des.pack(pady=(10,20))
        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if index !=0:
            prev = Button(self.root,text='Prev',width=16,height=3,command=lambda : self.load_news(index - 1))
            prev.pack(side=LEFT)
        read = Button(self.root,text='More',width=16,height=3,command=lambda: self.open_url(self.data['articles'][index]['url']))
        read.pack(side=LEFT)
        if index != len(self.data['articles']) -1:
            next = Button(self.root,text='Next',width=16,height=3,command=lambda : self.load_news(index + 1))
            next.pack(side=LEFT)
        self.root.mainloop()

    ### Function for opening the webpage
    def open_url(self,url):
        webbrowser.open(url)

obj = TopNewsApp()