"""Gui script for diary."""
import sys
from tkinter import *
from tkcalendar import Calendar, DateEntry
import os
from . import __version__

class gui:



    def __init__(self, main_form):
        main_form.title("Diary GUI")
        #main_form.geometry("800x600")
        main_form.minsize(800, 600)
        main_form.grid_rowconfigure(0, weight=1)
        main_form.grid_columnconfigure(0, weight=1)
        ROOTPATH = os.path.dirname(__file__)
        print(ROOTPATH)

        date_picker_pattern = "y mm dd"  # used to display the date at date piker.
        date_picker_format_str = '%Y %m %d'  # used at date function to convert datepiker selected date.


        font_cal = "Arial 17"
        font_gui = "Arial 11"
        font_menu = "Arial 13"
        font_header_title = "Arial 20"
        font_header = "Arial 15"
        font_label_input = "Arial 10"
        font_input = "Arial 16"
        width_input = 7
        font_submit = "Arial 11"
        font_result = "Arial 16"

        main_frame = Frame(main_form)
        main_frame.grid(row=0, column=0, sticky="NEW")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=0)
        main_frame.grid_columnconfigure(2, weight=1)

        # menu
        menu_bar = Menu(main_form)
        main_form.config(menu=menu_bar)
        main_form.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(font=font_menu, label="About",command=self.about_command)
        file_menu.add_command(font=font_gui, label="Save Diary",)
        file_menu.add_command(font=font_gui, label="Settings")
        file_menu.add_command(font=font_gui, label="Import")
        file_menu.add_command(font=font_gui, label="Export")
        file_menu.add_separator()
        file_menu.add_command(font=font_menu, label="Exit", underline=1, accelerator='Alt-X',
                                   command=lambda arg1=main_form: self.quit(arg1))

        menu_bar.add_cascade(font=font_gui, label="File", menu=file_menu)
        menu_bar.bind_all("<Alt-x>", self.quit)

        diary_menu = Menu(menu_bar, tearoff=0)
        diary_menu.add_command(font=font_gui, label="Random Diary")

        diary_menu.add_command(font=font_gui, label="Today Diary")
        diary_menu.add_command(font=font_gui, label="Tomorrow")
        diary_menu.add_command(font=font_gui, label="Yesterday")
        diary_menu.add_separator()
        diary_menu.add_command(font=font_gui, label="Next Diary")
        diary_menu.add_command(font=font_gui, label="Previous Diary")
        diary_menu.add_command(font=font_gui, label="Last year same day")
        diary_menu.add_command(font=font_gui, label="Next year same day")
        diary_menu.add_separator()
        diary_menu.add_command(font=font_gui, label="First Diary")
        diary_menu.add_command(font=font_gui, label="Last Diary")

        menu_bar.add_cascade(font=font_gui, label="Diary", menu=diary_menu)

        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(font=font_gui, label="Cut")
        edit_menu.add_command(font=font_gui, label="Copy")
        edit_menu.add_command(font=font_gui, label="Paste")
        edit_menu.add_separator()
        edit_menu.add_command(font=font_gui, label="Delete Current Diary")

        menu_bar.add_cascade(font=font_gui, label="Edit", menu=edit_menu)




    def quit(self, event):
        #print("quitting...")
        sys.exit(0)


    def about_command(self):



        self.about_window = Toplevel()
        self.about_window.geometry("480x480")
        self.about_window.resizable(0, 0)
        self.about_window.title("About")

        self.about_window.grid_rowconfigure(0, weight=0)
        self.about_window.grid_rowconfigure(1, weight=1)
        self.about_window.grid_rowconfigure(2, weight=1)
        self.about_window.grid_rowconfigure(3, weight=1)
        self.about_window.grid_rowconfigure(4, weight=1)
        self.about_window.grid_rowconfigure(5, weight=1)
        self.about_window.grid_columnconfigure(0, weight=1)

        self.ROOT_DIR = os.path.dirname(__file__)
        self.bannerabout = PhotoImage(file=self.ROOT_DIR + '/banner480x160.png')


        self.about_link_doc = Label(self.about_window, image=self.bannerabout, width=480, height=160)
        self.about_link_doc.grid(row=0, column=0, sticky="")
        self.about_link_doc.configure(padx=10, pady=10)

        self.about_text = "" \
                "Diary "+ str(__version__) +"  \r\r" \
                "Record your daily experiences from terminal or gui and see the difference!.  Diary helps you focus on your thoughts and make journaling a pleasant experience.\r\r" \
                "This program is free software under GPL V3 \r\r" \
                "Copyright (C) 2020  anopensourcecoder" \

        self.about_messagearea = Message(self.about_window, width=460, text = self.about_text)

        self.about_messagearea.grid(row=1, column=0,sticky="WN")
        self.about_messagearea.configure(padx=10, pady=10)

        self.about_link_doc = Label(self.about_window, text="Read Diary's Wiki for more details", fg="blue", cursor="hand2")
        self.about_link_doc.grid(row=2, column=0, sticky="WN")
        self.about_link_doc.configure(padx=10, pady=10)
        self.about_link_doc.bind("<Button-1>", lambda e: self.link("https://github.com/anopensourcecoder/diary/wiki"))

        self.about_link_github = Label(self.about_window, text="Visit Diary on github and get involved.", fg="blue",
                                    cursor="hand2")
        self.about_link_github.grid(row=3, column=0, sticky="WN")
        self.about_link_github.configure(padx=10, pady=10)
        self.about_link_github.bind("<Button-1>",
                                 lambda e: self.link("https://github.com/anopensourcecoder/diary"))



        self.about_footer = Button( self.about_window, text="Close", command=lambda arg1=self.about_window: self.close_about_window(arg1))

        self.about_footer.grid(row=4, column=0, sticky="")
        self.about_footer.configure(padx=10, pady=10 )

        self.about_link_doc = Label(self.about_window, text=" ")
        self.about_link_doc.grid(row=5, column=0, sticky="WN")
        self.about_link_doc.configure(padx=10, pady=0)

    def logo_command(self):
        self.about_command()

    def close_about_window(self, about_window):
        about_window.destroy()

    def link(self, url):
        import webbrowser
        webbrowser.open_new(url)

def main( ):
    root = Tk()
    gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
