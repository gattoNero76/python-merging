from tkinter import *
import PyPDF2
import os, sys, stat

def create_pdf(dir, dir_to_write, newfile_name):
    # change the permission
    st = os.stat(dir_to_write)
    os.chmod(dir_to_write,  st.st_mode| 0o775)

    files = os.listdir(dir)
    merger = PyPDF2.PdfFileMerger()

    for filename in files:
        merger.append(fileobj=open(os.path.join(dir,filename), 'rb'))

    merger.write(open(os.path.join(dir_to_write, newfile_name), 'wb'))

def mergefile():
    dir1 = e1.get()
    dir_to_write1 = e2.get()
    newfile_name1 = e2.get()

    create_pdf(dir1, dir_to_write1, newfile_name1)

window = Tk()

l1 = Label(window, text = "From:")
l1.grid(row=0, column=0)

directory = StringVar()
e1 = Entry(window, textvariable=directory)
e1.grid(row=0, column=1)

l2 = Label(window, text = "To:")
l2.grid(row=1, column=0)

dir_to_write = StringVar()
e2 = Entry(window, textvariable=dir_to_write)
e2.grid(row=1, column=1)

l3 = Label(window, text = "New file name:")
l3.grid(row=2, column=0)

newfile_name = StringVar()
e3 = Entry(window, textvariable=newfile_name)
e3.grid(row=2, column=1)


b1 = Button(window, text="Merge files", width=12, command=mergefile)
b1.grid(row=3, column=0, columnspan=2)

window.mainloop()
