

import img2pdf
from PIL import Image
import os

import tempfile


from PyPDF2 import PdfFileMerger, PdfFileReader


import moviepy.editor as mp
from tkinter import *
from tkinter.filedialog import askopenfile
from moviepy.editor import *
from tkinter import filedialog as fd


import wand.image

root = Tk()

root.title('Video to Audio Converter')


root.configure(bg='#00FF00')

mylabel1 = Label(root, text="Image to pdf", bg='#00FF00')
mylabel2 = Label(root, text="select file", bg='#00FF00')


mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, column=3)


def whenclicked():

    filepath = fd.askopenfilename()
    print(filepath)

    pdf_bytes = img2pdf.convert(filepath)

    file = open("/Users/ajayk/Downloads/new.pdf", "wb")

    file.write(pdf_bytes)

    file.close()


btn = Button(root, text='Open', command=whenclicked)
btn.grid(row=9, column=9)


root.mainloop()
