#!/usr/bin/python
import Tkinter
from Tkinter import *
import ttk
from ttk import *
import webbrowser


def define_it(*args):
    
    try:
	url='http://www.merriam-webster.com/dictionary/'
        webbrowser.open_new_tab(url+word.get())
    except ValueError:
        pass
    
root = Tk()
root.title("Merriam-Webster")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

word = StringVar()

feet_entry = ttk.Entry(mainframe, width=25, textvariable=word)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable="Word").grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Go", command=define_it).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="word").grid(column=3, row=1, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', define_it)

root.mainloop()
