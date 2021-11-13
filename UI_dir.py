from tkinter import ttk, Tk
from tkinter import *
from class_dir import Voyage, Sector


class Window(object):
    def setupUI(self):
        root = Tk()
        root.title("Journaal")
        root.minsize(width=795, height=410)
        root.maxsize(width=795, height=410)

        voyage_frame = ttk.Frame(root, padding="3 3 12 12")
        voyage_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        Voyage.setup_voyage_UI(voyage_frame)

        sector_frame = ttk.Frame(root, padding="3 3 12 12")
        sector_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        label2 = ttk.Label(sector_frame, text="Sectoren")
        label2.grid(column=1, row=1, sticky=(W, E))

        root.mainloop()
