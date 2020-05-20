"""Gui script for diary."""
import sys
from tkinter import *
from tkcalendar import Calendar, DateEntry
import os

class gui:

    def __init__(self, main_form):
        main_form.title("Diary")
        #main_form.geometry("800x600")
        main_form.minsize(800, 600)
        main_form.grid_rowconfigure(0, weight=1)
        main_form.grid_columnconfigure(0, weight=1)
        ROOTPATH = os.path.dirname(__file__)
        print(ROOTPATH)

        main_frame = Frame(main_form)
        main_frame.grid(row=0, column=0, sticky="NEW")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=0)
        main_frame.grid_columnconfigure(2, weight=1)

def main( ):
    root = Tk()
    gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
