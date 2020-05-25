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



    def __init__(self, root):
        d = Diary()
        h = HumanDate()

        root.title("Diary GUI")
        #root.geometry("960x600")
        root.minsize(960, 600)
        #root.config( background="#000000")
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        ROOTPATH = os.path.dirname(__file__)

        font_cal = "Dejavu 18"
        font_gui = "Dejavu 12"
        font_menu = "Dejavu 13"
        font_header_title = "Dejavu 20"
        font_header = "Dejavu 15"
        font_label_input = "Dejavu 10"
        font_input = "Dejavu 16"
        width_go_buttons = 4
        width_input = 7
        wide_scrollbar=20
        height_nav = 32

        font_submit = "Dejavu 11"
        font_result = "Dejavu 16"




        # menu
        menu_bar = Menu(root )
        root.config(menu=menu_bar)

        home_menu = Menu(menu_bar, tearoff=0)
        home_menu.add_command(font=font_menu, label="About",command=self.about_command)
        #home_menu.add_command(font=font_gui, label="Save Diary",)
        #home_menu.add_command(font=font_gui, label="Settings")
        #home_menu.add_command(font=font_gui, label="Import")
        #home_menu.add_command(font=font_gui, label="Export")
        home_menu.add_separator()
        home_menu.add_command(font=font_menu, label="Exit", underline=1, accelerator='Alt-X',
                                   command=lambda arg1=root: self.quit(arg1))

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

        self.main_frame = Frame(root)
        #self.main_frame.configure(background="#ff0000")
        self.main_frame.grid(row=0, column=0, sticky="NSEW")
        self.main_frame.grid_columnconfigure(0, weight=1 )
        self.main_frame.grid_columnconfigure(1, weight=0  )
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)


        self.container = Frame(self.main_frame )
        #self.main_frame.configure(background="#aabbaa")
        self.container.grid(row=0, column=0, sticky="NEWS")
        self.container.grid(row=0, column=1, sticky="NEWS")
        self.container.configure(padx=0, pady=5)

        self.header_frame = Frame(self.container)
        self.header_frame.grid(row=0, column=0, sticky="WE")
        self.header_frame.configure(pady=0)



        self.header_left_frame = Frame(self.header_frame )
        self.header_frame.grid_columnconfigure(0, weight=1, minsize=100)
        self.header_left_frame.grid(row=0, column=0,sticky="W")


        self.header_right_frame = Frame(self.header_frame)
        self.header_frame.grid_columnconfigure(0, weight=1, minsize=100)
        self.header_left_frame.grid(row=0, column=0)
        self.header_right_frame.grid(row=0, column=1, sticky="E")


        ROOT_DIR = os.path.dirname(__file__)
        self.logo = PhotoImage(file=ROOT_DIR + '/logo32.png')
        self.gui_header_logo = Button(self.header_left_frame, width=32, height=height_nav,
                                      text="", image=self.logo, compound=LEFT, command=self.logo_command)
        self.gui_header_logo.grid(row=0, column=0, sticky="NWSE")

        self.date_picker_var = StringVar()
        self.cal = DateEntry(self.header_left_frame, font=font_cal, date_pattern=self.date_picker_pattern,
                             textvariable=self.date_picker_var,
                             selectmode='day', cursor="hand1", width=10)
        self.cal.grid(row=0, column=1, sticky="WE", padx=8 )

        self.empty_label = Label(self.header_left_frame )
        self.empty_label.grid(row=0, column=2, sticky="NWSE", padx=0)

        self.first_entry_button = Button(self.header_right_frame, font=font_gui, width=width_go_buttons , text="<<<", command=self.first_entry)
        self.first_entry_button.grid(row=0, column=3, sticky="NWSE")

        self.prev_entry_button = Button(self.header_right_frame, font=font_gui, width=width_go_buttons , text="<<", command=self.prev_entry)
        self.prev_entry_button.grid(row=0, column=4, sticky="NWSE")

        self.prev_day_button = Button(self.header_right_frame, font=font_gui, width=width_go_buttons , text=" < ", command=self.prev_day)
        self.prev_day_button.grid(row=0, column=5, sticky="NWSE")

        self.today_entry_button = Button(self.header_right_frame, font=font_gui,width=width_go_buttons , text="<>", command=self.today_entry)
        self.today_entry_button.grid(row=0, column=6, sticky="NWSE")

        self.next_day_button = Button(self.header_right_frame, font=font_gui,width=width_go_buttons , text=" >", command=self.next_day)
        self.next_day_button.grid(row=0, column=7, sticky="NWSE")

        self.next_entry_button = Button(self.header_right_frame, font=font_gui, width=width_go_buttons , text=">>", command=self.next_entry)
        self.next_entry_button.grid(row=0, column=8, sticky="NWSE")

        self.last_diary_button = Button(self.header_right_frame, font=font_gui,width=width_go_buttons , text=">>>", command=self.last_diary)
        self.last_diary_button.grid(row=0, column=9, sticky="NWSE")

        self.button_save = Button(self.header_right_frame, font=font_gui, width=width_go_buttons, text="Save" ,
                                  command=self.save_entry)
        self.button_save.grid(row=0, column=10, sticky="NWSE")


        self.container.grid_rowconfigure(0, weight=0,minsize=40)
        self.container.grid_rowconfigure(1, weight=1,minsize=100)
        self.container.grid_columnconfigure(0,minsize = 945 )


        self.editor_frame = Frame(self.container )
        #self.editor_frame.configure(background="#0000ff")
        self.editor_frame.grid(row=1,sticky="NWSE")
        self.editor_frame.grid_columnconfigure(0, weight=1)
        self.editor_frame.grid_rowconfigure(0, weight=1)
        self.editor_frame.configure(padx=0, pady=5)

        self.diary_editor_scroll = Scrollbar(self.editor_frame, width=wide_scrollbar)
        self.diary_editor_scroll.grid(row=0, column=1, sticky="NWES")

        self.diary_editor = Text(self.editor_frame, font=font_gui, wrap=WORD,yscrollcommand=self.diary_editor_scroll.set  )
        self.diary_editor.grid(row=0, column=0, sticky="NWES")

        self.diary_editor_scroll.config(command=self.diary_editor.yview)



        #self.diary_editor.bind('<Return>', (lambda _: self.editor_callback(self.diary_editor)))

        self.diary_editor.bind('<Key>', self.editor_callback )
        #self.diary_editor.bind('<FocusOut>', (lambda _: self.save_entry()))
        #self.diary_editor.bind('<FocusIn>', (lambda _: self.editor_callback(self.diary_editor)))

        # self.diary_editor.bind('<Return>', self.onModification)
        # self.diary_editor.bind('<Button-1>', self.func1)



        # button = Button(root, text="Click me")
        # button.grid()
        # button.bind('<Button-1>', self.func1)

        self.date_picker_var.trace("w", self.date_picker_action)
        self.date_picker_action()

        #self.cal.bind("<<DateEntrySelected>>", self.date_picker_action)

        #main_form.protocol("WM_DELETE_WINDOW", lambda arg1=main_form: self.quit_sofware(arg1))

    def editor_callback(self,event):
        #print(self.diary_editor.get('1.0', 'end-1c'))
        try:
            if event.char:
                self.button_save["state"] = "active"
        except:
            pass

    def save_entry(self):
        entry = self.diary_editor.get('1.0', 'end-1c')
        d.add_diary(entry)
        self.button_save["state"] = "disabled"

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
                self.button_save["state"] = "disabled"

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
