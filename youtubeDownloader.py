from __future__ import unicode_literals

from tkinter import *

from pytube import YouTube


root = Tk()


root.title('Youtube Downloader')

root.geometry("500x250")
root.resizable(0, 0)
root.configure(bg='#e65050')


mylabel2 = Label(root, text="Paste the link here",
                 bg='#e65050', font='poppins')

e = Entry(root)
e.grid(row=1, column=1, pady=(100, 10), padx=(40))


mylabel2.grid(row=1, column=0, pady=(100, 10), padx=(20))


ydl_opts = {}


def whenclicked():
    textin = e.get()

    try:
        YouTube(textin).streams.first().download('/Users/ajayk/Downloads')
        mylabel3 = Label(root, text='Download finished')
    except:
        mylabel3 = Label(root, text='Failed to Download')

    mylabel3.grid(row=3, column=0, padx=(100, 10))


mybutton = Button(root, text='Download', command=whenclicked,
                  font='poppins', borderwidth='4')
mybutton.grid(row=2, column=1, padx=(10, 10))

root.mainloop()
