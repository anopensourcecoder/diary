"""Gui script for diary."""
import sys
from tkinter import *
from tkcalendar import Calendar, DateEntry
import os
from . import __version__

import datetime
import click

from  diary.diary import Diary
from diary.humandate import HumanDate

# init Diary Software
d = Diary()
h=HumanDate()

class gui:

    date_picker_pattern = "y mm dd"  # used to display the date at date piker.
    date_picker_format_str = '%Y %m %d'  # used at date function to convert datepiker selected date.
    width_go_buttons = 4
    def __init__(self, main_form):
        d = Diary()
        h = HumanDate()

        main_form.title("Diary GUI")
        main_form.geometry("800x600")
        main_form.minsize(800, 600)
        main_form.grid_rowconfigure(0, weight=1)
        main_form.grid_columnconfigure(0, weight=1)
        ROOTPATH = os.path.dirname(__file__)

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
        main_frame.grid_columnconfigure(0, weight=1)

        main_form.grid_rowconfigure(0, weight=1)
        main_form.grid_columnconfigure(0, weight=1)

        # menu
        menu_bar = Menu(main_form)
        main_form.config(menu=menu_bar)
        main_form.config(menu=menu_bar)

        home_menu = Menu(menu_bar, tearoff=0)
        home_menu.add_command(font=font_menu, label="About",command=self.about_command)
        #home_menu.add_command(font=font_gui, label="Save Diary",)
        #home_menu.add_command(font=font_gui, label="Settings")
        #home_menu.add_command(font=font_gui, label="Import")
        #home_menu.add_command(font=font_gui, label="Export")
        home_menu.add_separator()
        home_menu.add_command(font=font_menu, label="Exit", underline=1, accelerator='Alt-X',
                                   command=lambda arg1=main_form: self.quit(arg1))

        menu_bar.add_cascade(font=font_gui, label="Home", menu=home_menu)
        menu_bar.bind_all("<Alt-x>", self.quit )

        go_menu = Menu(menu_bar, tearoff=0)
        go_menu.add_command(font=font_gui, label="Random Entry" ,command=self.random_entry ,accelerator='Alt-r')
        menu_bar.bind_all("<Alt-r>", self.go_random_entry)

        go_menu.add_command(font=font_gui, label="Today" ,command=self.today_entry ,accelerator='Alt-Up' )
        menu_bar.bind_all("<Alt-Up>", self.go_today)

        go_menu.add_command(font=font_gui, label="Next Day" ,command=self.next_day , accelerator='Alt-Right' )
        menu_bar.bind_all("<Alt-Right>", self.go_next_day)

        go_menu.add_command(font=font_gui, label="Previous Day" ,command=self.prev_day , accelerator='Alt-Left' )
        menu_bar.bind_all("<Alt-Left>", self.go_prev_day)

        go_menu.add_separator()
        go_menu.add_command(font=font_gui, label="Next Entry" ,command=self.next_entry , accelerator='Alt-Right')
        go_menu.add_command(font=font_gui, label="Previous Entry" ,command=self.prev_entry , accelerator='Alt-Left' )
        go_menu.add_separator()
        go_menu.add_command(font=font_gui, label="First Entry",command=self.first_entry)
        go_menu.add_command(font=font_gui, label="Last Entry" ,command=self.last_diary )

        menu_bar.add_cascade(font=font_gui, label="Go", menu=go_menu)

        #edit_menu = Menu(menu_bar, tearoff=0)
        #edit_menu.add_command(font=font_gui, label="Cut")
        #edit_menu.add_command(font=font_gui, label="Copy")
        #edit_menu.add_command(font=font_gui, label="Paste")
        #edit_menu.add_separator()
        #edit_menu.add_command(font=font_gui, label="Delete Current Diary")

        #menu_bar.add_cascade(font=font_gui, label="Edit", menu=edit_menu)

        self.nav_frame = Frame(main_frame)
        self.nav_frame.grid(row=0, column=0, sticky="N")
        self.nav_frame.configure(padx=0, pady=5)

        # import datetime
        #today = datetime.date.today()
        self.date_picker_var = StringVar()
        self.cal = DateEntry(self.nav_frame, font=font_cal, date_pattern=self.date_picker_pattern,
                             textvariable=self.date_picker_var,
                             selectmode='day', cursor="hand1", width=10)
        self.cal.grid(row=0, column=0, sticky="N")

        self.emptylabel = Label(self.nav_frame )
        self.emptylabel.grid(row=0, column=1, sticky="N", padx=10)

        self.button_first = Button(self.nav_frame, font=font_gui, width=self.width_go_buttons , text="<<<", command=self.first_entry)
        self.button_first.grid(row=0, column=2, sticky="N")

        self.button_preview = Button(self.nav_frame, font=font_gui, width=self.width_go_buttons , text="<<", command=self.prev_entry)
        self.button_preview.grid(row=0, column=3, sticky="N")

        self.button_preview = Button(self.nav_frame, font=font_gui, width=self.width_go_buttons , text=" < ", command=self.prev_day)
        self.button_preview.grid(row=0, column=4, sticky="N")

        self.button_today = Button(self.nav_frame, font=font_gui,width=self.width_go_buttons , text="<>", command=self.today_entry)
        self.button_today.grid(row=0, column=5, sticky="N")

        self.button_next = Button(self.nav_frame, font=font_gui,width=self.width_go_buttons , text=" >", command=self.next_day)
        self.button_next.grid(row=0, column=6, sticky="N")

        self.button_next = Button(self.nav_frame, font=font_gui, width=self.width_go_buttons , text=">>", command=self.next_entry)
        self.button_next.grid(row=0, column=7, sticky="N")

        self.button_last = Button(self.nav_frame, font=font_gui,width=self.width_go_buttons , text=">>>", command=self.last_diary)
        self.button_last.grid(row=0, column=8, sticky="N")

        self.editor_frame = Frame(main_frame)
        self.editor_frame.grid(row=2, column=0, sticky="N")

        self.diary_editor = Text(self.editor_frame, font=font_gui, width="74", height="10")
        self.diary_editor.grid()

        # self.diary_editor.bind('<Return>', self.onModification)
        # self.diary_editor.bind('<Button-1>', self.func1)

        # button = Button(root, text="Click me")
        # button.grid()
        # button.bind('<Button-1>', self.func1)

        self.date_picker_var.trace("w", self.date_picker_action)
        self.date_picker_action()

        #self.cal.bind("<<DateEntrySelected>>", self.date_picker_action)

        #main_form.protocol("WM_DELETE_WINDOW", lambda arg1=main_form: self.quit_sofware(arg1))



    def first_entry(self):
        d.go_first_diary()
        entry = d.get_diary()
        entry_datetime = entry.get_item_date()
        today_date_str = entry_datetime.strftime(self.date_picker_format_str)
        self.date_picker_var.set(today_date_str)

    def prev_entry(self):
        result = d.go_previous_diary()
        entry = d.get_diary()
        entry_datetime = entry.get_item_date()
        today_date_str = entry_datetime.strftime(self.date_picker_format_str)
        self.date_picker_var.set(today_date_str)

    def prev_day(self):
        d.set_day(-1)
        entry = d.get_diary()
        entry_datetime = entry.get_item_date()
        today_date_str = entry_datetime.strftime(self.date_picker_format_str)
        self.date_picker_var.set(today_date_str)

    def today_entry(self):

        d.set_date("")
        entry = d.get_diary()
        entry_datetime =  entry.get_item_date()
        today_date_str = entry_datetime.strftime(self.date_picker_format_str)
        self.date_picker_var.set(today_date_str)

    def next_day(self):
        d.set_day(1)
        entry = d.get_diary()
        entry_datetime = entry.get_item_date()
        today_date_str = entry_datetime.strftime(self.date_picker_format_str)
        self.date_picker_var.set(today_date_str)

    def next_entry(self):
        result = d.go_next_diary()
        entry = d.get_diary()
        entry_datetime = entry.get_item_date()
        today_date_str = entry_datetime.strftime(self.date_picker_format_str)
        self.date_picker_var.set(today_date_str)


    def last_diary(self):
        d.go_last_diary()
        entry = d.get_diary()
        entry_datetime = entry.get_item_date()
        today_date_str = entry_datetime.strftime(self.date_picker_format_str)
        self.date_picker_var.set(today_date_str)

    def random_entry(self):
        d.go_random_entry()
        entry = d.get_diary()
        entry_datetime = entry.get_item_date()
        today_date_str = entry_datetime.strftime(self.date_picker_format_str)
        self.date_picker_var.set(today_date_str)

    def date_picker_action(self, *args):

        try:
            current_date_picker_str = self.date_picker_var.get()
            current_date_picker_datetime_obj = datetime.datetime.strptime(current_date_picker_str,'%Y %m %d')
            self.diary_editor.delete('1.0', END)

            d.set_datetime( current_date_picker_datetime_obj )
            entry = d.get_diary()
            if entry.item_content:
                self.diary_editor.insert('1.0', entry.get_item_content())
                self.diary_editor_before = self.diary_editor.get('1.0', 'end-1c')

        except:
            pass




    def get_calstringvar_date_obj(self):
        date_obj = datetime.datetime.strptime(self.date_picker_var.get(), self.date_picker_format_str)
        return date_obj

    def quit(self, event):
        #print("quitting...")
        sys.exit(0)




    def go_today(self, event):
        self.today_entry()

    def go_prev_day(self, event):
        self.prev_day()

    def go_next_day(self, event):
        self.next_day()

    def go_random_entry(self, event):
        self.random_entry()

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
